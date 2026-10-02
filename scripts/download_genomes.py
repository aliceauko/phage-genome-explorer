from Bio import Entrez
from Bio import SeqIO
from pathlib import Path

# NCBI settings

Entrez.email = "aukoalice@gmail.com"

# Search NCBI

query = (
    '"Staphylococcus phage"[Title] '
    'AND "complete genome"[Title] '
    'AND viruses[filter] '
    'AND refseq[filter]'
)

print("Searching NCBI...")

handle = Entrez.esearch(
    db="nuccore",
    term=query,
    retmax=500
)

search_results = Entrez.read(handle)
handle.close()

ids = search_results["IdList"]

print(f"Records found: {len(ids)}")

# Create output directory
output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "staphylococcus_phages.gb"

# Download GenBank record
print("Downloading records from NCBI...")

handle = Entrez.efetch(
    db="nuccore",
    id=",".join(ids),
    rettype="gb",
    retmode="text"
)

with open(output_file, "w") as file:
    file.write(handle.read())

handle.close()

# Verify downloaded records
records = list(SeqIO.parse(output_file, "genbank"))

print(f"Genomes downloaded: {len(records)}")
print(f"Saved to: {output_file}")