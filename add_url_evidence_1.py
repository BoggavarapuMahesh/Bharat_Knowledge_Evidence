import sqlite3

DB = "bharat_knowledge.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""
INSERT INTO references_data (
    evidence_id,
    reference_text,
    citation_author,
    citation_work,
    citation_publisher,
    citation_year,
    scholarly_reference,
    scholarly_url,
    scholarly_source_url,
    scholarly_source_type,
    source_reliability,
    citation_verified
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    1,
    "The Rigveda is the oldest Veda and a compilation of 1,028 hymns; its formation took place over several centuries.",
    "L. Mahesh Deokar and Jean-Luc Chevillard",
    "The Cambridge World History of Lexicography – Ancient India",
    "Cambridge University Press",
    2019,
    "Cambridge World History of Lexicography",
    "https://doi.org/10.1017/9781316827437.005",
    "https://www.cambridge.org/core/books/abs/cambridge-world-history-of-lexicography/ancient-india/67571FDA197C96057C704DC51D02227F",
    "Academic Book Chapter",
    "High",
    "Yes"
))

conn.commit()

print("Evidence ID 1 reference added successfully.")

cur.execute("""
SELECT reference_id, evidence_id, scholarly_url, citation_verified
FROM references_data
WHERE evidence_id = 1
ORDER BY reference_id DESC
LIMIT 1
""")

print(cur.fetchone())

conn.close()