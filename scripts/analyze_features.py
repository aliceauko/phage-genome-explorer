import pandas as pd
import matplotlib.pyplot as plt

# Load metadata
df = pd.read_csv("data/processed/phage_genome_metadata.csv")

# --------------------------------------------------
# CDS count
# --------------------------------------------------

print("=== CDS COUNT SUMMARY ===")
print(df["cds_count"].describe())

# --------------------------------------------------
# tRNA count
# --------------------------------------------------

print("\n=== tRNA COUNT SUMMARY ===")
print(df["trna_count"].describe())

# --------------------------------------------------
# Topology
# --------------------------------------------------

print("\n=== GENOME TOPOLOGY ===")
print(df["topology"].value_counts())

# --------------------------------------------------
# CDS count distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["cds_count"], bins=20)

plt.xlabel("Number of CDS")
plt.ylabel("Number of phages")
plt.title("CDS Count Distribution of Staphylococcus Phages")

plt.tight_layout()

plt.savefig(
    "results/figures/cds_count_distribution.png",
    dpi=300
)

plt.show()

# --------------------------------------------------
# tRNA count distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["trna_count"], bins=10)

plt.xlabel("Number of tRNAs")
plt.ylabel("Number of phages")
plt.title("tRNA Count Distribution of Staphylococcus Phages")

plt.tight_layout()

plt.savefig(
    "results/figures/trna_count_distribution.png",
    dpi=300
)

plt.show()