import data
from collections import *

FROM_INDEX = 'from'
TO_INDEX = 'to'

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


def printUsage():
	print '''python count_degree.py in|out'''


if __name__ == '__main__':
	if len(sys.argv) != 2:
		printUsage()

	elif sys.argv[1] in ['to', 'from']:
		countDegree(sys.argv[1])
	else:
		printUsage()