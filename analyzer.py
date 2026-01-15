import os
from Bio import SeqIO
import csv

# --- Get the absolute path to this script ---
base_dir = os.path.dirname(os.path.abspath(__file__))

# --- Full path to the FASTA file ---
fasta_file = os.path.join(base_dir, "data", "sample.fasta")

# --- Read sequences ---
try:
    records = list(SeqIO.parse(fasta_file, "fasta"))
except FileNotFoundError:
    print(f"ERROR: Could not find {fasta_file}")
    exit(1)

# --- Analyze sequences ---
results = []

def calculate_gc(seq):
    g = seq.count("G")
    c = seq.count("C")
    return round(((g + c) / len(seq)) * 100, 2)

for record in records:
    seq = str(record.seq)
    results.append({
        "Sequence_ID": record.id,
        "Length": len(seq),
        "GC_Content(%)": calculate_gc(seq)
    })

# --- Write output CSV ---
output_file = os.path.join(base_dir, "output.csv")
with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

