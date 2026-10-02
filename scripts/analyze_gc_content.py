import pandas as pd
import matplotlib.pyplot as plt

# Load metadata
df = pd.read_csv("data/processed/phage_genome_metadata.csv")

# Summary statistics
print("=== GC CONTENT SUMMARY ===")
print(df["gc_percent"].describe())

# Plot distribution
plt.figure(figsize=(8, 5))

plt.hist(df["gc_percent"], bins=15)

plt.xlabel("GC content (%)")
plt.ylabel("Number of phages")
plt.title("GC Content Distribution of Staphylococcus Phages")

plt.tight_layout()

plt.savefig(
    "results/figures/gc_content_distribution.png",
    dpi=300
)

plt.show()