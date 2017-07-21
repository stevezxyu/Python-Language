from statspy import mean_module
import math

def my_sd(x):
	n_minus_one = len(x) - 1
	x_bar = mean_module.my_mean(x)
	sqe = 0
	for i in x:
		sqe += (i - x_bar)**2
	return math.sqrt(sqe/ n_minus_one)