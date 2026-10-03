import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

records = [

    {
        "title": "Baudhayana Sulbasutra",
        "field": "Mathematics",
        "topic": "Geometry",
        "claim": "The Baudhayana Sulbasutra contains geometric construction rules used in the construction of ritual altars, including a statement corresponding to a special case of the Pythagorean theorem.",
        "period": "Approximately 800 BCE according to the cited history-of-mathematics source",
        "evidence_type": "Primary Text",
        "reference": "Baudhayana Sulbasutra; exact sutra/section requires edition-specific verification.",
        "scholarly": "MacTutor History of Mathematics, Indian Sulbasutras",
        "url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_sulbasutras/",
        "status": "Scholarly secondary source verified; exact primary citation pending",
        "notes": "The source explicitly notes that the Sulbasutras contain construction procedures but generally do not provide formal proofs."
    },

    {
        "title": "Indian Decimal Place-Value System",
        "field": "Mathematics",
        "topic": "Numeral Systems",
        "claim": "Historical evidence indicates the use of a decimal positional number system in India by the end of the sixth century CE.",
        "period": "By the 6th century CE",
        "evidence_type": "Historical Record",
        "reference": "Dated document from 594 CE discussed in the cited historical analysis.",
        "scholarly": "MacTutor History of Mathematics, Indian Numerals",
        "url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_numerals/",
        "status": "Secondary historical evidence verified; interpretation of early development remains debated",
        "notes": "Do not state that India was necessarily the first civilization to use positional notation; Babylonian base-60 positional notation predates Indian decimal positional notation."
    },

    {
        "title": "Aryabhatiya",
        "field": "Astronomy",
        "topic": "Astronomy and Mathematics",
        "claim": "Aryabhata's Aryabhatiya contains mathematical and astronomical material and was completed in 499 CE.",
        "period": "499 CE",
        "evidence_type": "Primary Text",
        "reference": "Aryabhatiya; completion date derived from Aryabhata's statement about his age.",
        "scholarly": "MacTutor History of Mathematics, Aryabhata",
        "url": "https://mathshistory.st-andrews.ac.uk/Biographies/Aryabhata_I/",
        "status": "Scholarly source verified",
        "notes": "The birthplace traditionally identified as Kusumapura is not completely certain according to the cited source."
    },

    {
        "title": "Panini's Ashtadhyayi",
        "field": "Grammar",
        "topic": "Sanskrit Grammar",
        "claim": "The Ashtadhyayi presents a highly systematic derivational grammar of Sanskrit.",
        "period": "Around the 4th century BCE according to the cited modern scholarly study",
        "evidence_type": "Primary Text",
        "reference": "Ashtadhyayi; exact sutra references should be added from a specified edition.",
        "scholarly": "Vincenzo Vergiani, The Introduction of Writing into Achaemenid Gandhara and the Origin of Panini's Grammar",
        "url": "https://journals.sagepub.com/doi/10.1177/09719458241226574",
        "status": "Scholarly source verified; exact primary citation pending",
        "notes": "Dating Panini is a scholarly question; this record uses the date argued in the cited 2024 study rather than treating it as universally settled."
    },

    {
        "title": "Charaka Samhita",
        "field": "Medicine",
        "topic": "Ayurveda",
        "claim": "The Charaka Samhita is a major Sanskrit medical text associated with the Ayurvedic tradition and survives in modern critical and scholarly editions.",
        "period": "Ancient/Classical India; precise dating requires scholarly qualification",
        "evidence_type": "Primary Text",
        "reference": "Charaka Samhita; edition-specific chapter and passage to be added.",
        "scholarly": "U.S. National Library of Medicine catalog records",
        "url": "https://www.ncbi.nlm.nih.gov/nlmcatalog/272532",
        "status": "Bibliographic source verified; exact primary citation pending",
        "notes": "The database should distinguish the existence and content of the text from claims about modern medical effectiveness."
    },

    {
        "title": "Sushruta Samhita",
        "field": "Medicine",
        "topic": "Surgery",
        "claim": "The Sushruta Samhita contains descriptions of surgical procedures, instruments, anatomy and medical treatment.",
        "period": "Ancient India; precise dating disputed",
        "evidence_type": "Primary Text",
        "reference": "Sushruta Samhita; exact section/page requires edition-specific verification.",
        "scholarly": "PubMed historical reviews of Sushruta and the Sushruta Samhita",
        "url": "https://pubmed.ncbi.nlm.nih.gov/23788147/",
        "status": "Scholarly historical source verified; dating and exact primary citation require further verification",
        "notes": "Published historical reviews give different dates for Sushruta; this record deliberately does not force one date as certain."
    },

    {
        "title": "Upanishadic Philosophy",
        "field": "Philosophy",
        "topic": "Atman, Brahman and Liberation",
        "claim": "The Upanishads are important primary texts for the development of classical Indian philosophical traditions and were directly used by later Indian philosophers.",
        "period": "Late Vedic and early classical periods; individual Upanishads have different dates",
        "evidence_type": "Primary Text",
        "reference": "Individual Upanishad required for exact passage; Maitri Upanishad 6-7 is discussed in relation to Yoga.",
        "scholarly": "Internet Encyclopedia of Philosophy, Upanisads",
        "url": "https://iep.utm.edu/upanisad/",
        "status": "Scholarly source verified",
        "notes": "The Upanishads are not a single text written at one time; records should identify the individual Upanishad whenever possible."
    },

    {
        "title": "Yoga Sutras of Patanjali",
        "field": "Yoga",
        "topic": "Classical Yoga",
        "claim": "The Yoga Sutras systematize an established body of Yoga practices and philosophy; Patañjali's first sutra presents the teaching as a continuation.",
        "period": "Classical Indian period; precise dating requires scholarly qualification",
        "evidence_type": "Primary Text",
        "reference": "Yoga Sutra I.1 and I.2; edition-specific Sanskrit citation to be added.",
        "scholarly": "Internet Encyclopedia of Philosophy, The Yoga Sutras of Patanjali",
        "url": "https://iep.utm.edu/yoga/",
        "status": "Primary passage identified; edition-specific citation pending",
        "notes": "The source explicitly distinguishes Patañjali's systematization from the much older history of Yoga practices."
    },

    {
        "title": "Yoga Sutra I.2",
        "field": "Yoga",
        "topic": "Definition of Yoga",
        "claim": "Yoga Sutra I.2 defines Yoga through the restraint/stilling of the modifications of the mind.",
        "period": "Classical Indian period",
        "evidence_type": "Primary Text",
        "reference": "Yoga Sutra I.2",
        "scholarly": "Internet Encyclopedia of Philosophy, The Yoga Sutras of Patanjali",
        "url": "https://iep.utm.edu/yoga/",
        "status": "Primary reference identified and secondary interpretation verified",
        "notes": "Translation wording varies by edition and translator; the final dataset should preserve the chosen translation and translator."
    },

    {
        "title": "Rigvedic Literature",
        "field": "Literature",
        "topic": "Vedic Literature",
        "claim": "The Rigveda is a foundational collection of Vedic Sanskrit hymns and an important primary source for studying early Vedic religious and cultural traditions.",
        "period": "Vedic period; precise dating is a scholarly question",
        "evidence_type": "Primary Text",
        "reference": "Individual mandala, sukta and verse should be specified for each future claim.",
        "scholarly": "Primary-text research record",
        "url": "",
        "status": "Primary source category verified; individual claim citations required",
        "notes": "This is a source-level record, not evidence that every historical claim made about the Rigveda is automatically established."
    }

]

for r in records:

    # Create source
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

    # Create evidence
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

    # Field
    cursor.execute("""
        INSERT OR IGNORE INTO fields
        (field_name, description)
        VALUES (?, ?)
    """, (
        r["field"],
        "Research field"
    ))

    field_id = cursor.execute("""
        SELECT field_id
        FROM fields
        WHERE field_name = ?
    """, (r["field"],)).fetchone()[0]

    cursor.execute("""
        INSERT OR IGNORE INTO evidence_fields
        (evidence_id, field_id)
        VALUES (?, ?)
    """, (
        evidence_id,
        field_id
    ))

    # Detailed citation
    cursor.execute("""
        INSERT INTO references_data
        (evidence_id,
         citation_work,
         citation_page,
         citation_chapter,
         citation_verse,
         scholarly_reference,
         scholarly_url,
         verification_status,
         verification_notes,
         source_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        evidence_id,
        r["title"],
        "",
        "",
        "",
        r["scholarly"],
        r["url"],
        r["status"],
        r["notes"],
        r["url"]
    ))

    # Quality record
    cursor.execute("""
        INSERT INTO evidence_quality
        (evidence_id,
         source_quality,
         citation_quality,
         verification_status,
         confidence_notes)
        VALUES (?, ?, ?, ?, ?)
    """, (
        evidence_id,
        "Primary or authoritative bibliographic source",
        "Partially verified",
        r["status"],
        r["notes"]
    ))

conn.commit()

print("Research Batch 01 added successfully.")
print("New evidence records:", len(records))
print("Total sources:", cursor.execute(
    "SELECT COUNT(*) FROM sources"
).fetchone()[0])
print("Total evidence:", cursor.execute(
    "SELECT COUNT(*) FROM evidence"
).fetchone()[0])

conn.close()