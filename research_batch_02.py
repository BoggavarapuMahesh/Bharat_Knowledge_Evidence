import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

records = [
    {
        "title": "Katha Upanishad",
        "field": "Yoga",
        "topic": "Yoga and control of the senses",
        "claim": "Katha Upanishad 6.10–11 describes the stilling of the senses and mind and explicitly identifies this state as Yoga.",
        "period": "Early Upanishadic tradition",
        "evidence_type": "Primary Text",
        "reference": "Katha Upanishad 6.10–11",
        "scholarly": "Principal Upanishads textual translations",
        "url": "https://forage.com/upanishads/principal-upanishads/katha/",
        "status": "Primary passage identified",
        "notes": "Translation wording varies between editions. Preserve the Sanskrit and identify the translation used."
    },

    {
        "title": "Shvetashvatara Upanishad",
        "field": "Yoga",
        "topic": "Posture and sense withdrawal",
        "claim": "Shvetashvatara Upanishad 2.8 describes holding the body erect and directing the senses inward with the mind.",
        "period": "Later Vedic/early classical Upanishadic tradition",
        "evidence_type": "Primary Text",
        "reference": "Shvetashvatara Upanishad 2.8",
        "scholarly": "Textual translations and commentary",
        "url": "https://upasanayoga.org/SvetU.htm",
        "status": "Primary passage identified",
        "notes": "This is textual evidence for a form of yogic practice; it should not be equated automatically with later Hatha Yoga postures."
    },

    {
        "title": "Shvetashvatara Upanishad",
        "field": "Yoga",
        "topic": "Breath regulation",
        "claim": "Shvetashvatara Upanishad 2.9 describes regulation of the breath and restraint of the mind.",
        "period": "Later Vedic/early classical Upanishadic tradition",
        "evidence_type": "Primary Text",
        "reference": "Shvetashvatara Upanishad 2.9",
        "scholarly": "Textual translations and commentary",
        "url": "https://upasanayoga.org/SvetU.htm",
        "status": "Primary passage identified",
        "notes": "Translation terminology for prana and breath control differs among editions."
    },

    {
        "title": "Shvetashvatara Upanishad",
        "field": "Yoga",
        "topic": "Practice environment",
        "claim": "Shvetashvatara Upanishad 2.10 recommends a clean, level and protected place for Yoga practice.",
        "period": "Later Vedic/early classical Upanishadic tradition",
        "evidence_type": "Primary Text",
        "reference": "Shvetashvatara Upanishad 2.10",
        "scholarly": "Textual translations",
        "url": "https://texts.wara.in/upanishads/shvetashvatara/",
        "status": "Primary passage identified",
        "notes": "Record as a textual description of practice conditions, not as a modern medical recommendation."
    },

    {
        "title": "Shvetashvatara Upanishad",
        "field": "Yoga",
        "topic": "Yoga and self-knowledge",
        "claim": "Shvetashvatara Upanishad 2.15 connects yogic realization with knowledge of Brahman and freedom from bondage.",
        "period": "Later Vedic/early classical Upanishadic tradition",
        "evidence_type": "Primary Text",
        "reference": "Shvetashvatara Upanishad 2.15",
        "scholarly": "Textual translations",
        "url": "https://upasanayoga.org/SvetU.htm",
        "status": "Primary passage identified",
        "notes": "This is a philosophical/religious claim made by the text and should be represented as such."
    },

    {
        "title": "Maitri Upanishad",
        "field": "Yoga",
        "topic": "Six-limbed Yoga",
        "claim": "Maitri Upanishad 6.18 presents Yoga as six-limbed: pranayama, pratyahara, dhyana, dharana, tarka and samadhi.",
        "period": "Later Upanishadic tradition",
        "evidence_type": "Primary Text",
        "reference": "Maitri Upanishad 6.18",
        "scholarly": "Maitri Upanishad textual tradition",
        "url": "https://darshya.online/upanishads/maitri-upanishad",
        "status": "Primary passage identified",
        "notes": "This six-limbed list differs from the eight-limbed structure associated with Patanjali."
    },

    {
        "title": "Sushruta Samhita",
        "field": "Medicine",
        "topic": "Anatomy and dissection",
        "claim": "The Sushruta Samhita contains a passage describing the preparation and dissection of a cadaver as part of anatomical study.",
        "period": "Classical Indian medical tradition",
        "evidence_type": "Primary Text",
        "reference": "Sushruta Samhita, Sharira Sthana, Chapter 5",
        "scholarly": "Kenneth G. Zysk, Some Observations on the Dissection of Cadavers in Ancient India",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3336764/",
        "status": "Primary passage discussed in scholarly article",
        "notes": "The scholarly article specifically identifies the fifth chapter of the third book as containing the relevant anatomical passage."
    },

    {
        "title": "Sushruta Samhita",
        "field": "Medicine",
        "topic": "Surgical procedures",
        "claim": "Sushruta Samhita Chapter 25 describes several categories of surgical operations, including incision, excision, scarification and puncturing/aspiration.",
        "period": "Classical Indian medical tradition",
        "evidence_type": "Primary Text",
        "reference": "Sushruta Samhita, Volume 1, Chapter 25",
        "scholarly": "English translation of Sushruta Samhita",
        "url": "https://en.wikisource.org/wiki/Sushruta_Samhita,_Volume_1/Chapter_25",
        "status": "Textual passage identified",
        "notes": "Historical description only; terminology should be mapped carefully rather than assumed to correspond exactly to modern surgical terminology."
    },

    {
        "title": "Sushruta Samhita",
        "field": "Medicine",
        "topic": "Ear and related diseases",
        "claim": "Historical scholarship identifies detailed descriptions and treatments of otorhinological conditions within the Sushruta Samhita.",
        "period": "Classical Indian medical tradition",
        "evidence_type": "Scholarly Research",
        "reference": "Pothula, Jones and Lesser, Otology in ancient India",
        "scholarly": "Journal of Laryngology & Otology, 2001",
        "url": "https://pubmed.ncbi.nlm.nih.gov/11244521/",
        "status": "Peer-reviewed historical article identified",
        "notes": "This record documents what modern historical scholarship reports about the text; it does not establish modern clinical effectiveness."
    },

    {
        "title": "Shvetashvatara Upanishad",
        "field": "Yoga",
        "topic": "Reported effects of Yoga",
        "claim": "Shvetashvatara Upanishad 2.13 lists lightness, health, clear complexion, pleasant voice and related conditions as precursors of Yoga perfection.",
        "period": "Later Vedic/early classical Upanishadic tradition",
        "evidence_type": "Primary Text",
        "reference": "Shvetashvatara Upanishad 2.13",
        "scholarly": "Textual translations",
        "url": "https://vivekavani.com/svuh/",
        "status": "Primary passage identified",
        "notes": "These are claims made by the ancient text; they should not be represented as modern clinical findings."
    }
]

for r in records:

    cursor.execute("""
        INSERT INTO sources
        (title, source_type, author, date_period, language, url, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        r["title"],
        r["evidence_type"],
        "",
        r["period"],
        "Sanskrit",
        r["url"],
        r["notes"]
    ))

    source_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO evidence
        (source_id, topic, claim, evidence_type,
         historical_period, location, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        source_id,
        r["topic"],
        r["claim"],
        r["evidence_type"],
        r["period"],
        "Indian subcontinent",
        r["notes"]
    ))

    evidence_id = cursor.lastrowid

    cursor.execute("""
        INSERT OR IGNORE INTO fields
        (field_name, description)
        VALUES (?, ?)
    """, (
        r["field"],
        "Research field"
    ))

    field_id = cursor.execute("""
        SELECT field_id FROM fields WHERE field_name = ?
    """, (r["field"],)).fetchone()[0]

    cursor.execute("""
        INSERT OR IGNORE INTO evidence_fields
        (evidence_id, field_id)
        VALUES (?, ?)
    """, (evidence_id, field_id))

    cursor.execute("""
        INSERT INTO references_data
        (evidence_id, citation_work,
         citation_chapter, citation_verse,
         scholarly_reference, scholarly_url,
         verification_status, verification_notes,
         source_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        evidence_id,
        r["title"],
        r["reference"],
        "",
        r["scholarly"],
        r["url"],
        r["status"],
        r["notes"],
        r["url"]
    ))

    cursor.execute("""
        INSERT INTO evidence_quality
        (evidence_id, source_quality,
         citation_quality, verification_status,
         confidence_notes)
        VALUES (?, ?, ?, ?, ?)
    """, (
        evidence_id,
        "Primary text or scholarly historical source",
        "Passage identified",
        r["status"],
        r["notes"]
    ))

conn.commit()

print("Research Batch 02 added successfully.")
print("New evidence records:", len(records))
print("Total sources:", cursor.execute(
    "SELECT COUNT(*) FROM sources"
).fetchone()[0])
print("Total evidence:", cursor.execute(
    "SELECT COUNT(*) FROM evidence"
).fetchone()[0])

conn.close()