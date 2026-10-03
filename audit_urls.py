import sqlite3

DB = "bharat_knowledge.db"

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

print("=" * 80)
print("URL AUDIT")
print("=" * 80)

cur.execute("""
SELECT
    e.evidence_id,
    e.topic,
    e.claim,
    r.reference_id,
    r.url,
    r.source_url,
    r.primary_source_url,
    r.scholarly_url,
    r.scholarly_source_url
FROM evidence e
LEFT JOIN references_data r
    ON e.evidence_id = r.evidence_id
ORDER BY e.evidence_id
""")

rows = cur.fetchall()

print(f"\nTotal evidence records: {len(set(row['evidence_id'] for row in rows))}")
print(f"Total reference rows: {len([r for r in rows if r['reference_id'] is not None])}")

print("\n" + "=" * 80)
print("RECORDS WITH MISSING URL INFORMATION")
print("=" * 80)

missing_count = 0

for row in rows:
    urls = [
        row["url"],
        row["source_url"],
        row["primary_source_url"],
        row["scholarly_url"],
        row["scholarly_source_url"]
    ]

    if not any(urls):
        missing_count += 1

        print(f"\nEvidence ID: {row['evidence_id']}")
        print(f"Reference ID: {row['reference_id']}")
        print(f"Topic: {row['topic']}")
        print(f"Claim: {row['claim']}")

print(f"\nTotal records with NO URL: {missing_count}")

print("\n" + "=" * 80)
print("URL COMPLETENESS")
print("=" * 80)

fields = [
    ("url", "Main URL"),
    ("source_url", "Source URL"),
    ("primary_source_url", "Primary Source URL"),
    ("scholarly_url", "Scholarly URL"),
    ("scholarly_source_url", "Scholarly Source URL")
]

for column, label in fields:
    count = sum(
        1 for row in rows
        if row[column] is not None and str(row[column]).strip() != ""
    )

    print(f"{label}: {count}/{len(rows)}")

print("\n" + "=" * 80)
print("POTENTIAL DUPLICATE URLS")
print("=" * 80)

cur.execute("""
SELECT url, COUNT(*) AS count
FROM references_data
WHERE url IS NOT NULL
  AND TRIM(url) != ''
GROUP BY url
HAVING COUNT(*) > 1
ORDER BY count DESC
""")

duplicates = cur.fetchall()

if duplicates:
    for row in duplicates:
        print(f"{row['count']} records -> {row['url']}")
else:
    print("No duplicate URLs found.")

conn.close()

print("\n" + "=" * 80)
print("URL AUDIT COMPLETE")
print("=" * 80)