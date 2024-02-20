from Bio import SeqIO
import os

# Input merged GBK file
input_file = "/home/sevan/Metagenomes/Thiohalocapsa_PSB/antismashoutput_Thiohalocapsa_PP7_B5_4/Thiohalocapsa_PP7_B5_4_antismash_allmerged.gbk"

# Output FASTA file
output_file = "/home/sevan/Metagenomes/Thiohalocapsa_PSB/antismashoutput_Thiohalocapsa_PP7_B5_4/PP7_B5_4_PFAM_sequences.fasta"

# Open the output FASTA file for writing
with open(output_file, 'w') as fasta_out:
    # Parse the merged GBK file
    records = SeqIO.parse(input_file, "genbank")
    
    for record in records:
        for feature in record.features:
            if feature.type == "PFAM_domain":
                # Extract PFAM domain information
                pfam_domain = feature.qualifiers.get("aSDomain", ["Unknown"])[0]
                pfam_domain = pfam_domain.replace(" ", "_")  # Replace spaces with underscores
                
                # Extract the translation sequence
                sequence = feature.qualifiers.get("translation", [""])[0]
                if sequence:
                    # Write to FASTA file
                    fasta_out.write(f">{pfam_domain}_PP7_B5_4\n{sequence}\n")

print("PFAM domain sequences have been written to", output_file)
