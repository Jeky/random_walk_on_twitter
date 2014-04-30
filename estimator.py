import data
import rw
import sys
import degree
from utils import *

@printRunningTime
def estimateAverageDegree(top = 10000, filename = None):
	steps = []
	if filename:
		steps = rw.readStepsFromFile(filename, top)
	else:
		steps = rw.readSteps()

	deg = {k:v for k,v in degree.getDegree(withCount = True)}
	fest = open(data.ESITMATE_FILE, 'w')
	rd = 0.0
	counter = 0.0

	for tid in steps:
		d = deg[tid]
		if d == 0:
			continue

		counter += 1.0
		rd += 1.0 / d
		est = counter / rd
		fest.write('%lf\n' % est)

	fest.close()


if __name__ == '__main__':
	if len(sys.argv) == 2:
		estimateAverageDegree(int(sys.argv[1]))
	else if len(sys.argv) == 3:
		estimateAverageDegree(int(sys.argv[1]), sys.argv[2])
