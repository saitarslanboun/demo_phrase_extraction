
# Downloading corpus
echo "Downloading corpus ..."
#corpus_dir="http://www.manythings.org/anki/tur-eng.zip" # Turkish - English sentence pairs corpus from Tatoeba Project
#corpus_dir="http://www.manythings.org/anki/est-eng.zip" # Estonian - English sentence pairs corpus from Tatoeba Project
corpus_dir="http://www.manythings.org/anki/rus-eng.zip" # Russian - English sentence pairs corpus from Tatoeba Project
wget $corpus_dir

# Preparing corpus
echo "Preparing corpus ..."
unzip ${corpus_dir: -11}
rm "_about.txt"
rm ${corpus_dir: -11}
python data-prep.py ${corpus_dir: -11:-8}.txt

# Aligning sentence pairs
echo "Aligning sentence pairs in corpus ..."
fast_align_dir="fast_align/build" # Chris Dyer's fast_align alignment tool directory path
./$fast_align_dir/fast_align -i corpus.txt -d -o -v > corpus.align

# Extracting aligned words
echo "Extracting aligned words ..."
python extract_alignments.py

# Extacting phrase pairs
echo "Exctracting phrase pairs ..."
python extract_phrases.py
