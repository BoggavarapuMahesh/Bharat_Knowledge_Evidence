import sqlite3

DB = "bharat_knowledge.db"

records = [
    {
        "title": "Panini's systematic grammatical rules",
        "source_type": "Scholarly Research",
        "author": "John J. Lowe",
        "period": "c. 4th century BCE",
        "language": "Sanskrit",
        "topic": "Linguistics",
        "claim": "Panini's Ashtadhyayi presents a highly systematic rule-based description of Sanskrit grammar.",
        "description": "Modern linguistic scholarship analyzes the Ashtadhyayi as an organized grammatical system containing interacting rules.",
        "source_url": "https://www.cambridge.org/core/books/abs/modern-linguistics-in-ancient-india/astadhyayi-at-work/986D88D54862FC7A68F641A6F7ACF387",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Panini and Sanskrit morphology",
        "source_type": "Scholarly Research",
        "author": "John J. Lowe",
        "period": "c. 4th century BCE",
        "language": "Sanskrit",
        "topic": "Grammar",
        "claim": "The Ashtadhyayi contains rules governing morphological formation in Sanskrit.",
        "description": "Modern analysis demonstrates how Paninian rules derive grammatical forms from linguistic inputs.",
        "source_url": "https://www.cambridge.org/core/books/abs/modern-linguistics-in-ancient-india/astadhyayi-at-work/986D88D54862FC7A68F641A6F7ACF387",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Panini and syntax",
        "source_type": "Scholarly Research",
        "author": "John J. Lowe",
        "period": "c. 4th century BCE",
        "language": "Sanskrit",
        "topic": "Grammar",
        "claim": "Paninian grammatical analysis includes rules relevant to Sanskrit sentence structure and syntax.",
        "description": "Modern scholarship examines how Panini's system handles sentence derivation and syntactic relationships.",
        "source_url": "https://www.cambridge.org/core/books/abs/modern-linguistics-in-ancient-india/astadhyayi-at-work/986D88D54862FC7A68F641A6F7ACF387",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Panini and phonological analysis",
        "source_type": "Scholarly Research",
        "author": "J. F. Staal",
        "period": "c. 4th century BCE",
        "language": "Sanskrit",
        "topic": "Phonetics",
        "claim": "Paninian grammatical analysis includes systematic treatment of Sanskrit sound classes and phonological processes.",
        "description": "Historical linguistic research examines Panini's organization and analysis of Sanskrit consonants and sound patterns.",
        "source_url": "https://www.cambridge.org/core/journals/language/article/abs/a-method-of-linguistic-description-the-order-of-consonants-according-to-panini/ADA286A56F41020B15B4149023C7C0771",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Paninian rule interaction",
        "source_type": "Scholarly Research",
        "author": "John J. Lowe",
        "period": "c. 4th century BCE",
        "language": "Sanskrit",
        "topic": "Logic",
        "claim": "The Ashtadhyayi uses interacting grammatical rules whose application contributes to the derivation of linguistic forms.",
        "description": "Modern analysis explicitly studies rule interaction as an important feature of Panini's grammatical system.",
        "source_url": "https://www.cambridge.org/core/books/abs/modern-linguistics-in-ancient-india/astadhyayi-at-work/986D88D54862FC7A68F641A6F7ACF387",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Panini and formal-language analysis",
        "source_type": "Scholarly Research",
        "author": "John J. Lowe",
        "period": "Ancient India",
        "language": "Sanskrit",
        "topic": "Linguistics",
        "claim": "Modern linguistic scholarship evaluates the formal properties and generative capacity of Panini's grammatical system.",
        "description": "The comparison with formal language theory is a modern scholarly analysis and should not be treated as an ancient claim about computer science.",
        "source_url": "https://www.cambridge.org/core/books/abs/modern-linguistics-in-ancient-india/formal-language-theory-and-computational-power/173B5AB75A967C6F2138B82CD1338651",
        "verification": "Scholarly source verified; modern comparison explicitly distinguished from historical context."
    },
    {
        "title": "Indian traditions of linguistic analysis",
        "source_type": "Scholarly Research",
        "author": "Madhav M. Deshpande",
        "period": "Premodern India",
        "language": "Sanskrit and other South Asian languages",
        "topic": "Linguistics",
        "claim": "Premodern Indian traditions developed sustained analysis of phonetics, grammar, etymology and related linguistic subjects.",
        "description": "Cambridge's history of linguistics discusses the breadth of linguistic analysis in the Sanskrit tradition.",
        "source_url": "https://www.cambridge.org/core/books/abs/cambridge-history-of-linguistics/history-of-linguistic-analysis-in-the-sanskrit-tradition-in-premodern-india-with-a-brief-discussion-of-vernacular-grammars/0FB92D02A57DF0E07D7360F4B539DC81",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Varahamihira's Panchasiddhantika",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "6th century CE",
        "language": "Sanskrit",
        "topic": "Astronomy",
        "claim": "Varahamihira's Panchasiddhantika summarized five earlier astronomical traditions.",
        "description": "Historical scholarship identifies the Panchasiddhantika as an important source for studying earlier Indian astronomical traditions.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Varahamihira/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Varahamihira and astronomical synthesis",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "6th century CE",
        "language": "Sanskrit",
        "topic": "Astronomy",
        "claim": "Varahamihira incorporated and summarized astronomical material from multiple earlier traditions.",
        "description": "The Panchasiddhantika preserves information about several earlier astronomical systems, including traditions with Greek-related material.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Varahamihira/",
        "verification": "Scholarly source verified; cross-cultural transmission should be represented rather than omitted."
    },
    {
        "title": "Varahamihira and trigonometric work",
        "source_type": "Scholarly Research",
        "author": "Ian G. Pearce / MacTutor",
        "period": "6th century CE",
        "language": "Sanskrit",
        "topic": "Mathematics",
        "claim": "Historical accounts associate Varahamihira with trigonometric formulas and improvement of astronomical sine tables.",
        "description": "MacTutor's historical account discusses Varahamihira's mathematical and astronomical contributions.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-11/",
        "verification": "Scholarly historical source verified."
    },
    {
        "title": "Varahamihira and binomial coefficients",
        "source_type": "Scholarly Research",
        "author": "Ian G. Pearce / MacTutor",
        "period": "6th century CE",
        "language": "Sanskrit",
        "topic": "Mathematics",
        "claim": "Historical accounts describe Varahamihira's work involving binomial coefficients and a form of Pascal's triangle.",
        "description": "The historical account connects this work with calculations involving binomial coefficients.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Varahamihira/",
        "verification": "Scholarly source verified; terminology such as Pascal's triangle is a modern comparative description."
    },
    {
        "title": "Aryabhata's sine table tradition",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "5th–6th century CE",
        "language": "Sanskrit",
        "topic": "Astronomy",
        "claim": "The Aryabhatiya contains a table of sines that influenced later Indian mathematical astronomy.",
        "description": "Historical accounts describe Aryabhata's trigonometric work and the later commentarial tradition surrounding it.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-10/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Bhaskara I and approximation of the sine function",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "7th century CE",
        "language": "Sanskrit",
        "topic": "Mathematics",
        "claim": "Historical accounts attribute to Bhaskara I an accurate approximation for the sine function.",
        "description": "Bhaskara I's commentary on Aryabhata's work developed mathematical and astronomical ideas further.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-10/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Ujjain as a centre of mathematical astronomy",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "Classical India",
        "language": "Sanskrit",
        "topic": "Astronomy",
        "claim": "Historical scholarship identifies Ujjain as an important centre for mathematical astronomy in classical India.",
        "description": "The Ujjain school is associated with figures including Varahamihira and Brahmagupta.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Biographies/Brahmagupta/",
        "verification": "Scholarly source verified."
    },
    {
        "title": "Transmission of Indian astronomy to the Islamic world",
        "source_type": "Scholarly Research",
        "author": "MacTutor History of Mathematics",
        "period": "Early medieval period",
        "language": "Sanskrit and Arabic",
        "topic": "Astronomy",
        "claim": "Historical scholarship documents the transmission and assimilation of Indian astronomical material into Islamic astronomical traditions.",
        "description": "Indian astronomical works and ideas formed part of wider exchanges of mathematical and astronomical knowledge.",
        "source_url": "https://mathshistory.st-andrews.ac.uk/Astronomy/StructureOfSolarSystem/",
        "verification": "Scholarly source verified; transmission occurred through multiple historical stages."
    },
    {
        "title": "Nalanda as a long-running scholastic institution",
        "source_type": "Archaeological",
        "author": "UNESCO World Heritage Centre",
        "period": "3rd century BCE–13th century CE",
        "language": "Multiple",
        "topic": "Education",
        "claim": "The archaeological site of Nalanda Mahavihara represents a long-running monastic and scholastic institution in South Asia.",
        "description": "UNESCO identifies archaeological remains of educational and residential buildings and describes organized transmission of knowledge over centuries.",
        "source_url": "https://whc.unesco.org/en/list/1502/",
        "verification": "UNESCO source verified."
    },
    {
        "title": "Nalanda's residential educational infrastructure",
        "source_type": "Archaeological",
        "author": "UNESCO World Heritage Centre",
        "period": "Early medieval South Asia",
        "language": "Multiple",
        "topic": "Architecture",
        "claim": "Nalanda's archaeological remains include viharas that functioned as residential and educational buildings.",
        "description": "The site demonstrates the architectural development of monastic and educational infrastructure.",
        "source_url": "https://whc.unesco.org/en/list/1502/",
        "verification": "UNESCO source verified."
    },
    {
        "title": "Nalanda and organized knowledge transmission",
        "source_type": "Archaeological",
        "author": "UNESCO World Heritage Centre",
        "period": "Ancient and early medieval South Asia",
        "language": "Multiple",
        "topic": "Education",
        "claim": "UNESCO describes Nalanda as an institution associated with organized transmission of knowledge over an extended historical period.",
        "description": "The archaeological site provides evidence for a sustained institutional tradition of monastic and scholastic learning.",
        "source_url": "https://whc.unesco.org/en/list/1502/",
        "verification": "UNESCO source verified; institutional comparisons with modern universities should be treated cautiously."
    },
    {
        "title": "Nalanda and development of educational architecture",
        "source_type": "Archaeological",
        "author": "UNESCO World Heritage Centre",
        "period": "Early medieval South Asia",
        "language": "Multiple",
        "topic": "Architecture",
        "claim": "Nalanda demonstrates the development of purpose-associated residential and educational architectural infrastructure.",
        "description": "UNESCO's assessment discusses the standardization and evolution of vihara architecture at the site.",
        "source_url": "https://whc.unesco.org/en/list/1502/",
        "verification": "UNESCO source verified."
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
        "Scholarly source verified",
        item["verification"],
        item["source_url"],
        "Scholarly / institutional source",
        "High",
        "Source checked; primary-text or archaeological-record verification may still be required"
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

print("Research Batch 05 added successfully.")
print("Records added:", added)
print("Total evidence records:", total_evidence)
print("Total reference records:", total_refs)