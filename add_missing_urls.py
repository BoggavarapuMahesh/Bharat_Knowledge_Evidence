import sqlite3

DB = "bharat_knowledge.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

records = [

    (
        2,
        "The Rigveda is the oldest Veda and a compilation of 1,028 hymns.",
        "Stephanie W. Jamison and Joel P. Brereton",
        "The Ancient Languages of Asia and the Americas – Sanskrit",
        "Cambridge University Press",
        2008,
        "https://www.cambridge.org/core/books/ancient-languages-of-asia-and-the-americas/sanskrit/CF7D5B91F9736880C0CECAC672754AEB",
        "https://doi.org/10.1017/CBO9780511486838.005",
        "Academic Book Chapter",
        "High"
    ),

    (
        3,
        "John J. Lowe provides a detailed scholarly analysis of how Panini's Ashtadhyayi works, including its structure, rules, morphology and syntax.",
        "John J. Lowe",
        "Modern Linguistics in Ancient India – The Aṣṭādhyāyī at Work",
        "Cambridge University Press",
        2024,
        "https://www.cambridge.org/core/books/abs/modern-linguistics-in-ancient-india/astadhyayi-at-work/986D88D54862FC7A68F641A6F7ACF387",
        "https://doi.org/10.1017/9781009364522.002",
        "Academic Book Chapter",
        "High"
    ),

    (
        4,
        "The Śulbasūtras are ancient Indian texts associated with altar construction and contain explicit mathematical and geometric procedures.",
        "S. G. Dani",
        "Ancient Indian Mathematics: Sulbasutras – A Mathematical Review",
        "Springer",
        2024,
        "https://doi.org/10.1007/978-3-031-40846-5_114",
        "https://doi.org/10.1007/978-3-031-40846-5_114",
        "Academic Reference Work",
        "High"
    ),

    (
        5,
        "The Caraka Samhita is a classical Sanskrit medical text associated with Ayurveda.",
        "Caraka; N. Srikanth, editor",
        "Charaka Samhita. Nidana Sthana: Critical Edition",
        "Central Council for Research in Ayurvedic Sciences, Ministry of Ayush",
        2021,
        "https://www.ncbi.nlm.nih.gov/nlmcatalog/272532",
        "https://www.ncbi.nlm.nih.gov/nlmcatalog/272532",
        "Library / Primary Text Catalog",
        "High"
    ),

    (
        6,
        "The Aryabhatiya is a surviving astronomical treatise containing mathematical material, including mathematical rules and astronomical calculations.",
        "Ian G. Pearce",
        "Indian Mathematics – The Classical Period: Aryabhata and his Commentators",
        "MacTutor History of Mathematics",
        None,
        "https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-10/",
        "https://mathshistory.st-andrews.ac.uk/Biographies/Aryabhata_I/",
        "Academic Historical Reference",
        "High"
    ),

    (
        16,
        "The Rigveda is a foundational collection of Vedic Sanskrit hymns and an important primary source for studying early Vedic religious and cultural traditions.",
        "Stephanie W. Jamison and Joel P. Brereton",
        "The Ancient Languages of Asia and the Americas – Sanskrit",
        "Cambridge University Press",
        2008,
        "https://www.cambridge.org/core/books/ancient-languages-of-asia-and-the-americas/sanskrit/CF7D5B91F9736880C0CECAC672754AEB",
        "https://doi.org/10.1017/CBO9780511486838.005",
        "Academic Book Chapter",
        "High"
    )

]

for record in records:

    (
        evidence_id,
        reference_text,
        author,
        work,
        publisher,
        year,
        scholarly_url,
        source_url,
        source_type,
        reliability
    ) = record

    cur.execute("""
        INSERT INTO references_data (
            evidence_id,
            reference_text,
            citation_author,
            citation_work,
            citation_publisher,
            citation_year,
            scholarly_reference,
            scholarly_url,
            source_url,
            scholarly_source_url,
            scholarly_source_type,
            source_reliability,
            citation_verified
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        evidence_id,
        reference_text,
        author,
        work,
        publisher,
        year,
        work,
        scholarly_url,
        source_url,
        scholarly_url,
        source_type,
        reliability,
        "Yes"
    ))

conn.commit()

print("=" * 70)
print("MISSING URL REFERENCES ADDED")
print("=" * 70)

for evidence_id, *_ in records:
    cur.execute("""
        SELECT reference_id, evidence_id, scholarly_url, citation_verified
        FROM references_data
        WHERE evidence_id = ?
        ORDER BY reference_id DESC
        LIMIT 1
    """, (evidence_id,))

    print(cur.fetchone())

print("=" * 70)
print("Records added:", len(records))
print("=" * 70)

conn.close()