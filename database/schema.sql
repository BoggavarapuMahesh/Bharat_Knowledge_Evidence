-- ============================================================
-- BHARAT KNOWLEDGE EVIDENCE
-- Initial Relational Database Schema
-- ============================================================

CREATE DATABASE bharat_knowledge_evidence;

-- After creating the database, connect to it before running
-- the remaining tables.

-- ============================================================
-- 1. LOCATIONS
-- ============================================================

CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ancient_name VARCHAR(255),
    modern_name VARCHAR(255),
    country VARCHAR(100),
    state_region VARCHAR(255),
    latitude DECIMAL(10,7),
    longitude DECIMAL(10,7),
    historical_period VARCHAR(255),
    description TEXT
);

-- ============================================================
-- 2. PEOPLE
-- ============================================================

CREATE TABLE people (
    person_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    alternative_name VARCHAR(500),
    birth_year INTEGER,
    death_year INTEGER,
    birth_year_type VARCHAR(50),
    death_year_type VARCHAR(50),
    region_id INTEGER REFERENCES locations(location_id),
    tradition VARCHAR(255),
    occupation VARCHAR(255),
    known_for TEXT,
    biography TEXT
);

-- ============================================================
-- 3. TEXTS
-- ============================================================

CREATE TABLE texts (
    text_id SERIAL PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    alternative_title VARCHAR(500),
    language VARCHAR(100),
    script VARCHAR(100),
    text_type VARCHAR(150),
    tradition VARCHAR(255),
    author_id INTEGER REFERENCES people(person_id),
    estimated_date_start INTEGER,
    estimated_date_end INTEGER,
    dating_method TEXT,
    original_location_id INTEGER REFERENCES locations(location_id),
    description TEXT,
    critical_edition TEXT
);

-- ============================================================
-- 4. MANUSCRIPTS
-- ============================================================

CREATE TABLE manuscripts (
    manuscript_id SERIAL PRIMARY KEY,
    text_id INTEGER REFERENCES texts(text_id),
    repository VARCHAR(500),
    collection VARCHAR(500),
    catalogue_number VARCHAR(255),
    location_id INTEGER REFERENCES locations(location_id),
    language VARCHAR(100),
    script VARCHAR(100),
    material VARCHAR(100),
    estimated_date VARCHAR(255),
    dating_method TEXT,
    condition VARCHAR(255),
    digitized BOOLEAN DEFAULT FALSE,
    digital_url TEXT,
    catalogue_url TEXT,
    description TEXT
);

-- ============================================================
-- 5. PASSAGES
-- ============================================================

CREATE TABLE passages (
    passage_id SERIAL PRIMARY KEY,
    text_id INTEGER NOT NULL REFERENCES texts(text_id),
    book VARCHAR(255),
    kanda VARCHAR(255),
    chapter VARCHAR(255),
    section VARCHAR(255),
    verse VARCHAR(255),
    page VARCHAR(100),
    original_language VARCHAR(100),
    original_script TEXT,
    original_text TEXT,
    transliteration TEXT,
    translation TEXT,
    translator VARCHAR(500),
    translation_source TEXT,
    context TEXT,
    passage_notes TEXT
);

-- ============================================================
-- 6. CONTRIBUTIONS
-- ============================================================

CREATE TABLE contributions (
    contribution_id SERIAL PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    category VARCHAR(150) NOT NULL,
    sub_category VARCHAR(255),
    description TEXT,
    period_start INTEGER,
    period_end INTEGER,
    region_id INTEGER REFERENCES locations(location_id),
    person_id INTEGER REFERENCES people(person_id),
    text_id INTEGER REFERENCES texts(text_id),
    historical_significance TEXT,
    modern_comparison TEXT,
    evidence_status VARCHAR(100),
    research_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- 7. SOURCES
-- ============================================================

CREATE TABLE sources (
    source_id SERIAL PRIMARY KEY,
    source_type VARCHAR(100) NOT NULL,
    title VARCHAR(1000) NOT NULL,
    author VARCHAR(500),
    institution VARCHAR(500),
    publisher VARCHAR(500),
    publication_year INTEGER,
    edition VARCHAR(500),
    volume VARCHAR(100),
    page VARCHAR(100),
    doi VARCHAR(500),
    isbn VARCHAR(100),
    url TEXT,
    access_date DATE,
    source_quality VARCHAR(100),
    source_notes TEXT
);

-- ============================================================
-- 8. EVIDENCE
-- ============================================================

CREATE TABLE evidence (
    evidence_id SERIAL PRIMARY KEY,
    contribution_id INTEGER NOT NULL REFERENCES contributions(contribution_id),
    passage_id INTEGER REFERENCES passages(passage_id),
    source_id INTEGER REFERENCES sources(source_id),
    evidence_type VARCHAR(150),
    evidence_description TEXT,
    directness VARCHAR(100),
    dating_confidence VARCHAR(100),
    interpretation_level VARCHAR(150),
    independent_confirmation TEXT,
    archaeological_support TEXT,
    material_support TEXT,
    scholarly_support TEXT,
    evidence_strength VARCHAR(100),
    verification_status VARCHAR(100),
    disputed_status BOOLEAN DEFAULT FALSE,
    researcher_notes TEXT
);

-- ============================================================
-- 9. MODERN CONCEPTS
-- ============================================================

CREATE TABLE modern_concepts (
    modern_concept_id SERIAL PRIMARY KEY,
    concept VARCHAR(500) NOT NULL,
    modern_field VARCHAR(255),
    modern_definition TEXT,
    modern_development_date VARCHAR(255),
    modern_source TEXT,
    similarity_description TEXT,
    difference_description TEXT,
    historical_connection TEXT,
    transmission_evidence TEXT,
    independent_development TEXT,
    comparison_status VARCHAR(150),
    notes TEXT
);

-- ============================================================
-- 10. CITATIONS
-- ============================================================

CREATE TABLE citations (
    citation_id SERIAL PRIMARY KEY,
    source_id INTEGER NOT NULL REFERENCES sources(source_id),
    cited_source_id INTEGER REFERENCES sources(source_id),
    citation_type VARCHAR(150),
    page VARCHAR(100),
    chapter VARCHAR(255),
    quote TEXT,
    citation_context TEXT,
    verified BOOLEAN DEFAULT FALSE,
    notes TEXT
);