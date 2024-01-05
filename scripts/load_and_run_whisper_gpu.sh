git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp
bash ./models/download-ggml-model.sh base
make clean
WHISPER_CUBLAS=1 make -j
# To run on one sample 
./main -m models/ggml-base.bin -f ../../data/intermediate/spanish/Language\ Transfer\ -\ Complete\ Spanish\ -\ Lesson\ 02.wav 