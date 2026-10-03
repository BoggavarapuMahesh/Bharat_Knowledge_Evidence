import sqlite3

DB = "bharat_knowledge.db"

records = [
    {
        "title": "Madhava and infinite series",
        "source_type": "Scholarly Research",
        "author": "Ian G. Pearce / MacTutor",
        "period": "14th–15th century CE",
        "language": "Malayalam / Sanskrit mathematical tradition",
        "topic": "Mathematics",
        "claim": "Historical scholarship attributes important infinite-series results to Madhava of Sangamagrama and the Kerala school.",
        "description": "The Kerala mathematical tradition is described as developing series associated with trigonometric functions and limiting processes.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-18/",
        "verification": "Scholarly historical source verified; attribution of surviving results relies substantially on later Kerala sources because Madhava's own mathematical works are not extant."
    },
    {
        "title": "Madhava and sine series",
        "source_type": "Scholarly Research",
        "author": "Ian G. Pearce / MacTutor",
        "period": "14th–15th century CE",
        "language": "Malayalam / Sanskrit mathematical tradition",
        "topic": "Mathematics",
        "claim": "Historical accounts associate Madhava with series expansions related to the sine function.",
        "description": "Later Kerala mathematical texts preserve results attributed to Madhava concerning trigonometric series.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-18/",
        "verification": "Scholarly historical source verified; surviving evidence is largely through later authors."
    },
    {
        "title": "Madhava and cosine series",
        "source_type": "Scholarly Research",
        "author": "Ian G. Pearce / MacTutor",
        "period": "14th–15th century CE",
        "language": "Malayalam / Sanskrit mathematical tradition",
        "topic": "Mathematics",
        "claim": "Historical scholarship associates Madhava with series expansions related to the cosine function.",
        "description": "The Kerala school preserved mathematical results involving trigonometric series.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-18/",
        "verification": "Scholarly historical source verified; later textual transmission must be considered."
    },
    {
        "title": "Madhava and approximation of pi",
        "source_type": "Scholarly Research",
        "author": "Ian G. Pearce / MacTutor",
        "period": "14th–15th century CE",
        "language": "Malayalam / Sanskrit mathematical tradition",
        "topic": "Mathematics",
        "claim": "The Kerala mathematical tradition contains methods associated with Madhava for calculating pi using series.",
        "description": "Historical accounts describe series-based methods in the Kerala school that yield increasingly accurate values of pi.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-18/",
        "verification": "Scholarly historical source verified; exact attribution should be tied to the later texts preserving the result."
    },
    {
        "title": "Jyesthadeva's Yuktibhasa",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "16th century CE",
        "language": "Malayalam",
        "topic": "Mathematics",
        "claim": "Jyesthadeva's Yuktibhasa presents mathematical and astronomical material from the Kerala school and includes proofs and derivations.",
        "description": "MacTutor describes Yuktibhasa as an important mathematical and astronomical text of the Kerala school.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Jyesthadeva/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Yuktibhasa and mathematical proofs",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "16th century CE",
        "language": "Malayalam",
        "topic": "Logic",
        "claim": "Yuktibhasa is notable for presenting proofs and derivations of mathematical rules.",
        "description": "The text differs from many earlier Indian mathematical works in the extent to which it provides explicit derivations.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Jyesthadeva/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Kerala school mathematical astronomy",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "14th–16th century CE",
        "language": "Malayalam / Sanskrit",
        "topic": "Astronomy",
        "claim": "The Kerala school developed a sustained mathematical and astronomical tradition involving figures such as Madhava, Nilakantha and Jyesthadeva.",
        "description": "Historical scholarship describes the Kerala school as an important centre of mathematical astronomy.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Jyesthadeva/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Nilakantha Somayaji and astronomical models",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "15th–16th century CE",
        "language": "Sanskrit",
        "topic": "Astronomy",
        "claim": "Nilakantha Somayaji developed astronomical models within the Kerala mathematical tradition.",
        "description": "Historical accounts of the Kerala school discuss Nilakantha's astronomical work and his interaction with earlier Indian astronomy.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Nilakantha/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Kerala school and trigonometric computation",
        "source_type": "Scholarly Research",
        "author": "Ian G. Pearce / MacTutor",
        "period": "14th–16th century CE",
        "language": "Malayalam / Sanskrit",
        "topic": "Mathematics",
        "claim": "Kerala mathematicians developed computational techniques involving trigonometric quantities.",
        "description": "The Kerala tradition combined mathematical calculation with astronomical applications.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-18/",
        "verification": "Scholarly historical source verified."
    },
    {
        "title": "Indian astronomy and knowledge exchange along the Silk Roads",
        "source_type": "Scholarly / Institutional Research",
        "author": "UNESCO",
        "period": "Ancient and early medieval period",
        "language": "Multiple",
        "topic": "Astronomy",
        "claim": "UNESCO documents the influence of Indian astronomy within wider knowledge exchanges along the Silk Roads.",
        "description": "UNESCO describes Indian astronomical influence in Iran and the production of Arabic translations of Indian astronomical manuals.",
        "source_url": "https://www.unesco.org/en/articles/evolution-astronomy-along-silk-roads",
        "verification": "UNESCO source verified; transmission occurred through multiple cultures and stages."
    },
    {
        "title": "Translation of Indian astronomical manuals into Arabic",
        "source_type": "Scholarly / Institutional Research",
        "author": "UNESCO",
        "period": "8th century CE",
        "language": "Sanskrit and Arabic",
        "topic": "Astronomy",
        "claim": "UNESCO reports that Indian astronomical manuals were translated into Arabic during the scientific activity centred on Baghdad.",
        "description": "The translations formed part of broader exchanges of astronomical knowledge between India and the Islamic world.",
        "source_url": "https://www.unesco.org/en/articles/evolution-astronomy-along-silk-roads",
        "verification": "UNESCO source verified."
    },
    {
        "title": "Ancient Indian medical education and apprenticeship",
        "source_type": "Scholarly Research",
        "author": "Indian medical history researchers",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Education",
        "claim": "Historical scholarship describes structured medical training, including teacher-led instruction and practical apprenticeship.",
        "description": "Studies describe medical education in ashramas and practical learning under experienced practitioners.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Ancient Indian surgical training",
        "source_type": "Scholarly Research",
        "author": "Indian medical history researchers",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Surgery",
        "claim": "Historical scholarship reports that Sushruta's tradition included practical training for surgical procedures using models and other practice materials.",
        "description": "The medical-history literature describes practical exercises intended to prepare students for surgical work.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "verification": "Scholarly source verified; descriptions reflect historical texts rather than modern surgical standards."
    },
    {
        "title": "Ancient Indian anatomical observation",
        "source_type": "Scholarly Research",
        "author": "Indian medical history researchers",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Anatomy",
        "claim": "Historical scholarship reports that Sushruta recommended observation of human bodies as part of anatomical learning.",
        "description": "Medical-history research connects anatomical observation with surgical education in the Sushruta tradition.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Ancient Indian physician competency framework",
        "source_type": "Scholarly Research",
        "author": "Historical medical education researchers",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Medicine",
        "claim": "Modern scholarship identifies a competency framework for physicians in ancient Indian medical literature involving knowledge, communication, professionalism and practical skills.",
        "description": "A modern review compares ancient Indian descriptions of physician competencies with contemporary competency frameworks.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10071902/",
        "verification": "Scholarly source verified; comparison with modern competency frameworks is a modern scholarly interpretation."
    },
    {
        "title": "Ancient Indian medical assessment and authorization",
        "source_type": "Scholarly Research",
        "author": "Historical medical education researchers",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Medicine",
        "claim": "Historical scholarship reports that ancient Indian medical training included assessment and authorization before independent practice.",
        "description": "The Sushruta tradition describes completion of study, practical experience, testing and permission before practice.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10071902/",
        "verification": "Scholarly source verified; the historical framework should not be equated directly with modern medical licensing."
    },
    {
        "title": "Nalanda as a major scholastic institution",
        "source_type": "Archaeological",
        "author": "UNESCO World Heritage Centre",
        "period": "5th–13th century CE",
        "language": "Multiple",
        "topic": "Education",
        "claim": "UNESCO identifies Nalanda Mahavihara as a major monastic and scholastic establishment with organized transmission of knowledge.",
        "description": "The archaeological remains document a large institutional complex with residential, educational and religious structures.",
        "source_url": "https://whc.unesco.org/en/list/1502/",
        "verification": "UNESCO source verified."
    },
    {
        "title": "Nalanda and institutional architecture",
        "source_type": "Archaeological",
        "author": "UNESCO World Heritage Centre",
        "period": "5th–13th century CE",
        "language": "Multiple",
        "topic": "Architecture",
        "claim": "Nalanda's archaeological remains demonstrate developed residential and educational architectural planning.",
        "description": "UNESCO identifies standardized vihara architecture and organized spatial planning at the site.",
        "source_url": "https://whc.unesco.org/en/list/1502/",
        "verification": "UNESCO source verified."
    },
    {
        "title": "Nalanda's influence on later monastic institutions",
        "source_type": "Archaeological",
        "author": "UNESCO World Heritage Centre",
        "period": "Early medieval South Asia",
        "language": "Multiple",
        "topic": "Education",
        "claim": "UNESCO states that Nalanda's systems of organization and architecture influenced later Mahaviharas in South Asia.",
        "description": "The World Heritage assessment identifies similarities between Nalanda and later institutions such as Vikramshila, Odantapuri and Jagaddala.",
        "source_url": "https://whc.unesco.org/en/list/1502/",
        "verification": "UNESCO source verified."
    },
    {
        "title": "Vedic oral transmission tradition",
        "source_type": "Institutional / Cultural Heritage",
        "author": "UNESCO",
        "period": "Ancient to present",
        "language": "Sanskrit",
        "topic": "Phonetics",
        "claim": "UNESCO recognizes Vedic chanting as an oral tradition involving systematic transmission of Vedic texts.",
        "description": "UNESCO's Intangible Cultural Heritage documentation describes the Vedic corpus and its long-standing oral transmission tradition.",
        "source_url": "https://ich.unesco.org/en/RL/tradition-of-vedic-chanting-00062",
        "verification": "UNESCO cultural-heritage source verified; heritage recognition does not independently establish the historical dating of every Vedic passage."
    }
]

# IMPORTANT: Batch 06 is intentionally fixed at exactly 20 records.
assert len(records) == 20, f"Expected 20 records, found {len(records)}"

conn = sqlite3.connect(DB)
cur = conn.cursor()

added = 0

for item in records:

    cur.execute("""
        INSERT INTO sources
        (title, source_type, author, date_period, language, url, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        item["title"],
        item["source_type"],
        item["author"],
        item["period"],
        item["language"],
        item["source_url"],
        item["description"]
    ))

    source_id = cur.lastrowid

    cur.execute("""
        INSERT INTO evidence
        (source_id, topic, claim, evidence_type, historical_period, location, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        source_id,
        item["topic"],
        item["claim"],
        item["source_type"],
        item["period"],
        "India / South Asia",
        item["description"]
    ))

    evidence_id = cur.lastrowid

    cur.execute("""
        INSERT INTO references_data
        (
            evidence_id,
            reference_text,
            url,
            citation_author,
            citation_work,
            source_url,
            scholarly_reference,
            scholarly_url,
            verification_status,
            verification_notes,
            scholarly_source_url,
            scholarly_source_type,
            source_reliability,
            citation_verified
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        evidence_id,
        item["title"],
        item["source_url"],
        item["author"],
        item["title"],
        item["source_url"],
        item["author"],
        item["source_url"],
        "Scholarly/institutional source verified",
        item["verification"],
        item["source_url"],
        item["source_type"],
        "High",
        "Source checked; primary-text verification may still be required"
    ))

    cur.execute("""
        INSERT INTO evidence_quality
        (
            evidence_id,
            source_quality,
            citation_quality,
            verification_status,
            confidence_notes
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        evidence_id,
        "High",
        "High",
        "Scholarly/institutional source verified",
        item["verification"]
    ))

    added += 1

conn.commit()

cur.execute("SELECT COUNT(*) FROM evidence")
total_evidence = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM references_data")
total_refs = cur.fetchone()[0]

conn.close()

print("Research Batch 06 added successfully.")
print("Records added:", added)
print("Total evidence records:", total_evidence)
print("Total reference records:", total_refs)