import codecs, os, sys

if __name__ == "__main__":

	# Splitting source and target
	file_name = sys.argv[1]
	f = codecs.open(file_name, encoding="utf-8").readlines()
	sr_f = open("source_corpus.txt", "w")
	tr_f = open("target_corpus.txt", "w")
	for a in range(len(f)):
		line = f[a].replace("\n", "").split('\t')
		line_str = line[0] + "\n"
		sr_f.write(line_str.encode("utf-8"))
		line_str = line[1] + "\n"
		tr_f.write(line_str.encode("utf-8"))
	sr_f.close()
	tr_f.close()

	# Tokenizing source and target
	os.system("tokenizer/tokenizer.perl < source_corpus.txt > tokenized_source_corpus.txt")
	os.system("tokenizer/tokenizer.perl < target_corpus.txt > tokenized_target_corpus.txt")

	# Last preparations for aligning
	sr_f = codecs.open("tokenized_source_corpus.txt", encoding="utf-8").readlines()
	tr_f = codecs.open("tokenized_target_corpus.txt", encoding="utf-8").readlines()
	l_f = open("corpus.txt", "w")
	for b in range(len(sr_f)):
		line = sr_f[b].replace("\n", "")
		line += " ||| "
		line += tr_f[b].replace("\n", "") + '\n'
		l_f.write(line.encode("utf-8"))
	l_f.close()
	os.system("mv tokenized_source_corpus.txt source.txt")
	os.system("mv tokenized_target_corpus.txt target.txt")
	os.system("rm source_corpus.txt target_corpus.txt")
