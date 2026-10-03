import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

records = [
    {
        "title": "Rigveda",
        "source_type": "Primary Text",
        "language": "Vedic Sanskrit",
        "period": "Vedic period",
        "topic": "Vedic Literature",
        "claim": "The Rigveda is one of the oldest surviving collections of Vedic Sanskrit hymns.",
        "evidence_type": "Primary Text",
        "field": "Literature",
        "status": "Needs exact citation verification"
    },
    {
        "title": "Panini's Ashtadhyayi",
        "source_type": "Primary Text",
        "language": "Sanskrit",
        "period": "Ancient India",
        "topic": "Grammar",
        "claim": "The Ashtadhyayi presents a systematic grammatical description of Sanskrit.",
        "evidence_type": "Primary Text",
        "field": "Grammar",
        "status": "Needs edition and sutra verification"
    },
    {
        "title": "Sulba Sutras",
        "source_type": "Primary Text",
        "language": "Sanskrit",
        "period": "Ancient India",
        "topic": "Geometry",
        "claim": "The Sulba Sutra tradition contains geometric procedures associated with the construction of ritual altars.",
        "evidence_type": "Primary Text",
        "field": "Mathematics",
        "status": "Needs exact text and scholarly citation verification"
    },
    {
        "title": "Charaka Samhita",
        "source_type": "Primary Text",
        "language": "Sanskrit",
        "period": "Ancient India",
        "topic": "Medicine",
        "claim": "The Charaka Samhita is an important classical Sanskrit text associated with Ayurveda and medical theory.",
        "evidence_type": "Primary Text",
        "field": "Medicine",
        "status": "Needs edition and passage verification"
    },
    {
        "title": "Aryabhatiya",
        "source_type": "Primary Text",
        "language": "Sanskrit",
        "period": "Classical India",
        "topic": "Astronomy and Mathematics",
        "claim": "Aryabhata's Aryabhatiya contains mathematical and astronomical material.",
        "evidence_type": "Primary Text",
        "field": "Astronomy",
        "status": "Needs exact verse and scholarly citation verification"
    }
]

for r in records:

    cursor.execute("""
        INSERT INTO sources
        (title, source_type, author, date_period, language, url, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        r["title"],
        r["source_type"],
        "",
        r["period"],
        r["language"],
        "",
        "Record entered for structured research; exact citation requires verification."
    ))

    source_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO evidence
        (source_id, topic, claim, evidence_type, historical_period, location, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        source_id,
        r["topic"],
        r["claim"],
        r["evidence_type"],
        r["period"],
        "Indian subcontinent",
        "Structured research record."
    ))

    evidence_id = cursor.lastrowid

    cursor.execute("""
        INSERT OR IGNORE INTO fields (field_name, description)
        VALUES (?, ?)
    """, (r["field"], "Research field"))

    field_id = cursor.execute(
        "SELECT field_id FROM fields WHERE field_name = ?",
        (r["field"],)
    ).fetchone()[0]

    cursor.execute("""
        INSERT OR IGNORE INTO evidence_fields
        (evidence_id, field_id)
        VALUES (?, ?)
    """, (evidence_id, field_id))

    cursor.execute("""
        INSERT INTO evidence_quality
        (evidence_id, source_quality, citation_quality,
         verification_status, confidence_notes)
        VALUES (?, ?, ?, ?, ?)
    """, (
        evidence_id,
        "Primary-source category",
        "Not yet fully cited",
        r["status"],
        "Do not treat the claim as independently verified until the exact source passage and reliable scholarly references are added."
    ))

conn.commit()

print("Initial evidence records added.")
print("Total sources:", cursor.execute(
    "SELECT COUNT(*) FROM sources"
).fetchone()[0])

print("Total evidence:", cursor.execute(
    "SELECT COUNT(*) FROM evidence"
).fetchone()[0])

conn.close()