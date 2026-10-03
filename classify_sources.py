import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

updates = {
    2: {
        "scholarly_source_type": "Academic historical reference",
        "source_reliability": "High",
        "citation_verified": "Pending primary-text verification"
    },
    3: {
        "scholarly_source_type": "Academic historical reference",
        "source_reliability": "High",
        "citation_verified": "Pending primary-text verification"
    },
    4: {
        "scholarly_source_type": "Academic historical reference",
        "source_reliability": "High",
        "citation_verified": "Pending primary-text verification"
    },
    5: {
        "scholarly_source_type": "Scholarly journal article",
        "source_reliability": "High",
        "citation_verified": "Pending detailed article verification"
    },
    6: {
        "scholarly_source_type": "National Library of Medicine catalog",
        "source_reliability": "High",
        "citation_verified": "Bibliographic verification"
    },
    7: {
        "scholarly_source_type": "PubMed-indexed historical research",
        "source_reliability": "High",
        "citation_verified": "Scholarly source verified"
    },
    8: {
        "scholarly_source_type": "Academic philosophy reference",
        "source_reliability": "High",
        "citation_verified": "Scholarly source verified"
    },
    9: {
        "scholarly_source_type": "Academic philosophy reference",
        "source_reliability": "High",
        "citation_verified": "Scholarly source verified"
    },
    10: {
        "scholarly_source_type": "Academic philosophy reference",
        "source_reliability": "High",
        "citation_verified": "Scholarly source verified"
    },
    12: {
        "primary_source_type": "Primary textual source translation",
        "source_reliability": "Medium",
        "citation_verified": "Pending edition verification"
    },
    13: {
        "primary_source_type": "Primary textual source translation",
        "source_reliability": "Medium",
        "citation_verified": "Pending edition verification"
    },
    14: {
        "primary_source_type": "Primary textual source translation",
        "source_reliability": "Medium",
        "citation_verified": "Pending edition verification"
    },
    15: {
        "primary_source_type": "Primary textual source translation",
        "source_reliability": "Medium",
        "citation_verified": "Pending edition verification"
    },
    16: {
        "primary_source_type": "Primary textual source translation",
        "source_reliability": "Medium",
        "citation_verified": "Pending edition verification"
    },
    17: {
        "primary_source_type": "Primary textual source translation",
        "source_reliability": "Medium",
        "citation_verified": "Pending edition verification"
    },
    18: {
        "scholarly_source_type": "Peer-reviewed scholarly article",
        "source_reliability": "High",
        "citation_verified": "Scholarly source verified"
    },
    19: {
        "primary_source_type": "Historical text translation",
        "source_reliability": "Medium",
        "citation_verified": "Pending edition verification"
    },
    20: {
        "scholarly_source_type": "PubMed-indexed historical research",
        "source_reliability": "High",
        "citation_verified": "Scholarly source verified"
    },
    21: {
        "primary_source_type": "Primary textual source translation",
        "source_reliability": "Medium",
        "citation_verified": "Pending edition verification"
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

print("Source classification completed.")
print("References classified:", len(updates))

conn.close()