import sqlite3

DB_FILE = "data/dna_data.db"

def get_db_connection():
    """Returns a database connection."""
    return sqlite3.connect(DB_FILE)
