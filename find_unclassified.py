import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

query = """
SELECT
    r.reference_id,
    r.evidence_id,
    r.reference_text,
    r.url,
    r.source_url,
    r.citation_author,
    r.citation_work,
    r.citation_year,
    r.verification_status,
    r.verification_notes
FROM references_data r
WHERE r.citation_verified IS NULL
   OR TRIM(r.citation_verified) = ''
ORDER BY r.reference_id;
"""

rows = cursor.execute(query).fetchall()

print("\nUNCLASSIFIED REFERENCES")
print("=" * 80)

for row in rows:
    print("\nReference ID:", row[0])
    print("Evidence ID:", row[1])
    print("Reference:", row[2])
    print("URL:", row[3])
    print("Source URL:", row[4])
    print("Author:", row[5])
    print("Work:", row[6])
    print("Year:", row[7])
    print("Verification Status:", row[8])
    print("Notes:", row[9])

print("\nTOTAL UNCLASSIFIED:", len(rows))

conn.close()