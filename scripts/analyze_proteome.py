import pandas as pd
import sys
from Bio import SeqIO

fasta_file = sys.argv[1]

lengths = []
ids = []

for record in SeqIO.parse(fasta_file, "fasta"):
    ids.append(record.id)
    lengths.append(len(record.seq))

df = pd.DataFrame({
    "protein_id": ids,
    "length": lengths
})

print("Number of proteins:", len(df))
print("Average length:", df["length"].mean())

for record in SeqIO.parse(fasta_file, "fasta"):
    print(record.id)
    print(len(record.seq))
    break

df.to_csv("N:\Jupiter_Projects\enzyme-genome-mining-course/results/protein_lengths.csv", index=False)