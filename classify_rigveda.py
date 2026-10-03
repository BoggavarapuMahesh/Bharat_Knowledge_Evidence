import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

updates = {
    1: {
        "primary_source_type": "Primary textual corpus",
        "source_reliability": "High",
        "citation_verified": "Source-level record; individual claim citations required"
    },

    11: {
        "primary_source_type": "Primary textual corpus",
        "source_reliability": "High",
        "citation_verified": "Source-level record; individual claim citations required"
    }
}

for reference_id, data in updates.items():

    fields = []
    values = []

    for field, value in data.items():
        fields.append(f"{field} = ?")
        values.append(value)

    values.append(reference_id)

    query = f"""
        UPDATE references_data
        SET {", ".join(fields)}
        WHERE reference_id = ?
    """

    cursor.execute(query, values)

conn.commit()

print("Rigveda source records classified successfully.")
print("References updated:", len(updates))

conn.close()