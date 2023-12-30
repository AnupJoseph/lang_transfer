# Lang Transfer


### Setup

Ok, so might be the setup for this is unecessarily complex. Anyway, install all dependencies in `requirements.txt`.

* Go to the dagshub URL and setup credentials with the steps [here](https://dagshub.com/AnupJoseph/lang_transfer)
* Afterwards run `dvc pull` from root directory
* Then run `dvc repro` to unzip the files and convert them from `mp3` to `wav`
* Follow steps at `./scripts/load_and_run_whisper.sh` to run Whisper on one of the samples for transcription