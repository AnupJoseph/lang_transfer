dvc stage add -n prepare  -d src/dataset_utils.py -d data/raw/spanish.zip python src/dataset_utils.py data/raw/spanish.zip

stages:
  prepare:
    cmd: python src/dataset_utils.py data/raw/spanish.zip
    deps:
    - data/raw/spanish.zip
    - src/dataset_utils.py
