import sqlite3

conn = sqlite3.connect("bharat_knowledge.db")
cursor = conn.cursor()

print("\nSANATANA DHARMA EVIDENCE DATABASE")
print("=" * 60)

evidence_count = cursor.execute(
    "SELECT COUNT(*) FROM evidence"
).fetchone()[0]

reference_count = cursor.execute(
    "SELECT COUNT(*) FROM references_data"
).fetchone()[0]

source_url_count = cursor.execute(
    """
    SELECT COUNT(*)
    FROM references_data
    WHERE source_url IS NOT NULL
      AND TRIM(source_url) != ''
    """
).fetchone()[0]

scholarly_count = cursor.execute(
    """
    SELECT COUNT(*)
    FROM references_data
    WHERE scholarly_source_url IS NOT NULL
      AND TRIM(scholarly_source_url) != ''
    """
).fetchone()[0]

primary_count = cursor.execute(
    """
    SELECT COUNT(*)
    FROM references_data
    WHERE primary_source_url IS NOT NULL
      AND TRIM(primary_source_url) != ''
    """
).fetchone()[0]

print("Evidence records:", evidence_count)
print("Reference records:", reference_count)
print("References with source URLs:", source_url_count)
print("References with scholarly URLs:", scholarly_count)
print("References with primary URLs:", primary_count)

print("\nVERIFICATION STATUS")
print("-" * 60)

statuses = cursor.execute(
    """
    SELECT citation_verified, COUNT(*)
    FROM references_data
    GROUP BY citation_verified
    ORDER BY COUNT(*) DESC
    """
).fetchall()

for status, count in statuses:
    status_name = status if status else "Not classified"
    print(f"{status_name}: {count}")

print("\n" + "=" * 60)

conn.close()