import sys
import zipfile
import os


def extract_zipfile(infile: str, outfolder: str = "./data/intermediate"):
    if not os.path.exists(infile):
        os.makedirs(outfolder)
    with zipfile.ZipFile(infile, "r") as zip_ref:
        zip_ref.extractall(outfolder)


def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Arguments error. Usage:\n")
        sys.stderr.write("\tpython prepare.py zip/file/path outfolder/path\n")
        sys.exit(1)

    zipfile_path = sys.argv[1]
    outfolder_path = "data/intermediate/" + zipfile_path.split("/")[-1].split(".")[0]
    extract_zipfile(zipfile_path, outfolder_path)


main()
