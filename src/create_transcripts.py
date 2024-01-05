#before running this file:
# Run either run load_and_whisper.sh or load_and_whisper_gpu.sh

import sys
from pathlib import Path
import os


def transcribe():
    wav_folder = "../data/intermediate/spanish"
    outfolder = "../data/transcripts/spanish"
    wavs_files = [i.name for i in Path(wav_folder).glob("*.wav")]
    csv_files = [i.replace("wav","csv") for i in wavs_files]
#     print(wavs_files)
    for wav,csv in zip(wavs_files,csv_files):
#         print(wav)
        os.system(f"./main -m models/ggml-small.bin -t 8 -p 4 -ocsv '{wav_folder}/{wav}' -of '{outfolder}/{csv}'")

transcribe()