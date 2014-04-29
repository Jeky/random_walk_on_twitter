import data
import sys
import rw
from collections import Counter
from utils import *


@printRunningTime
def countRank():
	'''
	Count the samples by step, and then sort them by count descendingly
	'''
	counter = Counter()
	def walker(tid, tag):
		counter[tid] += 1

	walkOnSampleResult.walkOnSampleResult(walker)

	frand = open(data.RANK_FILE, 'w')
	i = 0
	for tid, c in counter.most_common():
		if i != 0 and i % 1000000 == 0:
			print 'read', i, 'lines'
		frand.write('%d\t%d\n' % (tid, c))
		i += 1

	frand.close()


@printRunningTime
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

		if i != 0 and i % 1000000 == 0:
			print 'read', i, 'lines'

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