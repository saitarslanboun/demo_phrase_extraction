import codecs, os

from collections import defaultdict

def arrange_alignments(alignments):
	cells = alignments.strip().split()
	sr_alignments = defaultdict(list)
	tr_alignments = defaultdict(list)
	for a in range(len(cells)):
		a1, a2 = cells[a].split("-")
		sr_alignments[a1].append(a2)
		tr_alignments[a2].append(a1)

	alignments = (sr_alignments, tr_alignments)
	return alignments

def check_alignments(source_pair, target_pair, alignments):
	source_pair = map(unicode, source_pair)
	target_pair = map(unicode, target_pair)
	sr_alignments = alignments[0]
	tr_alignments = alignments[1]
	for a in range(len(source_pair)):
		if not set(sr_alignments[str(source_pair[a])]).issubset(target_pair):
			return False
	for b in range(len(target_pair)):
		if not set(tr_alignments[str(target_pair[b])]).issubset(source_pair):
			return False

	return True

if __name__ == "__main__":
	alignments = codecs.open("corpus.align", encoding="utf-8").readlines()
	sources = codecs.open("source.txt", encoding="utf-8").readlines()
	targets = codecs.open("target.txt", encoding="utf-8").readlines()
	phrase_table = open("phrase_table.txt", "w")
	phrases = defaultdict(int)
	for a in range(len(sources)):
		if (a+1) % 1000 == 0:
			print "Line " + str(a+1)
		source_words = sources[a].strip().split()
		target_words = targets[a].strip().split()
		current_alignments = arrange_alignments(alignments[a])
		for b in xrange(1, len(source_words)+1):
			for c in range(len(source_words) - b + 1):
				source_pair = range(b-1,c+b)
				for d in xrange(1, len(target_words)+1):
					for e in range(len(target_words) - d + 1):
						target_pair = range(d-1,e+d)
						if check_alignments(source_pair, target_pair, current_alignments):
							sr_pair = " ".join([source_words[i] for i in source_pair])
							tr_pair = " ".join([target_words[i] for i in target_pair])
							line_str = sr_pair + "\t" + tr_pair + "\n"
							phrase_table.write(line_str.encode("utf-8"))

	phrase_table.close()

