import rank
import rw
from collections import Counter

fout = open('rank-1.txt', 'w')
steps = rw.readSteps()
size = len(steps) / 10000
tid = str(rank.getRank(1)[0])

for i in range(10000):
	print 'size', size * i
	counter = Counter([str(s) for s in steps[i * size: (i+1) * size]])
	rank = 0
	count = 0

	for r, item in enumerate(counter.most_common()):
		if item[0] == tid:
			rank = r + 1
			count = item[1]
			print 'find'
			break
		
	fout.write('%d\t%d\n' % (rank, count))

fout.close()