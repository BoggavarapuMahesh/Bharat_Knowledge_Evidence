import sqlite3

DB = "bharat_knowledge.db"

conn = sqlite3.connect(DB)
cur = conn.cursor()

updates = {
    1: (
        "VedaWeb – Rigveda",
        "https://vedaweb.uni-koeln.de/rigveda/view",
        "VedaWeb provides a digitally processed and annotated Rigveda corpus for scholarly study of Old Indo-Aryan texts.",
        "Primary-text research platform",
        "High",
        "Primary source resource verified; individual historical claims still require specific hymn/passage citations."
    ),

    11: (
        "VedaWeb – Rigveda",
        "https://vedaweb.uni-koeln.de/rigveda/view",
        "VedaWeb provides a digitally processed and annotated Rigveda corpus for scholarly study of Old Indo-Aryan texts.",
        "Primary-text research platform",
        "High",
        "Primary source resource verified; individual historical claims still require specific hymn/passage citations."
    )
}

for reference_id, data in updates.items():

    work, url, reference_text, source_type, reliability, notes = data

    cur.execute("""
        UPDATE references_data
        SET
            reference_text = ?,
            citation_work = ?,
            source_url = ?,
            primary_source_url = ?,
            primary_source_type = ?,
            source_reliability = ?,
            verification_status = ?,
            verification_notes = ?,
            citation_verified = ?
        WHERE reference_id = ?
    """, (
        reference_text,
        work,
        url,
        url,
        source_type,
        reliability,
        "Primary source resource verified",
        notes,
        "Yes",
        reference_id
    ))

conn.commit()

print("=" * 70)
print("OLD RIGVEDA REFERENCES UPDATED")
print("=" * 70)

for reference_id in [1, 11]:
    cur.execute("""
        SELECT
            reference_id,
            evidence_id,
            source_url,
            primary_source_url,
            citation_verified
        FROM references_data
        WHERE reference_id = ?
    """, (reference_id,))

    print(cur.fetchone())

conn.close()

print("=" * 70)
print("Updated 2 existing references.")
print("=" * 70)