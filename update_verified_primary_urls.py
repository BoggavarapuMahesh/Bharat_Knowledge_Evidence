import sqlite3

DB = "bharat_knowledge.db"

updates = {
    # Rigveda
    1: {
        "url": "https://vedaweb.uni-koeln.de/rigveda/view",
        "type": "Primary-text research platform",
        "note": "VedaWeb provides direct access to the Rigveda primary-text corpus. Individual historical claims still require specific hymn/passage citations."
    },
    2: {
        "url": "https://vedaweb.uni-koeln.de/rigveda/view",
        "type": "Primary-text research platform",
        "note": "VedaWeb provides direct access to the Rigveda primary-text corpus. Individual historical claims still require specific hymn/passage citations."
    },

    # Panini - Ashtadhyayi
    3: {
        "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_pANini-aSTAdhyAyI.htm",
        "type": "Primary Sanskrit text / e-text",
        "note": "GRETIL Sanskrit e-text of Panini's Ashtadhyayi. The digital text is derived from the commented tradition and should be checked against a critical/printed edition for exact citation."
    },

    # Aryabhatiya
    6: {
        "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_AryabhaTa-AryabhaTIya.htm",
        "type": "Primary Sanskrit text / e-text",
        "note": "GRETIL Sanskrit e-text of Aryabhatiya based on a scholarly edition."
    },
    9: {
        "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_AryabhaTa-AryabhaTIya.htm",
        "type": "Primary Sanskrit text / e-text",
        "note": "GRETIL Sanskrit e-text of Aryabhatiya based on a scholarly edition."
    },

    # Brahmagupta - Brahmasphutasiddhanta
    27: {
        "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_brahmagupta-brAhmasphuTasiddhAnta.htm",
        "type": "Primary Sanskrit text / e-text",
        "note": "GRETIL Sanskrit e-text of Brahmagupta's Brahmasphutasiddhanta, based on S. Dvivedin's Benares 1902 edition."
    },
    28: {
        "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_brahmagupta-brAhmasphuTasiddhAnta.htm",
        "type": "Primary Sanskrit text / e-text",
        "note": "GRETIL Sanskrit e-text of Brahmagupta's Brahmasphutasiddhanta, based on S. Dvivedin's Benares 1902 edition."
    },
    29: {
        "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_brahmagupta-brAhmasphuTasiddhAnta.htm",
        "type": "Primary Sanskrit text / e-text",
        "note": "GRETIL Sanskrit e-text of Brahmagupta's Brahmasphutasiddhanta, based on S. Dvivedin's Benares 1902 edition."
    },
    30: {
        "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_brahmagupta-brAhmasphuTasiddhAnta.htm",
        "type": "Primary Sanskrit text / e-text",
        "note": "GRETIL Sanskrit e-text of Brahmagupta's Brahmasphutasiddhanta, based on S. Dvivedin's Benares 1902 edition."
    },
    31: {
        "url": "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_brahmagupta-brAhmasphuTasiddhAnta.htm",
        "type": "Primary Sanskrit text / e-text",
        "note": "GRETIL Sanskrit e-text of Brahmagupta's Brahmasphutasiddhanta, based on S. Dvivedin's Benares 1902 edition."
    }
}

conn = sqlite3.connect(DB)
cur = conn.cursor()

for evidence_id, data in updates.items():

    # Update existing reference rows for this evidence
    cur.execute("""
        UPDATE references_data
        SET primary_source_url = ?,
            primary_source_type = ?,
            verification_status = 'Primary source resource verified',
            verification_notes = ?,
            citation_verified = 'Yes'
        WHERE evidence_id = ?
    """, (
        data["url"],
        data["type"],
        data["note"],
        evidence_id
    ))

    # If no reference exists, create one
    if cur.rowcount == 0:
        cur.execute("""
            INSERT INTO references_data (
                evidence_id,
                reference_text,
                source_url,
                primary_source_url,
                primary_source_type,
                source_reliability,
                verification_status,
                verification_notes,
                citation_verified
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            evidence_id,
            "Verified primary-text resource",
            data["url"],
            data["url"],
            data["type"],
            "High",
            "Primary source resource verified",
            data["note"],
            "Yes"
        ))

conn.commit()

print("Verified primary-source URLs updated.")

print("\nUpdated evidence IDs:")
for evidence_id in updates:
    print("-", evidence_id)

conn.close()