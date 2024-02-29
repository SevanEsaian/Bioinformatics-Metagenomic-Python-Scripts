import re
import sys
import os

def main():
    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("usage: python parse_dbcan_gff.py prodigal.gff")
        sys.exit(1)

    # Input filename and directory
    input_filename = sys.argv[1]
    input_directory = os.path.dirname(input_filename)

    # Output filename and directory
    output_filename = os.path.join(input_directory, "mature_bin.47_dbcan_geneious.gff")

    try:
        with open(input_filename, 'r') as f_in, open(output_filename, 'w') as f_out:
            for line in f_in:
                if line.startswith('#'):
                    f_out.write(line)
                else:
                    match = re.search(r'(^k[0-9]+_[0-9]+)', line)
                    if match:
                        contig = "\tID=" + match.group(1) + "_"
                        newline = re.sub(r'\tID=[0-9]+_', contig, line)
                        f_out.write(newline)
                    else:
                        print("contig names too different, fix regex")
                        sys.exit(1)
    except IOError as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
