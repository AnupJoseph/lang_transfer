import sys
import zipfile
import os
import tempfile
from tqdm import tqdm

from pathlib import Path


def extract_zipfile(infile: str, outfolder: str = "./data/intermediate/spanish"):
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)

    tempdir = tempfile.TemporaryDirectory(delete=False)
    with zipfile.ZipFile(infile, "r") as zip_ref:
        zip_ref.extractall(tempdir.name)

    mp3s = [i.name for i in Path(tempdir.name).glob("*.mp3")]
    wavs = [f"{i.replace('mp3','wav')}" for i in mp3s]

    for wav, mp3 in tqdm(zip(wavs, mp3s), total=len(mp3s)):
        os.system(f'ffmpeg -i "{tempdir.name}/{mp3}" -ar 16000 "{outfolder}/{wav}"')
    tempdir.cleanup()


def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Arguments error. Usage:\n")
        sys.stderr.write("\tpython prepare.py zip/file/path outfolder/path\n")
        sys.exit(1)

    zipfile_path = sys.argv[1]
    outfolder_path = "data/intermediate/" + zipfile_path.split("/")[-1].split(".")[0]
    extract_zipfile(zipfile_path, outfolder_path)


main()
