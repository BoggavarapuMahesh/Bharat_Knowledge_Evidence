import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

columns = cursor.execute(
    "PRAGMA table_info(references_data)"
).fetchall()

print("\nREFERENCES_DATA COLUMNS:")
print("-" * 50)

for column in columns:
    print(column[1])

print("\nTOTAL COLUMNS:", len(columns))

conn.close()