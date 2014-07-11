import data
import sys
import glob
from utils import *

STEP_IN_PIECE = 1000000
RW_PIECE_NAME = data.RW_PATH + 'rw.%d.txt'
REMOVE_COUNT = 1


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
def readSteps(top = 0):
    '''
    Read all steps of random walk
    '''
    steps = []
    removeCount = REMOVE_COUNT

    for i in range(getRwFileCount()):
        rwpiece = open(RW_PIECE_NAME % i)
        print 'reading', RW_PIECE_NAME % i

        for l in rwpiece.xreadlines():
            if top != 0 and len(steps) == top:
                rwpiece.close()
                return steps

            tid, tag = l.strip().split('\t')
            if tag == '1':
                removeCount = REMOVE_COUNT
            else:
                removeCount -= 1

            if removeCount <= 0:
                steps.append(int(tid))

        rwpiece.close()

    return steps

@printRunningTime
def readStepsFromFile(filename, top = 0):
    '''
    Read all steps of random walk from file
    '''
    steps = []
    removeCount = REMOVE_COUNT

    rwpiece = open(filename)
    print 'reading', filename

    for l in rwpiece.xreadlines():
        if top != 0 and len(steps) == top:
            rwpiece.close()
            return steps

        tid, tag = l.strip().split('\t')
        if tag == '1':
            removeCount = REMOVE_COUNT
        else:
            removeCount -= 1

        if removeCount <= 0:
            steps.append(int(tid))

    rwpiece.close()

    return steps

@printRunningTime
def walkOnSampleResult(walker):
    '''
    Walk on random walk sample result. For each step in walking, use walker function to handle it.
    Walker function takes two parameters. 
    First is tid, an integer of twitter id.
    Second one is tag. If tag == '1', means this step is jumped from previous step;
    tag == '0' means this step is walked from preivous step.

    Walker function should have return value. If walker function return True, walk will continue; otherwise it will stop.
    '''
    removeCount = REMOVE_COUNT

    con = True

    for i in range(getRwFileCount()):
        rwpiece = open(RW_PIECE_NAME % i)
        print 'reading', RW_PIECE_NAME % i

        for l in rwpiece.xreadlines():
            if not con:
                rwpiece.close()
                return

            tid, tag = l.strip().split('\t')
            if tag == '1':
                removeCount = REMOVE_COUNT
            else:
                removeCount -= 1

            if removeCount == 0:
                if not walker(int(tid), tag):
                    con = False

        rwpiece.close()


def printUsage():
    print '''python rw.py split'''


if __name__ == '__main__':
    if len(sys.argv) != 2:
        printUsage()

    elif sys.argv[1] == 'split':
        split()
    else:
        printUsage()