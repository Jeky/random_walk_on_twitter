import data
import rw
import sys
import degree

def estimateAverageDegree(top = 100000):
	steps = rw.readSteps()
	deg = {k:v for k,v in degree.getDegree(withCount = True)}

	fest = open(data.ESITMATE_FILE, 'w')
	rd = 0.0

	for i in range(top):
		count += 1.0
		rd += 1.0 / deg[steps[i]]
		est = (i + 1.0) / rd
		fest.write('%lf\n' % est)

	fest.close()


if __name__ == '__main__':
	estimateAverageDegree(int(sys.argv[1]))
