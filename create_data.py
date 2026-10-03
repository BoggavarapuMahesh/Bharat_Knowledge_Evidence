import sqlite3

DB = "bharat_knowledge.db"

conn = sqlite3.connect(DB)
cursor = conn.cursor()

# Add a source
cursor.execute("""
INSERT INTO sources
(title, source_type, author, date_period, language, url, notes)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (
    "Rigveda",
    "Vedic Scripture",
    "Traditional Vedic corpus",
    "Ancient India",
    "Vedic Sanskrit",
    "",
    "One of the four Vedas; evidence should be linked to specific hymns where possible."
))

# Add an evidence record
source_id = cursor.lastrowid

cursor.execute("""
INSERT INTO evidence
(source_id, topic, claim, evidence_type, historical_period, location, description)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (
    source_id,
    "Vedic Literature",
    "Rigvedic material preserves evidence of early Vedic religious, philosophical and cultural traditions.",
    "Primary textual source",
    "Vedic period",
    "Indian subcontinent",
    "Record specific hymns and verses when documenting individual claims."
))

evidence_id = cursor.lastrowid

# Add a reference
cursor.execute("""
INSERT INTO references_data
(evidence_id, reference_text, page_or_verse, url)
VALUES (?, ?, ?, ?)
""", (
    evidence_id,
    "Rigveda",
    "Specific hymn/verse to be verified",
    ""
))

# Add a contribution
cursor.execute("""
INSERT INTO contributions
(evidence_id, field, contribution, significance, modern_relevance)
VALUES (?, ?, ?, ?, ?)
""", (
    evidence_id,
    "Philosophy and Literature",
    "Vedic literature provides primary textual material for studying ancient Indian intellectual traditions.",
    "Useful for historical and comparative study.",
    "Can be studied through textual, linguistic and historical analysis."
))

conn.commit()
conn.close()

print("Sample evidence record added successfully.")