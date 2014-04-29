import data
import rw
import sys
import rank

def estimateAverageDegree(top = 100000):
	steps = rw.readSteps()
	degree = {k:v for k,v in rank.getRank(withCount = True)}

	fest = open(data.ESITMATE_FILE, 'w')
	rd = 0.0

	for i in range(top):
		rd += 1.0 / degree[steps[i]]
		est = (i + 1.0) / rd
		fest.write('%lf\n' % est)

	fest.close()


if __name__ == '__main__':
	estimateAverageDegree(int(sys.argv[1]))
