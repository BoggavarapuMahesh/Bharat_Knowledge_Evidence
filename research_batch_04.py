import sqlite3

DB = "bharat_knowledge.db"

records = [
    {
        "title": "Brahmagupta and rules for zero",
        "source_type": "Scholarly Research",
        "author": "Carl B. Boyer / MacTutor historical account",
        "period": "7th century CE",
        "language": "Sanskrit",
        "topic": "Mathematics",
        "claim": "Brahmagupta gave explicit arithmetic rules involving zero, including operations with positive and negative numbers.",
        "description": "Brahmagupta's Brahmasphutasiddhanta contains systematic rules concerning zero and signed numbers.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "verification": "Scholarly source verified; historical interpretation should distinguish Brahmagupta's text from later developments."
    },
    {
        "title": "Brahmagupta and indeterminate equations",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "7th century CE",
        "language": "Sanskrit",
        "topic": "Mathematics",
        "claim": "Brahmagupta developed methods for solving certain quadratic and indeterminate equations.",
        "description": "Historical accounts of the Brahmasphutasiddhanta describe Brahmagupta's treatment of algebraic and indeterminate problems.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Brahmagupta and cyclic quadrilaterals",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "7th century CE",
        "language": "Sanskrit",
        "topic": "Geometry",
        "claim": "Brahmagupta gave a rule for calculating the area of a cyclic quadrilateral.",
        "description": "The Brahmasphutasiddhanta contains a geometric rule associated with cyclic quadrilaterals.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Brahmagupta and sums of squares and cubes",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "7th century CE",
        "language": "Sanskrit",
        "topic": "Mathematics",
        "claim": "Brahmagupta studied formulas involving sums of squares and cubes.",
        "description": "Historical accounts of Brahmagupta's mathematical work include results concerning sums of powers.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Brahmagupta and mathematical astronomy",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "7th century CE",
        "language": "Sanskrit",
        "topic": "Astronomy",
        "claim": "Brahmagupta's astronomical work addressed planetary positions, eclipses and conjunctions.",
        "description": "The Brahmasphutasiddhanta combines mathematical methods with astronomical calculations.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Bhaskara II and algebra",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "12th century CE",
        "language": "Sanskrit",
        "topic": "Mathematics",
        "claim": "Bhaskara II developed and presented methods for solving algebraic problems involving unknown quantities.",
        "description": "Bhaskara II's mathematical works contain extensive treatment of algebra and equations.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Bhaskara II and mathematical astronomy",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "12th century CE",
        "language": "Sanskrit",
        "topic": "Astronomy",
        "claim": "Bhaskara II's Siddhantasiromani included substantial mathematical astronomy.",
        "description": "The work addressed astronomical calculations using mathematical methods.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Bhaskara II and zero",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "12th century CE",
        "language": "Sanskrit",
        "topic": "Mathematics",
        "claim": "Bhaskara II continued mathematical work involving zero, negative numbers and equations.",
        "description": "His mathematical writings developed earlier Indian traditions concerning arithmetic and algebra.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "verification": "Scholarly source verified; later mathematical developments should not be attributed solely to one author."
    },
    {
        "title": "Indian decimal place-value mathematics",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "Ancient and early medieval India",
        "language": "Sanskrit",
        "topic": "Mathematics",
        "claim": "Indian mathematical traditions developed and used a decimal place-value system that became historically important in the transmission of modern numerals.",
        "description": "Historical research traces the development of decimal place-value notation in India and its later transmission beyond India.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_numerals/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_numerals/",
        "verification": "Scholarly source verified; transmission involved multiple historical stages."
    },
    {
        "title": "Indian development of zero as a number",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "Early medieval India",
        "language": "Sanskrit",
        "topic": "Mathematics",
        "claim": "Indian mathematical sources provide early evidence for treating zero as a number in arithmetic.",
        "description": "Historical accounts identify Indian mathematics as an important stage in the development of zero as a numerical concept.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Zero/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Zero/",
        "verification": "Scholarly source verified; dating and transmission should be treated carefully."
    },
    {
        "title": "Ancient Indian physicians and medical practice",
        "source_type": "Scholarly Research",
        "author": "Indian medical history research",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Medicine",
        "claim": "Historical research identifies organized traditions of physicians and medical practice in ancient India.",
        "description": "Studies of ancient Indian medicine describe physicians, medical texts, training and therapeutic practice.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Medical education in ancient India",
        "source_type": "Scholarly Research",
        "author": "Historical research on ancient Indian medicine",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Education",
        "claim": "Historical sources describe training and education of physicians in ancient Indian medical traditions.",
        "description": "Medical-history scholarship discusses physician education and the transmission of medical knowledge.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "verification": "Scholarly source verified; details vary across periods and traditions."
    },
    {
        "title": "Charaka and Sushruta medical traditions",
        "source_type": "Scholarly Research",
        "author": "Historical research on Ayurveda",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Medicine",
        "claim": "Charaka Samhita and Sushruta Samhita are major textual sources in the history of classical Indian medicine.",
        "description": "Modern historical scholarship treats these works as major sources for studying classical Indian medical traditions.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3336651/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3336651/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Sushruta and anatomical study",
        "source_type": "Scholarly Research",
        "author": "Historical anatomy research",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Anatomy",
        "claim": "The Sushruta Samhita contains descriptions relevant to anatomical study and surgical practice.",
        "description": "Historical research examines anatomical knowledge described in the Sushruta Samhita.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3039177/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3039177/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Sushruta and surgical instruments",
        "source_type": "Scholarly Research",
        "author": "Historical research on Sushruta",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Surgery",
        "claim": "The Sushruta tradition describes surgical instruments and operative techniques.",
        "description": "Historical studies identify descriptions of instruments and surgical procedures in the Sushruta Samhita.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11527508/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11527508/",
        "verification": "Scholarly source verified; modern terminology should not be projected uncritically onto ancient practice."
    },
    {
        "title": "Sushruta and reconstructive nasal surgery",
        "source_type": "Scholarly Research",
        "author": "Historical research on Sushruta",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Surgery",
        "claim": "Historical scholarship associates the Sushruta tradition with reconstructive procedures involving the nose.",
        "description": "Studies of Indian surgical history discuss nasal reconstruction within the Sushruta tradition.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5512402/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5512402/",
        "verification": "Scholarly source verified; historical attribution and later transmission require qualification."
    },
    {
        "title": "Sushruta and cataract surgery",
        "source_type": "Scholarly Research",
        "author": "Historical research on ancient Indian surgery",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Surgery",
        "claim": "Historical literature on Sushruta discusses procedures associated with treatment of cataract.",
        "description": "Historical scholarship examines descriptions of ocular procedures attributed to the Sushruta tradition.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11000756/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11000756/",
        "verification": "Scholarly source verified; ancient procedures should not be equated directly with modern ophthalmic surgery."
    },
    {
        "title": "Physicians and surgeons as distinct medical roles",
        "source_type": "Scholarly Research",
        "author": "Historical research on ancient Indian medicine",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Medicine",
        "claim": "Historical scholarship discusses differentiated roles for physicians and surgeons within ancient Indian medical traditions.",
        "description": "Research on ancient Indian medicine examines the professional organization and specialization of medical practitioners.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3336666/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3336666/",
        "verification": "Scholarly source verified; terminology is a modern analytical description."
    },
    {
        "title": "Historical evidence of urban sanitation",
        "source_type": "Scholarly Research",
        "author": "Public-health historical research",
        "period": "Ancient South Asia",
        "language": "Multiple",
        "topic": "Public Health",
        "claim": "Historical research identifies planned urban infrastructure and sanitation features in parts of ancient South Asia.",
        "description": "Historical public-health scholarship discusses infrastructure such as streets, drainage and water-management systems in ancient urban settlements.",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7170188/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7170188/",
        "verification": "Scholarly source verified; evidence applies to particular archaeological contexts rather than all ancient Indian settlements."
    }
]

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
            citation_year,
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        evidence_id,
        item["title"],
        item["source_url"],
        item["author"],
        item["title"],
        None,
        item["source_url"],
        item["author"],
        item["scholarly_url"],
        "Scholarly source verified",
        item["verification"],
        item["scholarly_url"],
        "Scholarly secondary source",
        "High",
        "Scholarly source verified; primary-text/edition verification may still be required"
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
        "Scholarly source verified",
        item["verification"]
    ))

    added += 1

conn.commit()

cur.execute("SELECT COUNT(*) FROM evidence")
total_evidence = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM references_data")
total_refs = cur.fetchone()[0]

conn.close()

print("Research Batch 04 added successfully.")
print("Records added:", added)
print("Total evidence records:", total_evidence)
print("Total reference records:", total_refs)