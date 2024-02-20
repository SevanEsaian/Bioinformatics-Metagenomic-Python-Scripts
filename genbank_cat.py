import os
from Bio import SeqIO

# Directory containing subdirectories with genbank files
parent_dir = '/home/sevan/Metagenomes/Thioahlocapsa_PSB'

# Loop through each subdirectory
for subdir in os.listdir(parent_dir):
    sub_path = os.path.join(parent_dir, subdir)
    
    # Check if it's a directory
    if os.path.isdir(sub_path):
        output_filename = f'{subdir}_antismash_allmerged.gbk'
        output_path = os.path.join(sub_path, output_filename)
        
        # Initialize an empty list to store SeqRecords
        merged_records = []
        
        # Loop through each genbank file starting with "c"
        for filename in os.listdir(sub_path):
            if filename.startswith('c') and filename.endswith('.gbk'):
                file_path = os.path.join(sub_path, filename)
                
                # Read the genbank file and append its records
                with open(file_path, 'r') as gbk_file:
                    records = SeqIO.parse(gbk_file, 'genbank')
                    merged_records.extend(records)
        
        # Write the merged records to the output genbank file
        with open(output_path, 'w') as output_file:
            SeqIO.write(merged_records, output_file, 'genbank')
