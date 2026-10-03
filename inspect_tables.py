import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

tables = cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name;
""").fetchall()

for table in tables:
    table_name = table[0]

    print("\n" + "=" * 60)
    print("TABLE:", table_name)
    print("=" * 60)

    columns = cursor.execute(
        f'PRAGMA table_info("{table_name}")'
    ).fetchall()

    for column in columns:
        print(column[1], "|", column[2])

conn.close()