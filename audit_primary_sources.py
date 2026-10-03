import sqlite3

DB = "bharat_knowledge.db"

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("""
SELECT
    e.evidence_id,
    e.topic,
    e.evidence_type,
    e.claim,
    r.reference_id,
    r.primary_source_url,
    r.scholarly_url,
    r.source_url
FROM evidence e
LEFT JOIN references_data r
    ON e.evidence_id = r.evidence_id
WHERE r.primary_source_url IS NULL
   OR TRIM(r.primary_source_url) = ''
ORDER BY e.evidence_id
""")

rows = cur.fetchall()

print("=" * 80)
print("RECORDS WITHOUT PRIMARY SOURCE URL")
print("=" * 80)

for row in rows:
    print()
    print(f"Evidence ID: {row['evidence_id']}")
    print(f"Reference ID: {row['reference_id']}")
    print(f"Topic: {row['topic']}")
    print(f"Evidence Type: {row['evidence_type']}")
    print(f"Claim: {row['claim']}")
    print(f"Scholarly URL: {row['scholarly_url']}")
    print(f"Source URL: {row['source_url']}")
    print("-" * 80)

print()
print(f"Records without primary source URL: {len(rows)}")

conn.close()