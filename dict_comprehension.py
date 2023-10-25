'''dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}
print(dict1_cond)

dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
print(dict1_doubleCond)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0 if v%3 == 0}
print(dict1_tripleCond)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
# Identify odd and even entries
dict1_evenodd = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}
print(dict1_evenodd)

b_dict={}
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
d1={1:[1,2],2:3}
for key,value in d1.items():
	b_dict[value]=key
print(b_dict)

x1 = {1,3}
x2 = {1,3,6,7,8}
print("Checking subset")
print(x1.issubset(x2))
print(x1<=x2)
# To check proper subset
print("Checking proper subset")
print(x1<x2)
print(x1<x1)
x2 = {1,3}
x1 = {1,3,6,7,8}
# To check superset
print("Checking superset")
print(x1.issuperset(x2))
print(x1>=x2)
# To check proper superset
print("Checking proper superset")
print(x1>x2)
print(x1>x1)

x = {'A', 'B', 'C','F'}
x.add('D')
print(x)
#if element is not existing remove() raises 
# an exception
x.remove('F')
print(x)
#x.remove('RAM') # raises exception
#Does nothing 
x.discard('A')
print(x)
#Removes a random element
x.pop()
print(x)
#Clears entire set
x.clear()
print(x)'''

x1={1,2,3,4}
#x1.update(x2) and x1 |= x2 add to x1 
#any elements in x2 that x1 does not already have
x1.update([3,5])
print(x1)
#Same as x1 &= X2
x1.intersection_update([3,4])
print(x1)
#Same as x1 -=x2
x1.difference_update([1,2])
print(x1)
#Same as x1 ^=x2
x1.symmetric_difference_update([1,2])
print(x1)
