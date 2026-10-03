# \# Bharat Knowledge Evidence Database

# 

# \## Overview

# 

# Bharat Knowledge Evidence is a structured relational database designed to document historical, textual, archaeological, scientific, linguistic, mathematical, medical, philosophical, and cultural evidence associated with Indian knowledge traditions.

# 

# The project focuses on organizing evidence together with its sources, references, verification information, historical context, fields of knowledge, and related texts.

# 

# The purpose of the database is to create a structured and traceable research dataset that can be expanded, analyzed, and independently reviewed.

# 

# \---

# 

# \## Project Objectives

# 

# \* Build a structured evidence database related to Indian knowledge traditions.

# \* Connect individual evidence records with documented sources and references.

# \* Preserve source URLs for future verification.

# \* Distinguish primary-source resources from scholarly research.

# \* Organize evidence across multiple knowledge fields.

# \* Record verification and source-quality information.

# \* Create a reusable dataset for data analysis and visualization.

# \* Provide a foundation for future research and comparative analysis.

# 

# \---

# 

# \## Current Dataset

# 

# | Metric                           |   Value |

# | -------------------------------- | ------: |

# | Evidence records                 |     103 |

# | Reference records                |     105 |

# | Knowledge fields                 |      21 |

# | Evidence types                   |       9 |

# | Database tables                  |      16 |

# | Evidence records with references | 103/103 |

# | References with URLs             | 105/105 |

# | Scholarly URL coverage           |  98.10% |

# | Primary-source URL coverage      |  35.24% |

# 

# \---

# 

# \## Knowledge Fields

# 

# The database currently covers 21 fields:

# 

# 1\. Mathematics

# 2\. Astronomy

# 3\. Medicine

# 4\. Yoga

# 5\. Philosophy

# 6\. Linguistics

# 7\. Literature

# 8\. Architecture

# 9\. Metallurgy

# 10\. Agriculture

# 11\. Education

# 12\. Logic

# 13\. Ethics

# 14\. Law

# 15\. Technology

# 16\. Economics

# 17\. Music

# 18\. Arts

# 19\. Phonetics

# 20\. Grammar

# 21\. Geography

# 

# \---

# 

# \## Evidence Types

# 

# The database uses nine evidence categories:

# 

# 1\. Primary Text

# 2\. Inscription

# 3\. Archaeological

# 4\. Manuscript

# 5\. Historical Record

# 6\. Scholarly Research

# 7\. Linguistic Evidence

# 8\. Comparative Evidence

# 9\. Scientific Analysis

# 

# \---

# 

# \## Database Architecture

# 

# The project uses SQLite and follows a relational database design.

# 

# \### Core Tables

# 

# \* `evidence`

# \* `sources`

# \* `references\_data`

# \* `evidence\_quality`

# 

# \### Classification Tables

# 

# \* `fields`

# \* `evidence\_fields`

# \* `evidence\_types`

# \* `historical\_periods`

# 

# \### People, Places and Texts

# 

# \* `people`

# \* `places`

# \* `evidence\_people`

# \* `evidence\_places`

# \* `texts`

# \* `verses`

# \* `evidence\_texts`

# 

# \### Contribution Analysis

# 

# \* `contributions`

# 

# The complete database structure is represented in:

# 

# `Bharat\_Knowledge\_Evidence\_ER\_Diagram.png`

# 

# \---

# 

# \## Evidence Structure

# 

# Each evidence record can contain:

# 

# \* Topic

# \* Claim

# \* Evidence type

# \* Historical period

# \* Location

# \* Description

# \* Source

# \* Related knowledge field

# \* Related people

# \* Related places

# \* Related texts

# \* Quality and verification information

# \* Supporting references

# 

# This structure allows the database to connect a claim with the evidence and sources supporting it.

# 

# \---

# 

# \## Reference and Verification System

# 

# References contain structured metadata such as:

# 

# \* Reference text

# \* Page or verse

# \* URL

# \* Author

# \* Work

# \* Edition

# \* Publisher

# \* Publication year

# \* Volume

# \* Page

# \* Book

# \* Chapter

# \* Verse

# \* Original language

# \* Translation

# \* Translator

# \* Scholarly reference

# \* Primary source URL

# \* Scholarly source URL

# \* Verification status

# \* Verification notes

# \* Source reliability

# \* Citation verification

# 

# The database does not assume that every claim is automatically proven simply because a source mentions it.

# 

# Primary-source resources and scholarly interpretations are recorded separately where appropriate.

# 

# \---

# 

# \## Data Quality Checks

# 

# The database has undergone structural quality checks.

# 

# \### Completed Checks

# 

# \* Every evidence record has at least one reference.

# \* Every reference has at least one URL.

# \* No exact duplicate evidence claims were detected.

# \* No orphan relationship records were detected.

# \* SQLite database integrity check passed.

# \* Foreign-key validation passed.

# \* Evidence records contain required core fields.

# \* Source reliability information is populated.

# \* Reference verification metadata was cleaned.

# \* Database backup was created before final cleanup.

# 

# \---

# 

# \## Source Philosophy

# 

# The project aims to preserve a distinction between:

# 

# \### Primary-Source Resources

# 

# Examples include:

# 

# \* Digitized Sanskrit texts

# \* Manuscripts

# \* Inscriptions

# \* Archaeological records

# \* Historical documents

# 

# \### Scholarly Sources

# 

# Examples include:

# 

# \* Peer-reviewed research

# \* Academic books

# \* University resources

# \* Scholarly databases

# \* Research publications

# 

# A scholarly source may discuss or interpret a historical claim without itself being the original historical source.

# 

# \---

# 

# \## Example Research Areas

# 

# The current dataset includes evidence related to areas such as:

# 

# \* Indian mathematics

# \* Zero and decimal place-value systems

# \* Astronomy

# \* Trigonometric traditions

# \* Sanskrit grammar

# \* Paninian linguistic analysis

# \* Ayurveda

# \* Surgery

# \* Yoga

# \* Vedic textual traditions

# \* Kerala mathematical traditions

# \* Ancient educational institutions

# \* Indian scientific and intellectual traditions

# 

# \---

# 

# \## Technology Stack

# 

# \* \*\*Database:\*\* SQLite

# \* \*\*Language:\*\* Python

# \* \*\*Data Processing:\*\* Python / SQL

# \* \*\*Database Analysis:\*\* SQLite

# \* \*\*ER Diagram:\*\* Mermaid

# \* \*\*Documentation:\*\* Markdown

# \* \*\*Future Analysis:\*\* Power BI / Python / SQL

# 

# \---

# 

# \## Project Files

# 

# Important project files include:

# 

# ```text

# bharat\_knowledge.db

# bharat\_knowledge\_er\_diagram.mmd

# Bharat\_Knowledge\_Evidence\_ER\_Diagram.png

# README.md

# ```

# 

# The project also contains Python scripts used for database creation, auditing, cleaning, and analysis.

# 

# \---

# 

# \## Database Usage

# 

# The database can be opened using SQLite-compatible tools.

# 

# \### Open the database

# 

# ```bash

# sqlite3 bharat\_knowledge.db

# ```

# 

# \### View evidence records

# 

# ```sql

# SELECT \*

# FROM evidence

# LIMIT 10;

# ```

# 

# \### Count evidence records

# 

# ```sql

# SELECT COUNT(\*)

# FROM evidence;

# ```

# 

# \### View references

# 

# ```sql

# SELECT \*

# FROM references\_data

# LIMIT 10;

# ```

# 

# These commands are examples for future users of the database.

# 

# \---

# 

# \## Data Expansion

# 

# The database is designed to support future expansion.

# 

# Possible future additions include:

# 

# \* More evidence records

# \* More primary-text passages

# \* More archaeological evidence

# \* More inscriptions

# \* More historical periods

# \* More people and places

# \* More scholarly references

# \* More precise page/verse citations

# \* Additional knowledge fields

# \* Multilingual translations

# \* Evidence scoring and confidence analysis

# \* Search and filtering interfaces

# 

# \---

# 

# \## Future Data Analytics

# 

# The dataset can later be used for:

# 

# \* Evidence distribution by field

# \* Evidence distribution by historical period

# \* Source reliability analysis

# \* Citation coverage analysis

# \* Primary vs scholarly source analysis

# \* Geographic visualization

# \* Timeline analysis

# \* Knowledge-field relationships

# \* Network analysis of people, texts, places and evidence

# \* Interactive dashboards

# 

# \---

# 

# \## Data Integrity

# 

# The final database audit confirmed:

# 

# \*\*SQLite Integrity:\*\* PASS

# 

# \*\*Foreign Keys:\*\* PASS

# 

# \*\*Evidence → Reference Coverage:\*\* PASS

# 

# \*\*Reference → URL Coverage:\*\* PASS

# 

# \*\*Duplicate Claim Check:\*\* PASS

# 

# \*\*Orphan Relationship Check:\*\* PASS

# 

# \---

# 

# \## Important Research Note

# 

# Historical interpretation can involve uncertainty, different scholarly reconstructions, and debates about chronology or attribution.

# 

# Therefore, the database records source and verification information alongside claims rather than treating every historical interpretation as equally established.

# 

# The project is intended as a structured research and data-analysis resource. Individual claims should be evaluated using their cited primary sources and scholarly literature.

# 

# \---

# 

# \## License

# 

# License information can be added when the project's data, source usage, and redistribution requirements have been finalized.

# 

# \---

# 

# \## Author

# 

# \*\*Boggavarapu Mahesh\*\*

# 

# MSc Data Analytics

# Berlin School of Business \& Innovation (BSBI), Germany



