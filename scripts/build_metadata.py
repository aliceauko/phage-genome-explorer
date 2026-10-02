from Bio import SeqIO
from pathlib import Path
import pandas as pd

# --------------------------------------------------
# Input and output files
# --------------------------------------------------

input_file = Path("data/raw/staphylococcus_phages.gb")
output_file = Path("data/processed/phage_genome_metadata.csv")

# Create output directory if needed
output_file.parent.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Extract metadata
# --------------------------------------------------

records = []

for record in SeqIO.parse(input_file, "genbank"):

    cds_count = sum(
        1 for feature in record.features
        if feature.type == "CDS"
    )

    trna_count = sum(
        1 for feature in record.features
        if feature.type == "tRNA"
    )

    records.append({
        "phage_name": record.description,
        "accession": record.id,
        "genome_length_bp": len(record.seq),
        "gc_percent": round(
            100 * (
                (record.seq.count("G") + record.seq.count("C"))
                / len(record.seq)
            ),
            2
        ),
        "topology": record.annotations.get("topology", "unknown"),
        "cds_count": cds_count,
        "trna_count": trna_count
    })

# --------------------------------------------------
# Create metadata table
# --------------------------------------------------

df = pd.DataFrame(records)

df.to_csv(output_file, index=False)

# --------------------------------------------------
# Verification
# --------------------------------------------------

print(f"Genomes processed: {len(df)}")
print(f"Metadata saved to: {output_file}")
print()
print(df.head())