import glob
import os.path
   
OUTPUT_PATH = '/Users/jeky/dataset/samples_rw/'
DEGREE_PATH = '/Users/jeky/dataset/samples_degree/'
AVER_D_PATH = '/Users/jeky/dataset/samples_averd/'

PRINT_STEP = 100000


def estimate(degList):
    count = 0
    ret = 0.0
    for d in degList:
        if d != 0:
            ret += 1 / float(d)
            count += 1

    ret = count / ret

    return ret


def estiamteAverDegree(sampleFilename, averDFilename):
    print 'Analysing:', sampleFilename, '\nOutput file:', averDFilename
    f = open(sampleFilename)

    degList = []

    for i, l in enumerate(f.xreadlines()):
        if i % PRINT_STEP == 0:
            print 'reading sample files:', i

        degList.append(int(l.strip().split('\t')[0]))

    f.close()

    f = open(averDFilename, 'w')

    for i in range(100):
        averDeg = estimate(degList[i * 10000 : (i + 1) * 10000])
        f.write('%lf\n' % averDeg)

    f.close()


def averDegree(graphDegFilename, direction):
    print 'Calculating Average', direction, 'Degree of', graphDegFilename
    f = open(graphDegFilename)
    averDeg = 0.0
    count = 0

    for i, l in enumerate(f.xreadlines()):
        if direction == 'in':
            averDeg += float(l.strip().split('\t')[1]) 
            count += 1
        elif direction == 'out':
            averDeg += float(l.strip().split('\t')[2]) 
            count += 1  

    f.close()

    return averDeg / count


if __name__ == '__main__':
    for f in glob.glob(DEGREE_PATH + '*'):
        print averDegree(f, 'in')