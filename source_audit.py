import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

query = """
SELECT
    r.reference_id,
    e.evidence_id,
    e.topic,
    r.url,
    r.source_url,
    r.primary_source_url,
    r.primary_source_type,
    r.scholarly_source_url,
    r.scholarly_source_type,
    r.source_reliability,
    r.citation_verified
FROM references_data r
LEFT JOIN evidence e
    ON r.evidence_id = e.evidence_id
ORDER BY r.reference_id;
"""

rows = cursor.execute(query).fetchall()

print("\nSOURCE AUDIT")
print("=" * 100)

for row in rows:
    print("\nReference ID:", row[0])
    print("Evidence ID:", row[1])
    print("Topic:", row[2])
    print("URL:", row[3])
    print("Source URL:", row[4])
    print("Primary Source URL:", row[5])
    print("Primary Source Type:", row[6])
    print("Scholarly Source URL:", row[7])
    print("Scholarly Source Type:", row[8])
    print("Source Reliability:", row[9])
    print("Citation Verified:", row[10])

print("\n" + "=" * 100)
print("TOTAL REFERENCES:", len(rows))

conn.close()