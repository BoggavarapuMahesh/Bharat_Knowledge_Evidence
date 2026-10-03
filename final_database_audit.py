import sqlite3
from collections import Counter

DB = "bharat_knowledge.db"

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

print("=" * 70)
print("BHARAT KNOWLEDGE EVIDENCE — FINAL DATABASE AUDIT")
print("=" * 70)

# ---------------------------------------------------------
# 1. TABLE COUNTS
# ---------------------------------------------------------
print("\n1. TABLE COUNTS")
print("-" * 70)

tables = [
    "sources",
    "evidence",
    "references_data",
    "contributions",
    "people",
    "places",
    "fields",
    "historical_periods",
    "texts",
    "verses",
    "evidence_types",
    "evidence_fields",
    "evidence_places",
    "evidence_people",
    "evidence_texts",
    "evidence_quality"
]

counts = {}

for table in tables:
    try:
        count = cur.execute(
            f"SELECT COUNT(*) FROM {table}"
        ).fetchone()[0]
        counts[table] = count
        print(f"{table:25} {count}")
    except Exception as e:
        print(f"{table:25} ERROR: {e}")

# ---------------------------------------------------------
# 2. EVIDENCE WITHOUT REFERENCES
# ---------------------------------------------------------
print("\n2. EVIDENCE WITHOUT REFERENCES")
print("-" * 70)

rows = cur.execute("""
    SELECT e.evidence_id, e.topic
    FROM evidence e
    LEFT JOIN references_data r
        ON e.evidence_id = r.evidence_id
    WHERE r.reference_id IS NULL
    ORDER BY e.evidence_id
""").fetchall()

if rows:
    for r in rows:
        print(f"Evidence {r['evidence_id']}: {r['topic']}")
else:
    print("PASS — Every evidence record has at least one reference.")

# ---------------------------------------------------------
# 3. REFERENCES WITHOUT URL
# ---------------------------------------------------------
print("\n3. REFERENCES WITHOUT ANY URL")
print("-" * 70)

rows = cur.execute("""
    SELECT reference_id, evidence_id
    FROM references_data
    WHERE
        COALESCE(TRIM(source_url), '') = ''
        AND COALESCE(TRIM(url), '') = ''
        AND COALESCE(TRIM(primary_source_url), '') = ''
        AND COALESCE(TRIM(scholarly_url), '') = ''
        AND COALESCE(TRIM(scholarly_source_url), '') = ''
    ORDER BY reference_id
""").fetchall()

if rows:
    for r in rows:
        print(
            f"Reference {r['reference_id']} "
            f"(Evidence {r['evidence_id']})"
        )
else:
    print("PASS — Every reference has at least one URL.")

# ---------------------------------------------------------
# 4. PRIMARY SOURCE COVERAGE
# ---------------------------------------------------------
print("\n4. PRIMARY SOURCE URL COVERAGE")
print("-" * 70)

total_refs = cur.execute(
    "SELECT COUNT(*) FROM references_data"
).fetchone()[0]

primary_refs = cur.execute("""
    SELECT COUNT(*)
    FROM references_data
    WHERE TRIM(COALESCE(primary_source_url, '')) <> ''
""").fetchone()[0]

print(f"Primary-source URLs: {primary_refs}/{total_refs}")

if total_refs:
    print(
        f"Coverage: {primary_refs / total_refs * 100:.2f}%"
    )

# ---------------------------------------------------------
# 5. SCHOLARLY SOURCE COVERAGE
# ---------------------------------------------------------
print("\n5. SCHOLARLY SOURCE URL COVERAGE")
print("-" * 70)

scholarly_refs = cur.execute("""
    SELECT COUNT(*)
    FROM references_data
    WHERE
        TRIM(COALESCE(scholarly_url, '')) <> ''
        OR TRIM(COALESCE(scholarly_source_url, '')) <> ''
""").fetchone()[0]

print(f"Scholarly URLs: {scholarly_refs}/{total_refs}")

if total_refs:
    print(
        f"Coverage: {scholarly_refs / total_refs * 100:.2f}%"
    )

# ---------------------------------------------------------
# 6. VERIFICATION STATUS
# ---------------------------------------------------------
print("\n6. VERIFICATION STATUS")
print("-" * 70)

rows = cur.execute("""
    SELECT
        COALESCE(NULLIF(TRIM(verification_status), ''), '[EMPTY]')
        AS status,
        COUNT(*) AS count
    FROM references_data
    GROUP BY status
    ORDER BY count DESC
""").fetchall()

for r in rows:
    print(f"{r['status']:55} {r['count']}")

# ---------------------------------------------------------
# 7. CITATION VERIFIED
# ---------------------------------------------------------
print("\n7. CITATION VERIFIED")
print("-" * 70)

rows = cur.execute("""
    SELECT
        COALESCE(NULLIF(TRIM(citation_verified), ''), '[EMPTY]')
        AS status,
        COUNT(*) AS count
    FROM references_data
    GROUP BY status
    ORDER BY count DESC
""").fetchall()

for r in rows:
    print(f"{r['status']:55} {r['count']}")

# ---------------------------------------------------------
# 8. EMPTY IMPORTANT EVIDENCE FIELDS
# ---------------------------------------------------------
print("\n8. EMPTY IMPORTANT EVIDENCE FIELDS")
print("-" * 70)

important_fields = [
    "topic",
    "claim",
    "evidence_type",
    "historical_period",
    "location",
    "description"
]

for field in important_fields:
    count = cur.execute(f"""
        SELECT COUNT(*)
        FROM evidence
        WHERE TRIM(COALESCE({field}, '')) = ''
    """).fetchone()[0]

    print(f"{field:25} {count} empty")

# ---------------------------------------------------------
# 9. EMPTY REFERENCE FIELDS
# ---------------------------------------------------------
print("\n9. EMPTY IMPORTANT REFERENCE FIELDS")
print("-" * 70)

reference_fields = [
    "reference_text",
    "page_or_verse",
    "citation_author",
    "citation_work",
    "citation_year",
    "verification_status",
    "source_reliability"
]

for field in reference_fields:
    count = cur.execute(f"""
        SELECT COUNT(*)
        FROM references_data
        WHERE TRIM(COALESCE({field}, '')) = ''
    """).fetchone()[0]

    print(f"{field:25} {count} empty")

# ---------------------------------------------------------
# 10. DUPLICATE URL CHECK
# ---------------------------------------------------------
print("\n10. REPEATED URL CHECK")
print("-" * 70)

rows = cur.execute("""
    SELECT primary_source_url, COUNT(*) AS count
    FROM references_data
    WHERE TRIM(COALESCE(primary_source_url, '')) <> ''
    GROUP BY primary_source_url
    HAVING COUNT(*) > 1
    ORDER BY count DESC
""").fetchall()

if rows:
    print("Repeated primary URLs are NOT automatically errors.")
    print("They often mean multiple claims use the same primary text.")
    for r in rows[:20]:
        print(f"{r['count']:3}  {r['primary_source_url']}")
else:
    print("No repeated primary URLs.")

# ---------------------------------------------------------
# 11. DUPLICATE EVIDENCE CLAIM CHECK
# ---------------------------------------------------------
print("\n11. POSSIBLE DUPLICATE EVIDENCE CLAIMS")
print("-" * 70)

rows = cur.execute("""
    SELECT
        LOWER(TRIM(claim)) AS normalized_claim,
        COUNT(*) AS count,
        GROUP_CONCAT(evidence_id) AS evidence_ids
    FROM evidence
    WHERE TRIM(COALESCE(claim, '')) <> ''
    GROUP BY LOWER(TRIM(claim))
    HAVING COUNT(*) > 1
    ORDER BY count DESC
""").fetchall()

if rows:
    for r in rows:
        print(
            f"{r['count']} records: "
            f"Evidence IDs {r['evidence_ids']}"
        )
else:
    print("PASS — No exact duplicate claims detected.")

# ---------------------------------------------------------
# 12. RELATIONSHIP COVERAGE
# ---------------------------------------------------------
print("\n12. RELATIONSHIP COVERAGE")
print("-" * 70)

relationship_tables = [
    ("evidence_fields", "Evidence → Fields"),
    ("evidence_places", "Evidence → Places"),
    ("evidence_people", "Evidence → People"),
    ("evidence_texts", "Evidence → Texts"),
    ("evidence_quality", "Evidence → Quality")
]

for table, label in relationship_tables:
    total = cur.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(f"{label:30} {total} links")

# ---------------------------------------------------------
# 13. ORPHAN RELATIONSHIPS
# ---------------------------------------------------------
print("\n13. ORPHAN RELATIONSHIP CHECK")
print("-" * 70)

checks = [
    (
        "evidence_fields",
        "evidence_id",
        "evidence",
        "evidence_id"
    ),
    (
        "evidence_places",
        "evidence_id",
        "evidence",
        "evidence_id"
    ),
    (
        "evidence_people",
        "evidence_id",
        "evidence",
        "evidence_id"
    ),
    (
        "evidence_texts",
        "evidence_id",
        "evidence",
        "evidence_id"
    ),
    (
        "evidence_quality",
        "evidence_id",
        "evidence",
        "evidence_id"
    )
]

orphan_total = 0

for table, column, parent, parent_column in checks:

    count = cur.execute(f"""
        SELECT COUNT(*)
        FROM {table} t
        LEFT JOIN {parent} p
            ON t.{column} = p.{parent_column}
        WHERE p.{parent_column} IS NULL
    """).fetchone()[0]

    orphan_total += count

    print(f"{table:25} {count} orphan records")

# ---------------------------------------------------------
# 14. DATABASE INTEGRITY
# ---------------------------------------------------------
print("\n14. SQLITE DATABASE INTEGRITY")
print("-" * 70)

integrity = cur.execute(
    "PRAGMA integrity_check"
).fetchone()[0]

print(integrity)

# ---------------------------------------------------------
# 15. FOREIGN KEY CHECK
# ---------------------------------------------------------
print("\n15. FOREIGN KEY CHECK")
print("-" * 70)

rows = cur.execute(
    "PRAGMA foreign_key_check"
).fetchall()

if rows:
    print("Foreign-key problems detected:", len(rows))
    for r in rows[:20]:
        print(tuple(r))
else:
    print("PASS — No foreign-key violations detected.")

# ---------------------------------------------------------
# FINAL SUMMARY
# ---------------------------------------------------------
print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

evidence_count = counts.get("evidence", 0)
reference_count = counts.get("references_data", 0)

print(f"Evidence records       : {evidence_count}")
print(f"Reference records      : {reference_count}")
print(f"Evidence/reference gap: {evidence_count - reference_count}")

print()

if integrity == "ok":
    print("Database integrity     : PASS")
else:
    print("Database integrity     : CHECK REQUIRED")

if not rows:
    print("Foreign keys           : PASS")

print()
print("AUDIT COMPLETE")
print("=" * 70)

conn.close()