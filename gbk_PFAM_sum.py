import os
import csv
from Bio import SeqIO

# Directory containing GenBank files
directory = '/home/sevan/Metagenomes/Thiohalocapsa_PSB/Gbk_For_Phylogenetic_Tree'

# Output CSV file
output_csv = '/home/sevan/Metagenomes/Thiohalocapsa_PSB/cds_counts.csv'

# Initialize a list to store results
results = []

# Iterate through each GenBank file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".gbk"):
        file_path = os.path.join(directory, filename)
        
        # Initialize the count for this file
        count = 0
        
        # Parse the GenBank file and count "CDS" features
        for record in SeqIO.parse(file_path, "genbank"):
            for feature in record.features:
                if feature.type == 'CDS':
                    count += 1
        
        # Append the result to the list
        results.append((filename, count))

# Write the results to a CSV file
with open(output_csv, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(['GenBank File', 'CDS Count'])
    
    # Write the data
    csv_writer.writerows(results)

print(f"CDS counts have been written to {output_csv}")
