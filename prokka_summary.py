import os
import glob
from Bio import SeqIO

def count_genes_per_bin(folder_path):
    output_file = "/home/sevan/Dereplicated_Coassemblies/gene_counts_per_bin.txt"

    with open(output_file, "w") as out_f:
        out_f.write("Bin\tGene_Count\n")

        gff_files = glob.glob(os.path.join(folder_path, "*_annotation", "*.gff"))
        for gff_file in gff_files:
            bin_label = os.path.basename(gff_file).split(".")[0]

            gene_count = 0
            with open(gff_file) as gff_f:
                for record in SeqIO.parse(gff_f, "genbank"):
                    for feature in record.features:
                        if feature.type == "CDS":
                            gene_count += 1

            out_f.write(f"{bin_label}\t{gene_count}\n")

def main():
    folder_path = "/home/sevan/Dereplicated_Coassemblies/Juvenile"
    count_genes_per_bin(folder_path)

if __name__ == "__main__":
    main()
