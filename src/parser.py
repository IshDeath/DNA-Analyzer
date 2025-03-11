from src.utils import get_db_connection

# File paths
INPUT_FILE = "data/example_dna.txt"

def create_database():
    """Creates the SQLite database and the snp_data table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS snp_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rsid TEXT UNIQUE,
            chromosome INTEGER,
            position INTEGER,
            allele1 TEXT,
            allele2 TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def parse_and_store_dna_data():
    """Reads the DNA text file and inserts SNP data into the SQLite database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    with open(INPUT_FILE, "r") as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            # Ignore comment lines
            if line.startswith("#"):
                continue
            
            # Skip the header row
            if "rsid" in line.lower():
                continue

            # Split by tab
            columns = line.strip().split("\t")
            if len(columns) == 5:
                rsid, chromosome, position, allele1, allele2 = columns

                try:
                    cursor.execute('''
                        INSERT OR IGNORE INTO snp_data (rsid, chromosome, position, allele1, allele2)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (rsid, int(chromosome), int(position), allele1, allele2))
                except Exception as e:
                    print(f"Error inserting {rsid}: {e}")

    conn.commit()
    conn.close()
    print("DNA data successfully stored in SQLite database.")

if __name__ == "__main__":
    create_database()
    parse_and_store_dna_data()
