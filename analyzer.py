from Bio import SeqIO
import csv

def calculate_gc(seq):
    g = seq.count("G")
    c = seq.count("C")
    return round(((g + c) / len(seq)) * 100, 2)

records = list(SeqIO.parse("data/sample.fasta", "fasta"))

results = []

for record in records:
    seq = str(record.seq)
    results.append({
        "Sequence_ID": record.id,
        "Length": len(seq),
        "GC_Content(%)": calculate_gc(seq)
    })

# Write output to CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"Total sequences: {len(results)}")
print("Analysis complete. Results saved to output.csv")
