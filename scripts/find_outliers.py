import pandas as pd

df = pd.read_csv("data/processed/phage_genome_metadata.csv")

# Largest and smallest genomes
print("=== SMALLEST GENOMES ===")
print(
    df.nsmallest(5, "genome_length_bp")[
        ["phage_name", "accession", "genome_length_bp", "gc_percent", "cds_count"]
    ]
)

print("\n=== LARGEST GENOMES ===")
print(
    df.nlargest(5, "genome_length_bp")[
        ["phage_name", "accession", "genome_length_bp", "gc_percent", "cds_count"]
    ]
)

# Lowest and highest GC
print("\n=== LOWEST GC CONTENT ===")
print(
    df.nsmallest(5, "gc_percent")[
        ["phage_name", "accession", "genome_length_bp", "gc_percent", "cds_count"]
    ]
)

print("\n=== HIGHEST GC CONTENT ===")
print(
    df.nlargest(5, "gc_percent")[
        ["phage_name", "accession", "genome_length_bp", "gc_percent", "cds_count"]
    ]
)