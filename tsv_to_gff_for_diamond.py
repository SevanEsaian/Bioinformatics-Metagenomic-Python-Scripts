import os

input_file = "/home/sevan/MasterList_dereplicated_bins_biopython_aminoacid_conversion/diamond_blastp/ALL_bin.1_diamond_uniprot_annotation.tsv"
output_dir = "/home/sevan/MasterList_dereplicated_bins_biopython_aminoacid_conversion/diamond_blastp/"
output_file = os.path.join(output_dir, "diamond_uniprot_annotation.gff")

with open(input_file, 'r') as tsvfile, open(output_file, 'w') as gfffile:
    for line in tsvfile:
        fields = line.strip().split('\t')
        seqid = fields[0]
        source = 'DIAMOND'
        feature = 'BLAST_hit'
        start = fields[7]
        end = fields[8]
        score = fields[11]
        strand = '.'
        attributes = f"ID={fields[1]};E-value={fields[10]}"

        # Check if start and end positions are numeric
        if not start.isdigit() or not end.isdigit():
            print("Warning: Start or end position is not numeric.")
            continue

        gfffile.write(f"{seqid}\t{source}\t{feature}\t{start}\t{end}\t{score}\t{strand}\t.\t{attributes}\n")
