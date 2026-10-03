import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

columns = [
    ("primary_source_url", "TEXT"),
    ("primary_source_type", "TEXT"),
    ("scholarly_source_url", "TEXT"),
    ("scholarly_source_type", "TEXT"),
    ("source_access_date", "TEXT"),
    ("source_reliability", "TEXT"),
    ("citation_verified", "TEXT")
]

existing = {
    row[1]
    for row in cursor.execute("PRAGMA table_info(references_data)")
}

for column, data_type in columns:
    if column not in existing:
        cursor.execute(
            f"ALTER TABLE references_data ADD COLUMN {column} {data_type}"
        )

conn.commit()
conn.close()

print("Source-quality fields added successfully.")
print("New fields:", len(columns))