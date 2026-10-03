import sqlite3
from datetime import date

DB = "bharat_knowledge.db"

records = [
    {
        "topic": "Mathematics",
        "claim": "Brahmagupta gave rules for arithmetic involving zero and negative numbers in the Brahmasphutasiddhanta.",
        "type": "Primary Text",
        "period": "7th century CE",
        "location": "Bhinmal / Rajasthan region",
        "description": "Brahmagupta's mathematical work contains explicit rules concerning zero, positive and negative quantities. The historical significance is that these operations were incorporated into a systematic mathematical treatment.",
        "reference": "Brahmasphutasiddhanta; rules concerning zero and negative numbers",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "primary_type": "Primary mathematical text represented through scholarly translation/discussion",
        "scholarly_type": "Academic history of mathematics",
        "reliability": "High",
        "status": "Scholarly source verified; exact edition passage pending"
    },
    {
        "topic": "Mathematics",
        "claim": "Brahmagupta described methods for solving quadratic and indeterminate equations.",
        "type": "Primary Text",
        "period": "7th century CE",
        "location": "Bhinmal / Rajasthan region",
        "description": "The Brahmasphutasiddhanta contains procedures for equations including quadratic and indeterminate forms.",
        "reference": "Brahmasphutasiddhanta; algebraic rules",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "primary_type": "Primary mathematical text represented through scholarly translation/discussion",
        "scholarly_type": "Academic history of mathematics",
        "reliability": "High",
        "status": "Scholarly source verified; exact edition passage pending"
    },
    {
        "topic": "Mathematics",
        "claim": "Brahmagupta provided a rule for the area of a cyclic quadrilateral.",
        "type": "Primary Text",
        "period": "7th century CE",
        "location": "Bhinmal / Rajasthan region",
        "description": "Brahmagupta presented a formula for the area of a cyclic quadrilateral. Historical interpretation of the intended conditions has been discussed by historians.",
        "reference": "Brahmasphutasiddhanta; quadrilateral area rule",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "primary_type": "Primary mathematical text represented through scholarly discussion",
        "scholarly_type": "Academic history of mathematics",
        "reliability": "High",
        "status": "Scholarly source verified; interpretation qualification required"
    },
    {
        "topic": "Mathematics",
        "claim": "Brahmagupta gave rules for summing squares and cubes of the first n natural numbers.",
        "type": "Primary Text",
        "period": "7th century CE",
        "location": "Bhinmal / Rajasthan region",
        "description": "The Brahmasphutasiddhanta contains formulas for sums of squares and cubes.",
        "reference": "Brahmasphutasiddhanta; series formulas",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "primary_type": "Primary mathematical text represented through scholarly discussion",
        "scholarly_type": "Academic history of mathematics",
        "reliability": "High",
        "status": "Scholarly source verified; exact edition passage pending"
    },
    {
        "topic": "Astronomy and Mathematics",
        "claim": "Brahmagupta's Brahmasphutasiddhanta addressed planetary positions, eclipses, conjunctions and other mathematical-astronomical problems.",
        "type": "Primary Text",
        "period": "7th century CE",
        "location": "Bhinmal / Ujjain mathematical tradition",
        "description": "The work combines mathematical procedures with astronomical calculations including solar and lunar eclipses and planetary positions.",
        "reference": "Brahmasphutasiddhanta; astronomical chapters",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "primary_type": "Primary astronomical text represented through scholarly discussion",
        "scholarly_type": "Academic history of astronomy",
        "reliability": "High",
        "status": "Scholarly source verified"
    },
    {
        "topic": "Mathematics",
        "claim": "Bhaskara II extended earlier Indian mathematical work on zero, negative numbers and equations.",
        "type": "Primary Text",
        "period": "12th century CE",
        "location": "Ujjain / India",
        "description": "Bhaskara II's mathematical works continued and extended earlier developments in Indian mathematics.",
        "reference": "Lilavati and Bijaganita; mathematical rules",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "primary_type": "Primary mathematical texts represented through scholarly discussion",
        "scholarly_type": "Academic history of mathematics",
        "reliability": "High",
        "status": "Scholarly source verified"
    },
    {
        "topic": "Mathematics",
        "claim": "Bhaskara II's works included systematic treatment of algebraic problems.",
        "type": "Primary Text",
        "period": "12th century CE",
        "location": "Ujjain / India",
        "description": "Bijaganita and related works contain algebraic procedures and equation-solving methods.",
        "reference": "Bijaganita; algebraic rules",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "primary_type": "Primary mathematical text represented through scholarly discussion",
        "scholarly_type": "Academic history of mathematics",
        "reliability": "High",
        "status": "Scholarly source verified; exact edition passage pending"
    },
    {
        "topic": "Astronomy and Mathematics",
        "claim": "Bhaskara II's Siddhantasiromani contained mathematical astronomy and spherical astronomy.",
        "type": "Primary Text",
        "period": "12th century CE",
        "location": "Ujjain / India",
        "description": "Siddhantasiromani included sections devoted to astronomical calculations and the sphere.",
        "reference": "Siddhantasiromani; astronomical sections",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Bhaskara_II/",
        "primary_type": "Primary astronomical text represented through scholarly discussion",
        "scholarly_type": "Academic history of astronomy",
        "reliability": "High",
        "status": "Scholarly source verified"
    },
    {
        "topic": "Mathematics",
        "claim": "Indian mathematical traditions developed sophisticated use of place-value notation.",
        "type": "Historical Record",
        "period": "Ancient and medieval India",
        "location": "India",
        "description": "Historical scholarship documents the development and use of decimal positional notation in India. Chronology and transmission should be stated cautiously.",
        "reference": "History of Indian numerals",
        "source_url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_numerals/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_numerals/",
        "primary_type": "Historical evidence discussed in scholarship",
        "scholarly_type": "Academic history of mathematics",
        "reliability": "High",
        "status": "Scholarly source verified; chronology requires qualification"
    },
    {
        "topic": "Mathematics",
        "claim": "The use of zero as a mathematical number is documented in Indian mathematical history by the early medieval period.",
        "type": "Historical Record",
        "period": "Early medieval India",
        "location": "India",
        "description": "Historical research distinguishes between the use of zero as a placeholder and its treatment as a number.",
        "reference": "History of zero in Indian mathematics",
        "source_url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Zero/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Zero/",
        "primary_type": "Historical mathematical evidence",
        "scholarly_type": "Academic history of mathematics",
        "reliability": "High",
        "status": "Scholarly source verified"
    },
    {
        "topic": "Mathematics",
        "claim": "Indian mathematicians developed algorithms for arithmetic operations using the decimal place-value system.",
        "type": "Historical Record",
        "period": "Ancient and medieval India",
        "location": "India",
        "description": "Historical accounts describe computational procedures using positional notation.",
        "reference": "Indian mathematics and numeral history",
        "source_url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_mathematics/",
        "scholarly_url": "https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_mathematics/",
        "primary_type": "Historical mathematical evidence",
        "scholarly_type": "Academic history of mathematics",
        "reliability": "High",
        "status": "Scholarly source verified"
    },
    {
        "topic": "Medicine",
        "claim": "Ancient Indian medical traditions developed systematic schools of physicians and surgeons.",
        "type": "Historical Record",
        "period": "Ancient India",
        "location": "India",
        "description": "Historical scholarship describes the development of physicians, surgeons, medical education and organized medical traditions.",
        "reference": "Historical review of physicians and surgeons in ancient India",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3336666/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3336666/",
        "primary_type": "Historical medical evidence",
        "scholarly_type": "Scholarly historical review",
        "reliability": "High",
        "status": "Scholarly source verified"
    },
    {
        "topic": "Medicine",
        "claim": "Ancient Indian medical education included training in medicine and surgery.",
        "type": "Historical Record",
        "period": "Ancient India",
        "location": "India",
        "description": "Historical research describes rigorous medical training and expectations placed on physicians.",
        "reference": "Physicians of ancient India; medical training",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "primary_type": "Historical medical evidence",
        "scholarly_type": "Scholarly historical review",
        "reliability": "High",
        "status": "Scholarly source verified"
    },
    {
        "topic": "Medicine",
        "claim": "The Charaka and Sushruta Samhitas became major classical sources for Indian medicine and surgery.",
        "type": "Historical Record",
        "period": "Early centuries CE",
        "location": "India",
        "description": "Historical scholarship identifies Charaka Samhita and Sushruta Samhita as foundational classical medical compilations.",
        "reference": "History of Indian medical literature",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "primary_type": "Historical medical evidence",
        "scholarly_type": "Scholarly historical review",
        "reliability": "High",
        "status": "Scholarly source verified; dating varies by scholarly reconstruction"
    },
    {
        "topic": "Anatomy",
        "claim": "The Sushruta Samhita contains detailed descriptions of bones, joints, muscles and other anatomical structures.",
        "type": "Primary Text",
        "period": "Ancient India; dating debated",
        "location": "Kashi / Varanasi tradition",
        "description": "Scholarly analysis discusses anatomical material in the Sushruta Samhita and the historical study of human morphology.",
        "reference": "Sushruta Samhita; anatomical descriptions",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3039177/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3039177/",
        "primary_type": "Primary medical text represented through scholarly analysis",
        "scholarly_type": "Scholarly anatomical history",
        "reliability": "High",
        "status": "Scholarly source verified; chronology and anatomical interpretation require qualification"
    },
    {
        "topic": "Surgery",
        "claim": "The Sushruta Samhita describes surgical instruments, incisions, suturing, bandaging and fracture management.",
        "type": "Primary Text",
        "period": "Ancient India; dating debated",
        "location": "Kashi / Varanasi tradition",
        "description": "A scholarly review identifies detailed surgical procedures and instruments in the Sushruta Samhita.",
        "reference": "Sushruta Samhita; surgical techniques",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8039338/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8039338/",
        "primary_type": "Primary medical text represented through scholarly analysis",
        "scholarly_type": "Scholarly medical-history review",
        "reliability": "High",
        "status": "Scholarly source verified; historical dating requires qualification"
    },
    {
        "topic": "Surgery",
        "claim": "The Sushruta tradition includes descriptions of reconstructive nasal surgery.",
        "type": "Primary Text",
        "period": "Ancient India; dating debated",
        "location": "Kashi / Varanasi tradition",
        "description": "Historical medical scholarship discusses reconstructive procedures attributed to the Sushruta tradition, including nasal reconstruction.",
        "reference": "Sushruta Samhita; reconstructive surgery",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11527508/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11527508/",
        "primary_type": "Primary medical text represented through scholarly analysis",
        "scholarly_type": "Scholarly medical-history review",
        "reliability": "High",
        "status": "Scholarly source located; exact textual passage pending edition verification"
    },
    {
        "topic": "Surgery",
        "claim": "The Sushruta tradition contains an account of cataract extraction using a surgical technique.",
        "type": "Primary Text",
        "period": "Ancient India; dating debated",
        "location": "India",
        "description": "Modern historical reviews discuss a cataract procedure described in the Sushruta Samhita.",
        "reference": "Sushruta Samhita; cataract procedure",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8039338/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8039338/",
        "primary_type": "Primary medical text represented through scholarly analysis",
        "scholarly_type": "Scholarly medical-history review",
        "reliability": "High",
        "status": "Scholarly source verified; exact textual passage pending edition verification"
    },
    {
        "topic": "Medicine",
        "claim": "Historical research describes professional physicians, state-employed medical practitioners and medical services in ancient India.",
        "type": "Historical Record",
        "period": "Ancient India",
        "location": "India",
        "description": "Historical scholarship discusses physicians working as full-time practitioners, in state service and in military contexts.",
        "reference": "Physicians of ancient India; professional medical practice",
        "source_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "scholarly_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5084543/",
        "primary_type": "Historical medical evidence",
        "scholarly_type": "Scholarly social history",
        "reliability": "High",
        "status": "Scholarly source verified"
    }
]

conn = sqlite3.connect(DB)
cursor = conn.cursor()

today = date.today().isoformat()

for item in records:

    cursor.execute(
        """
        INSERT INTO sources
        (title, source_type, author, date_period, language, url, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            item["reference"],
            item["type"],
            None,
            item["period"],
            "Sanskrit / English scholarship",
            item["source_url"],
            "Batch 03 source; claims are recorded with historical limitations."
        )
    )

    source_id = cursor.lastrowid

    cursor.execute(
        """
        INSERT INTO evidence
        (source_id, topic, claim, evidence_type, historical_period, location, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            source_id,
            item["topic"],
            item["claim"],
            item["type"],
            item["period"],
            item["location"],
            item["description"]
        )
    )

    evidence_id = cursor.lastrowid

    cursor.execute(
        """
        INSERT INTO references_data
        (
            evidence_id,
            reference_text,
            page_or_verse,
            url,
            source_url,
            source_access_date,
            scholarly_reference,
            scholarly_url,
            primary_source_type,
            scholarly_source_type,
            source_reliability,
            citation_verified,
            verification_notes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            evidence_id,
            item["reference"],
            "Exact edition/page/verse pending where not specified",
            item["source_url"],
            item["source_url"],
            today,
            item["reference"],
            item["scholarly_url"],
            item["primary_type"],
            item["scholarly_type"],
            item["reliability"],
            item["status"],
            "Batch 03. Scholarly evidence is recorded separately from claims about exact primary-text wording. Historical dating and interpretation are qualified where necessary."
        )
    )

    cursor.execute(
        """
        INSERT INTO evidence_quality
        (evidence_id, source_quality, citation_quality, verification_status, confidence_notes)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            evidence_id,
            item["reliability"],
            "Scholarly source attached",
            item["status"],
            "Claim should not be interpreted beyond the cited historical evidence."
        )
    )

conn.commit()

print("Research Batch 03 added successfully.")
print("Records added:", len(records))

total_evidence = cursor.execute(
    "SELECT COUNT(*) FROM evidence"
).fetchone()[0]

total_references = cursor.execute(
    "SELECT COUNT(*) FROM references_data"
).fetchone()[0]

print("Total evidence records:", total_evidence)
print("Total reference records:", total_references)

conn.close()