import pandas as pd
import matplotlib.pyplot as plt

# Load metadata
df = pd.read_csv("data/processed/phage_genome_metadata.csv")

# Summary statistics
print("=== GENOME SIZE SUMMARY ===")
print(df["genome_length_bp"].describe())

# Plot distribution
plt.figure(figsize=(8, 5))

plt.hist(df["genome_length_bp"], bins=20)

plt.xlabel("Genome size (bp)")
plt.ylabel("Number of phages")
plt.title("Genome Size Distribution of Staphylococcus Phages")

plt.tight_layout()

plt.savefig(
    "results/figures/genome_size_distribution.png",
    dpi=300
)

plt.show()