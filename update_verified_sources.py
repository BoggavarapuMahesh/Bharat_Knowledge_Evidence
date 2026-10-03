import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

updates = {
    5: {
        "scholarly_source_url": "https://journals.sagepub.com/doi/10.1177/09719458241226574",
        "scholarly_source_type": "Scholarly journal article",
        "source_reliability": "High",
        "citation_verified": "Scholarly source verified; historical dating remains debated"
    },

    7: {
        "scholarly_source_url": "https://pubmed.ncbi.nlm.nih.gov/23788147/",
        "scholarly_source_type": "PubMed-indexed historical review",
        "source_reliability": "High",
        "citation_verified": "Scholarly source verified; historical claims require qualification"
    },

    18: {
        "scholarly_source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3336764/",
        "scholarly_source_type": "Scholarly article",
        "source_reliability": "High",
        "citation_verified": "Scholarly source verified"
    },

    20: {
        "scholarly_source_url": "https://pubmed.ncbi.nlm.nih.gov/11244521/",
        "scholarly_source_type": "PubMed-indexed historical article",
        "source_reliability": "High",
        "citation_verified": "Scholarly source verified"
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

print("Verified scholarly sources updated.")
print("References updated:", len(updates))

conn.close()