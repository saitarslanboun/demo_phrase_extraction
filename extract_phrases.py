from __future__ import division
from collections import defaultdict

import codecs

if __name__ == "__main__":
	f = codecs.open("phrase_table.txt", encoding="utf-8").readlines()
	xy_alignments = defaultdict(int)
	yx_alignments = defaultdict(int)
	x_phrases = defaultdict(int)
	y_phrases = defaultdict(int)
	of = open("phrase_pairs.txt", "w")

	for a in range(len(f)):
		if (a+1) % 1000 == 0: print "Line " + str(a+1)
		x, y = f[a].strip().split("\t")
		xy_alignments[(x,y)] += 1
		yx_alignments[(y,x)] += 1
		x_phrases[x] += 1
		y_phrases[y] += 1

	len_alignments = len(xy_alignments.keys())
	xy_alignment_keys = xy_alignments.keys()

	for b in range(len_alignments):
		if (b+1) % 1000 == 0: print "Line " + str(b+1)
                x = xy_alignment_keys[b][0]
                y = xy_alignment_keys[b][1]
                yx_prob = yx_alignments[(y,x)] / x_phrases[x]
                xy_prob = xy_alignments[(x,y)] / y_phrases[y]
                line_str = x + "\t" + y + "\t" + str(yx_prob) + "\t" + str(xy_prob) + "\n"
                of.write(line_str.encode("utf-8"))
        of.close()
