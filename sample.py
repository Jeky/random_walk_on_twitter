import random
import glob
import os.path
from utils import *
from collections import Counter

JUMP_TAG = 1
WALK_TAG = 0
PRINT_STEP = 100000

@printRunningTime
def loadGraph(filename):
    f = open(filename)
    g = {}
    g['in'] = Counter()

    for i, l in enumerate(f.xreadlines()):
        fromId, toId = l.strip().split('\t')
        # fromId = int(fromId)
        # toId   = int(toId)
        if fromId not in g:
            g[fromId] = []

        g[fromId].append(toId)
        g['in'][toId] += 1

    f.close()

    return g


@printRunningTime
def randomWalk(graph, length, outFile, jp = 0.05, continueWalking = False, removeFirst = True):
    '''
    Random walk on this graph

    Params:
    graph : a dict represents the adjacency list of graph
    length : sample length of walking
    outFile : output filename. The output format is id \t tag. Tag is 1 if jumped from previous node; 
              is 0 if walked from previous node.
    jp : jumping probability
    continueWalking :
        True : Will jump once the length of walking is enough.
               If jp = 0.05 and continueWalking = True, walker will walk 20 steps and then jump.
        False: Will jump randomly.
               If jp = 0.05 and continueWalking = False, walker will first roll the dice, and if
               the random value is bigger than 0.05, then walk, otherwise it will jump.
    removeFirst : remove the first step after jumping

    '''
    print 'Jump probability =', jp, 'continueWalking =', continueWalking, 'removeFirst =', removeFirst

    out = open(outFile, 'w')

    if continueWalking:
        _randomContinueWalk(graph, length, out, jp)
    else:
        if removeFirst:
            _randomWalkAndRemoveFirst(graph, length, out, jp)
        else:
            _randomWalk(graph, length, out, jp)

    out.close()


def _randomContinueWalk(graph, length, out, jp):
    count = 0
    withinCount = 0
    ids = graph.keys()

    currentId = random.choice(ids)
    out.write('%s\t%d\n' % (graph['in'][currentId], JUMP_TAG))
    count += 1

    while count < length:
        if count % PRINT_STEP == 0:
            print 'Walk Steps:', count

        if currentId not in graph: # dead end
            currentId = random.choice(ids)
            out.write('%s\t%d\n' % (graph['in'][currentId], JUMP_TAG))
            count += 1

        if jp == 0.05 or jp == 0.1 or jp == 0.2:
            if withinCount == int(1 / jp) - 1: # jump
                currentId = random.choice(ids)
                out.write('%s\t%d\n' % (graph['in'][currentId], JUMP_TAG))
                count += 1
                withinCount = 0
            else: # walk
                currentId = random.choice(graph[currentId])
                out.write('%s\t%d\n' % (graph['in'][currentId], WALK_TAG))
                count += 1
                withinCount += 1
        else:
            if withinCount == 100: # repeat
                withinCount = 0
            elif withinCount < 100 and withinCount >= 100 * (1 - jp): # jump
                currentId = random.choice(ids)
                out.write('%s\t%d\n' % (graph['in'][currentId], JUMP_TAG))
                count += 1
                withinCount += 1
            else: # walk
                currentId = random.choice(graph[currentId])
                out.write('%s\t%d\n' % (graph['in'][currentId], WALK_TAG))
                count += 1
                withinCount += 1


def _randomWalkAndRemoveFirst(graph, length, out, jp):
    count = 0
    ids = graph.keys()

    currentId = random.choice(ids)

    while count < length:
        if count % PRINT_STEP == 0:
            print 'Walk Steps:', count

        if currentId not in graph: # dead end
            currentId = random.choice(ids)

        elif random.random() < jp: # jump
            currentId = random.choice(ids)

        else: # walk
            currentId = random.choice(graph[currentId])
            out.write('%s\t%d\n' % (graph['in'][currentId], WALK_TAG))
            count += 1


def _randomWalk(graph, length, out, jp):
    count = 0
    ids = graph.keys()

    currentId = random.choice(ids)
    out.write('%s\t%d\n' % (graph['in'][currentId], JUMP_TAG))
    count += 1

    while count < length:
        if count % PRINT_STEP == 0:
            print 'Walk Steps:', count

        if currentId not in graph: # dead end
            currentId = random.choice(ids)
            out.write('%s\t%d\n' % (graph['in'][currentId], JUMP_TAG))
            count += 1

        elif random.random() < jp: # jump
            currentId = random.choice(ids)
            out.write('%s\t%d\n' % (graph['in'][currentId], JUMP_TAG))
            count += 1

        else: # walk
            currentId = random.choice(graph[currentId])
            out.write('%s\t%d\n' % (graph['in'][currentId], WALK_TAG))
            count += 1


if __name__ == '__main__':
    BASE_PATH = '/Users/jeky/dataset/samples/*'
    OUTPUT_PATH = '/Users/jeky/dataset/samples_rw/'

    for f in glob.glob(BASE_PATH):
        print 'Sampling', f

        g = loadGraph(f)
        for x in range(1, 21):
            randomWalk(g, 1000000, OUTPUT_PATH + os.path.basename(f) + '.rw%0.3f.rm1' % (0.01 * x), 0.01 * x, False, True)
            randomWalk(g, 1000000, OUTPUT_PATH + os.path.basename(f) + '.rw%0.3f' % (0.01 * x), 0.01 * x, False, False)
            randomWalk(g, 1000000, OUTPUT_PATH + os.path.basename(f) + '.rw%0.3f.cw' % (0.01 * x), 0.01 * x, True, True)