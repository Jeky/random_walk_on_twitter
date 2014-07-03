import sys
import data
from collections import *
from utils import *

FROM_INDEX = 'from'
TO_INDEX = 'to'

@printRunningTime
def countDegree(index):
	'''
	Count the in/out degree of graph file
	'''
	fdata = open(data.ORINGNAL_FILE)
	counter = Counter()

	for i, l in enumerate(fdata.xreadlines()):
		if i != 0 and i % 100000 == 0:
			print 'read', i, 'lines'

		fromId, toId = l.strip().split('\t')

		if index == FROM_INDEX:
			counter[fromId] += 1
		elif index == TO_INDEX:
			counter[toId] += 1

	fdata.close()

	if index == FROM_INDEX:
		fcount = open(data.NODE_OUT_DEGREE_FILE, 'w')
	elif index == TO_INDEX:
		fcount = open(data.NODE_IN_DEGREE_FILE, 'w')

	print 'writing degree count file'
	for tid, c in counter.most_common():
		fcount.write('%s\t%d\n' % (tid, c))

	fcount.close()


@printRunningTime
def getDegree(top = 0, withCount = False):
	'''
	Get top n degree node with the count. If n = 0, return all nodes.
	Returning value is like this:
	[(1234,1111), (2345, 555), (555, 111), (111, 0)]
	'''
	degreeList = []
	fdegree = open(data.NODE_OUT_DEGREE_FILE)
	for i, l in enumerate(fdegree.xreadlines()):
		if top != 0 and i == top:
			break

		if i != 0 and i % 1000000 == 0:
			print 'read', i, 'lines'

		tid, count = l.strip().split('\t')
		if withCount:
			degreeList.append((int(tid), int(count)))
		else:
			degreeList.append(int(tid))

	fdegree.close()

	return degreeList


def printUsage():
	print '''python degree.py to|from'''


if __name__ == '__main__':
	if len(sys.argv) != 2:
		printUsage()

	elif sys.argv[1] in ['to', 'from']:
		countDegree(sys.argv[1])
	else:
		printUsage()
