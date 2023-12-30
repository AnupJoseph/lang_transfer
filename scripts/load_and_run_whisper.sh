git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp
bash ./models/download-ggml-model.sh base
make
# To run on one of our samples 
./main -m models/ggml-base.bin -f ../../data/intermediate/spanish/Language\ Transfer\ -\ Complete\ Spanish\ -\ Lesson\ 02.wav 