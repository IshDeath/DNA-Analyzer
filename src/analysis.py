import sqlite3
from src.utils import get_db_connection

def get_snps_by_chromosome(chromosome):
    """Fetches all SNPs from a specific chromosome."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT rsid, position, allele1, allele2 FROM snp_data WHERE chromosome = ?", (chromosome,))
    snps = cursor.fetchall()
    
    conn.close()
    return snps

def get_heterozygous_snps():
    """Fetches all SNPs where allele1 ≠ allele2 (heterozygous)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT rsid, chromosome, position, allele1, allele2 FROM snp_data WHERE allele1 != allele2")
    snps = cursor.fetchall()
    
    conn.close()
    return snps
