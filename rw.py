import data
import sys
import glob
import utils

STEP_IN_PIECE = 1000000
RW_PIECE_NAME = data.RW_PATH + 'rw.%d.txt'


@printRunningTime
def getRwFileCount():
	return len(glob.glob(data.RW_PATH + '*'))


@printRunningTime
def split():
	'''
	Split random walk file into pieces. Every piece contains 1,000,000 steps
	'''
	frw = open(data.RW_FILE)
	rwFileCount = getRwFileCount()

	writeCount = 0
	fout = open(RW_PIECE_NAME, 'w')
	print 'writing', RW_PIECE_NAME % rwFileCount

	for i, l in enumerate(frw.xreadlines()):
		if writeCount == STEP_IN_PIECE:
			rwFileCount += 1
			fout.close()

			writeCount = 0
			fout = open(RW_PIECE_NAME % rwFileCount, 'w')
			print 'writing', RW_PIECE_NAME % rwFileCount

		fout.write(l)
		writeCount += 1


	fout.close()
	frw.close()


@printRunningTime
def readSteps():
	'''
	Read all steps of random walk
	'''
	steps = []

	for i in range(getRwFileCount()):
		rwpiece = open(RW_PIECE_NAME % i)
		print 'reading', RW_PIECE_NAME % i
		for l in rwpiece.xreadlines():
			tid, tag = l.strip().split('\t')
			steps.append(int(tid))

		rwpiece.close()

	return steps


def printUsage():
	print '''python rw.py split'''


if __name__ == '__main__':
	if len(sys.argv) != 2:
		printUsage()

	elif sys.argv[1] == 'split':
		split()
	else:
		printUsage()