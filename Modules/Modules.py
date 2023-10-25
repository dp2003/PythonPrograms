import calculation
print(calculation.add(2,5))
print(calculation.sub(6,2))

import calculation as cal
print(cal.add(10,5))
print(cal.sub(10,3))

from calculation import add
print(add(2,5))

from calculation import*
print(add(2,5))
print(add(6,2))

from math import pi,e
print("Value of pi = ",pi)
print("Value of e = ",e)

print(dir())






