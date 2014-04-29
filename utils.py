import time

def printRunningTime(func):
	def _printRunningTime(*args, **kwargs):
		start = time.time()
		print 'Start Running Function: ' + func.__name__ + '()'
		ret = func(*args, **kwargs)
		end = time.time()
		print 'Finish Running: ' + func.__name__ + '(). Total Running Time: ' + str(end - start) 

		return ret

	return _printRunningTime
