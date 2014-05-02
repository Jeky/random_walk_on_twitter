import data
import rank
import rw
from utils import *
from collections import Counter

STEP_IN_PIECE = 1000000
RW_PIECE_NAME = data.RW_PATH + 'rw.%d.txt'

tid = '19058681'
size = 5000

steps = []

out = open('rank-1.txt', 'w')

fin = open(data.PATH + 'rw.50m.txt')

print 'tid of rank 1: ', tid
for i, l in enumerate(fin.xreadlines()):
	if i % 1000000 == 0:
		print i
	tid, tag = l.strip().split('\t')
	steps.append(tid)

	if len(steps) == size:
		rank = 0
		count = 0
		counter = Counter(steps)
		for r, item in enumerate(counter.most_common(100)):
			if item[0] == tid:
				rank = r + 1
				count = item[1]
				break

		out.write('%d\t%d\n' % (rank, count))

		steps = []

fin.close()
out.close()