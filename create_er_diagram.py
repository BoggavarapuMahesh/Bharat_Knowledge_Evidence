import sqlite3
from pathlib import Path

DB = "bharat_knowledge.db"
OUTPUT = "bharat_knowledge_er_diagram.mmd"

conn = sqlite3.connect(DB)
cur = conn.cursor()

tables = cur.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
      AND name NOT LIKE 'sqlite_%'
    ORDER BY name
""").fetchall()

lines = []
lines.append("erDiagram")

for (table_name,) in tables:
    columns = cur.execute(f'PRAGMA table_info("{table_name}")').fetchall()
    foreign_keys = cur.execute(f'PRAGMA foreign_key_list("{table_name}")').fetchall()

    lines.append(f"    {table_name} {{")

    for col in columns:
        cid, name, data_type, not_null, default_value, pk = col

        data_type = data_type or "TEXT"
        data_type = data_type.replace(" ", "_")

        if pk:
            lines.append(f'        {data_type} {name} PK')
        else:
            lines.append(f'        {data_type} {name}')

    lines.append("    }")

# Add relationships
for (table_name,) in tables:
    foreign_keys = cur.execute(
        f'PRAGMA foreign_key_list("{table_name}")'
    ).fetchall()

    for fk in foreign_keys:
        referenced_table = fk[2]
        from_column = fk[3]

        lines.append(
            f'    {referenced_table} ||--o{{ {table_name} : "references"'
        )

conn.close()

Path(OUTPUT).write_text("\n".join(lines), encoding="utf-8")

print("=" * 60)
print("ER DIAGRAM CREATED")
print("=" * 60)
print()
print("Database:", DB)
print("Tables:", len(tables))
print("Output:", OUTPUT)
print()
print("The database was NOT modified.")