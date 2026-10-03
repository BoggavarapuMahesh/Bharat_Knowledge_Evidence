import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

updates = {
    12: {
        "primary_source_url": "https://forage.com/upanishads/principal-upanishads/katha/",
        "primary_source_type": "Primary text translation",
        "citation_verified": "Primary text located; edition verification pending"
    },

    13: {
        "primary_source_url": "https://upasanayoga.org/SvetU.htm",
        "primary_source_type": "Primary text translation",
        "citation_verified": "Primary text located; edition verification pending"
    },

    14: {
        "primary_source_url": "https://upasanayoga.org/SvetU.htm",
        "primary_source_type": "Primary text translation",
        "citation_verified": "Primary text located; edition verification pending"
    },

    15: {
        "primary_source_url": "https://texts.wara.in/upanishads/shvetashvatara/",
        "primary_source_type": "Primary text translation",
        "citation_verified": "Primary text located; edition verification pending"
    },

    16: {
        "primary_source_url": "https://upasanayoga.org/SvetU.htm",
        "primary_source_type": "Primary text translation",
        "citation_verified": "Primary text located; edition verification pending"
    },

    17: {
        "primary_source_url": "https://darshya.online/upanishads/maitri-upanishad",
        "primary_source_type": "Primary text translation",
        "citation_verified": "Primary text located; edition verification pending"
    },

    19: {
        "primary_source_url": "https://en.wikisource.org/wiki/Sushruta_Samhita,_Volume_1/Chapter_25",
        "primary_source_type": "Historical text translation",
        "citation_verified": "Primary text located; edition verification pending"
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

print("Primary-source links added successfully.")
print("References updated:", len(updates))

conn.close()