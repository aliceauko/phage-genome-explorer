import pandas as pd
import matplotlib.pyplot as plt

# Load metadata
df = pd.read_csv("data/processed/phage_genome_metadata.csv")

# Plot genome size vs GC content
plt.figure(figsize=(8, 5))

plt.scatter(
    df["genome_length_bp"],
    df["gc_percent"]
)

plt.xlabel("Genome size (bp)")
plt.ylabel("GC content (%)")
plt.title("Genome Size vs GC Content of Staphylococcus Phages")

plt.tight_layout()

plt.savefig(
    "results/figures/genome_size_vs_gc.png",
    dpi=300
)

plt.show()