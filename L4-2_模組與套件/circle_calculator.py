'''
import sys
import math

def circle_calculator(r):
	return math.pi * r **2, 2 * math.pi * r
	
radius = float(sys.argv[1])
print("Radius:%.2f, Area:%.4f" % 
	(radius, circle_calculator(radius)[0]))

print("Radius:%.2f, Circum:%.4f" % 
	(radius, circle_calculator(radius)[1]))
'''

# 精簡寫法
import math

def circle_area(r):
    'Calculate circle area'
    area = math.pi * r**2
    return area

def circle_circum(r):
    'Calculate circle circum'
    circum = 2 * math.pi * r
    return circum