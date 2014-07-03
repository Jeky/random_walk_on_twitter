import sys
import data
from collections import *
from utils import *

IN_INDEX = 'in'
OUT_INDEX = 'out'

@printRunningTime
def countDegree(index):
	'''
	Count the in/out degree of graph file
	'''
    if index == IN_INDEX:
        print 'Counting in degree'
    elif index == OUT_INDEX:
        print 'Counting out degree'

	fdata = open(data.ORINGNAL_FILE)
	counter = Counter()

	for i, l in enumerate(fdata.xreadlines()):
		if i != 0 and i % 1000000 == 0:
			print 'read', i, 'lines'

		fromId, toId = l.strip().split('\t')

		if index == IN_INDEX:
			counter[toId] += 1
		elif index == OUT_INDEX:
			counter[fromId] += 1

	fdata.close()

	if index == IN_INDEX:
		fcount = open(data.NODE_IN_DEGREE_FILE, 'w')
	elif index == OUT_INDEX:
		fcount = open(data.NODE_OUT_DEGREE_FILE, 'w')

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
	print '''python degree.py in|out'''


if __name__ == '__main__':
	if len(sys.argv) != 2:
		printUsage()

	elif sys.argv[1] in [IN_INDEX, OUT_INDEX]:
		countDegree(sys.argv[1])
	else:
		printUsage()
