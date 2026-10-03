import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

columns = [
    ("citation_author", "TEXT"),
    ("citation_work", "TEXT"),
    ("citation_edition", "TEXT"),
    ("citation_publisher", "TEXT"),
    ("citation_year", "TEXT"),
    ("citation_volume", "TEXT"),
    ("citation_page", "TEXT"),
    ("citation_book", "TEXT"),
    ("citation_chapter", "TEXT"),
    ("citation_verse", "TEXT"),
    ("original_language", "TEXT"),
    ("translation_used", "TEXT"),
    ("translator", "TEXT"),
    ("source_url", "TEXT"),
    ("source_access_date", "TEXT"),
    ("scholarly_reference", "TEXT"),
    ("scholarly_url", "TEXT"),
    ("verification_status", "TEXT"),
    ("verification_notes", "TEXT")
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

print("Citation structure added successfully.")
print("Citation fields added:", len(columns))