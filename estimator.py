import data
import rw
import sys
import degree
from utils import *

@printRunningTime
def estimateAverageDegree(top = 100000):
	steps = rw.readSteps()
	deg = {k:v for k,v in degree.getDegree(withCount = True)}

	fest = open(data.ESITMATE_FILE, 'w')
	rd = 0.0

	counter = 0.0

	for i in range(top):
		d = deg[steps[i]]
		if d == 0:
			continue

		counter += 1.0
		rd += 1.0 / d
		est = counter / rd
		fest.write('%lf\n' % est)

	fest.close()


if __name__ == '__main__':
	estimateAverageDegree(int(sys.argv[1]))
