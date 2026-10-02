import pandas as pd

input_file = "data/processed/phage_genome_metadata.csv"

df = pd.read_csv(input_file)

print("=== DATASET QC ===")
print(f"Number of genomes: {len(df)}")
print(f"Number of variables: {len(df.columns)}")

print("\n=== Missing values ===")
print(df.isna().sum())

print("\n=== Duplicate accessions ===")
print(df["accession"].duplicated().sum())

print("\n=== Genome length ===")
print(f"Minimum: {df['genome_length_bp'].min():,} bp")
print(f"Maximum: {df['genome_length_bp'].max():,} bp")

print("\n=== GC content ===")
print(f"Minimum: {df['gc_percent'].min():.2f}%")
print(f"Maximum: {df['gc_percent'].max():.2f}%")

print("\n=== Topology ===")
print(df["topology"].value_counts())

print("\n=== QC complete ===")