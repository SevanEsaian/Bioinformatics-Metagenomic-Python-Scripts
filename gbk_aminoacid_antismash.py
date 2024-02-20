from Bio import SeqIO
import os

# Directory containing GenBank files
directory = "/home/sevan/Metagenomes/Thiohalocapsa_PSB/Gbk_For_Phylogenetic_Tree"

# Output FASTA file name
output_fasta_file = "output.fasta"

# Open the output FASTA file for writing
with open(output_fasta_file, "w") as fasta_output:

    # Loop through GenBank files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".gbk"):
            # Construct the full file path
            file_path = os.path.join(directory, filename)

            # Parse the GenBank file
            for record in SeqIO.parse(file_path, "genbank"):
                # Look for features of type "PFAM_domain"
                for feature in record.features:
                    if feature.type == "PFAM_domain":
                        # Extract the relevant information
                        aSDomain = feature.qualifiers.get("aSDomain", ["Unknown"])[0]
                        translation = str(feature.qualifiers.get("translation", [""]))[2:-2].replace("\\n", "")
                        
                        # Create the FASTA header with file name and aSDomain
                        fasta_header = f">{filename} asDomain={aSDomain}"
                        
                        # Write the header and sequence to the output file
                        fasta_output.write(fasta_header + "\n" + translation + "\n")

print("FASTA file generation complete.")
