import string
import sys
import pyminizip

n_of_cli_args = len(sys.argv)

if n_of_cli_args < 4:
    print("Number of CLI arguments mismatches 3")
    print("Required arguments are: sourceFile targetfile(zip) password")

src_file = sys.argv[1]
prefix = None
target_file_zip = sys.argv[2]
password = sys.argv[3]


pyminizip.compress(src_file, prefix, target_file_zip, password, 5)

