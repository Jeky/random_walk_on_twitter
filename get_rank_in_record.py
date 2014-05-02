import data
import rank
import rw
from utils import *
from collections import Counter

STEP_IN_PIECE = 1000000
RW_PIECE_NAME = data.RW_PATH + 'rw.%d.txt'

tid = rank.getRank(1)[0]
size = 5000

steps = []

out = open('rank-1.txt', 'w')

print 'tid of rank 1: ', tid

for i in range(rw.getRwFileCount()):
	rwpiece = open(RW_PIECE_NAME % i)
	print 'reading', RW_PIECE_NAME % i

	for l in rwpiece.xreadlines():
		tid, tag = l.strip().split('\t')
		steps.append(int(tid))

		if len(steps) == size:
			rank = 0
			counter = Counter(steps)
			for i, item in enumerate(counter.most_common()):
				if item[0] == tid:
					rank = i + 1
					break

			out.write('%d\n' % rank)

			steps = []

	rwpiece.close()

out.close()