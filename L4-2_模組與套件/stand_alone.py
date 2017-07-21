import sys

print("I am executed from the terminal!", sys.argv)
for i in sys.argv:
	print(i)