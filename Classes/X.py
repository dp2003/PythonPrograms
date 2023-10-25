import random
import math
class Error(Exception):
	pass

class MarksNotInRange(Error):
	pass

mks= random.randint(0, 100)
while True:

	try:
		mks = int(input("Enter a marks:"))
		if mks<0 or mks>100:
			raise MarksNotInRange
		break 		

	except MarksNotInRange:
		print("enter value in range")


