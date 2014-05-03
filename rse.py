import rw
import rank
from utils import *

TOP = 100
SAMPLE_COUNT = 100
SAMPLE_TIME = 100


def count(arr):
	freq = {}
	for i in arr:
		if i in freq:
			freq[i] = freq[i] + 1
		else:
			freq[i] = 1

	freq = [(k,v) for k,v in freq.iteritems()]
	freq.sort(key = lambda x : -x[1])
	return [f[0] for f in freq]


def getRank(freq, rankList):
	ranks = {}
	for r in rankList:
		ranks[r] = 0

	for i, f in enumerate(freq):
		if f in rankList:
			ranks[f] = i + 1

	ranks = [(k,v) for k,v in ranks.iteritems()]
	ranks.sort(key = lambda x: rankList.index(x[0]))

	return [x[1] for x in ranks]


@printRunningTime
def rse(steps, rankList):
	eachSize = len(steps) / SAMPLE_TIME / SAMPLE_COUNT
	outputs = []

	for k in range(TOP):
		f = open('sample-%d.txt' % (k + 1), 'w')
		outputs.append(f)

	for i in range(1, SAMPLE_TIME + 1):
		size = eachSize * i
		print 'counting:', size
		for j in range(TOP):
			freq = count(steps[j * size : (j + 1) * size])
			ranks = getRank(freq, rankList)
			for k, r in enumerate(ranks):
				outputs[k].write(str(r))
				if j != TOP - 1:
					outputs[k].write(',')

		for output in outputs:
			output.write('\n')

	for output in outputs:
		output.close()


if __name__ == '__main__':
	steps = rw.readSteps()
	rank = rank.getRank()
	rse(steps, rank[:TOP])