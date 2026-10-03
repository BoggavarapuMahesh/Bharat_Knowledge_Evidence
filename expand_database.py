import sqlite3

DB = "bharat_knowledge.db"

conn = sqlite3.connect(DB)
cursor = conn.cursor()

cursor.executescript("""

CREATE TABLE IF NOT EXISTS people (
    person_id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT,
    period TEXT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS places (
    place_id INTEGER PRIMARY KEY,
    name TEXT,
    ancient_name TEXT,
    modern_country TEXT,
    latitude REAL,
    longitude REAL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS fields (
    field_id INTEGER PRIMARY KEY,
    field_name TEXT UNIQUE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS historical_periods (
    period_id INTEGER PRIMARY KEY,
    period_name TEXT UNIQUE,
    start_date TEXT,
    end_date TEXT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS texts (
    text_id INTEGER PRIMARY KEY,
    title TEXT,
    text_type TEXT,
    language TEXT,
    approximate_period TEXT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS verses (
    verse_id INTEGER PRIMARY KEY,
    text_id INTEGER,
    book TEXT,
    chapter TEXT,
    verse TEXT,
    original_text TEXT,
    translation TEXT,
    FOREIGN KEY(text_id) REFERENCES texts(text_id)
);

CREATE TABLE IF NOT EXISTS evidence_types (
    evidence_type_id INTEGER PRIMARY KEY,
    type_name TEXT UNIQUE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS evidence_fields (
    evidence_id INTEGER,
    field_id INTEGER,
    PRIMARY KEY(evidence_id, field_id),
    FOREIGN KEY(evidence_id) REFERENCES evidence(evidence_id),
    FOREIGN KEY(field_id) REFERENCES fields(field_id)
);

CREATE TABLE IF NOT EXISTS evidence_places (
    evidence_id INTEGER,
    place_id INTEGER,
    PRIMARY KEY(evidence_id, place_id),
    FOREIGN KEY(evidence_id) REFERENCES evidence(evidence_id),
    FOREIGN KEY(place_id) REFERENCES places(place_id)
);

CREATE TABLE IF NOT EXISTS evidence_people (
    evidence_id INTEGER,
    person_id INTEGER,
    relationship TEXT,
    PRIMARY KEY(evidence_id, person_id),
    FOREIGN KEY(evidence_id) REFERENCES evidence(evidence_id),
    FOREIGN KEY(person_id) REFERENCES people(person_id)
);

CREATE TABLE IF NOT EXISTS evidence_texts (
    evidence_id INTEGER,
    text_id INTEGER,
    relationship TEXT,
    PRIMARY KEY(evidence_id, text_id),
    FOREIGN KEY(evidence_id) REFERENCES evidence(evidence_id),
    FOREIGN KEY(text_id) REFERENCES texts(text_id)
);

CREATE TABLE IF NOT EXISTS evidence_quality (
    quality_id INTEGER PRIMARY KEY,
    evidence_id INTEGER,
    source_quality TEXT,
    citation_quality TEXT,
    verification_status TEXT,
    confidence_notes TEXT,
    FOREIGN KEY(evidence_id) REFERENCES evidence(evidence_id)
);

""")

conn.commit()
conn.close()

print("Expanded database structure created successfully.")