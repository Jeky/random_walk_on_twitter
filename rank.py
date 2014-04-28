import data
import sys
import rw
from collections import Counter


def countRank():
	'''
	Count the samples by step, and then sort them by count descendingly
	'''
	steps = rw.readSteps()
	counter = Counter(steps)

	frand = open(data.RANK_FILE, 'w')
	for tid, c in counter.most_common():
		frand.write('%d\t%d\n' % (tid, c))

	frand.close()


def getRank(top = 0, withCount = False):
	'''
	Get top n rank node with the count. If n = 0, return all nodes.
	Returning value is like this:
	[(1234,1111), (2345, 555), (555, 111), (111, 0)]
	'''
	rankList = []
	frand = open(data.RANK_FILE)
	for i, l in enumerate(frand.xreadlines()):
		if top != 0 and i == top:
			break

		tid, count = l.strip().split('\t')
		if withCount:
			rankList.append((int(tid), int(count)))
		else:
			rankList.append(int(tid))

	frand.close()

	return rankList


def printUsage():
	print '''python rank.py count'''


if __name__ == '__main__':
	if len(sys.argv) != 2:
		printUsage()

	elif sys.argv[1] == 'count':
		countRank()
	else:
		printUsage()