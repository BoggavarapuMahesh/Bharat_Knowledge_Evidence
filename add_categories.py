import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

fields = [
    ("Mathematics", "Mathematical concepts, methods and texts"),
    ("Astronomy", "Astronomical observations, calendars and calculations"),
    ("Medicine", "Ayurveda and historical medical knowledge"),
    ("Yoga", "Yoga, meditation and related traditions"),
    ("Philosophy", "Philosophical concepts and schools"),
    ("Linguistics", "Language, grammar and linguistic traditions"),
    ("Literature", "Literary works and traditions"),
    ("Architecture", "Architecture, construction and urban planning"),
    ("Metallurgy", "Historical metalworking and materials"),
    ("Agriculture", "Agricultural knowledge and practices"),
    ("Education", "Educational institutions and learning traditions"),
    ("Logic", "Logic, reasoning and debate traditions"),
    ("Ethics", "Ethical and moral concepts"),
    ("Law", "Legal and social texts"),
    ("Technology", "Historical technological knowledge"),
    ("Economics", "Economic and trade traditions"),
    ("Music", "Music theory and traditions"),
    ("Arts", "Visual and performing arts"),
    ("Phonetics", "Phonetics and pronunciation traditions"),
    ("Grammar", "Formal grammatical traditions"),
    ("Geography", "Geographical knowledge and descriptions")
]

for name, description in fields:
    cursor.execute(
        "INSERT OR IGNORE INTO fields (field_name, description) VALUES (?, ?)",
        (name, description)
    )

evidence_types = [
    ("Primary Text", "Evidence directly from a historical text"),
    ("Inscription", "Evidence from an inscription"),
    ("Archaeological", "Material or archaeological evidence"),
    ("Manuscript", "Evidence from a manuscript"),
    ("Historical Record", "Historical documentary evidence"),
    ("Scholarly Research", "Modern academic research"),
    ("Linguistic Evidence", "Evidence from language or linguistics"),
    ("Comparative Evidence", "Evidence involving comparison between sources"),
    ("Scientific Analysis", "Evidence supported by scientific analysis")
]

for name, description in evidence_types:
    cursor.execute(
        "INSERT OR IGNORE INTO evidence_types (type_name, description) VALUES (?, ?)",
        (name, description)
    )

conn.commit()

print("Categories added successfully.")
print("Fields:", cursor.execute("SELECT COUNT(*) FROM fields").fetchone()[0])
print("Evidence types:", cursor.execute("SELECT COUNT(*) FROM evidence_types").fetchone()[0])

conn.close()