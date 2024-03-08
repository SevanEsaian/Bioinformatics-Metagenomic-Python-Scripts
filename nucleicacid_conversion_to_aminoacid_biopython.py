import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def translate_nucleic_to_amino(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over each FASTA file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".fasta"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename.replace(".fasta", "_amino.fasta"))
            with open(input_file, "r") as input_handle, open(output_file, "w") as output_handle:
                for record in SeqIO.parse(input_handle, "fasta"):
                    nucleotide_sequence = record.seq
                    amino_sequence = nucleotide_sequence.translate(table=1)  # Translating using the standard genetic code
                    amino_record = SeqRecord(amino_sequence, id=record.id, description=record.description)
                    SeqIO.write(amino_record, output_handle, "fasta")

# Input and output directory paths
input_directory = "/home/sevan/bins_dRep_masterlist_11142023"
output_directory = "/home/sevan/bins_dRep_masterlist_11142023_amino"

# Translate nucleic acid to amino acid sequences
translate_nucleic_to_amino(input_directory, output_directory)
