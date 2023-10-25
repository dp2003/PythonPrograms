x1 = {1, 2, 3,4,5}
x2 = {1,3,6,7,8}
print("Union Operation:")
print(x1 | x2)
print(x1.union(x2))
print("Intersection Operation:")
print(x1 & x2)
print(x1.intersection(x2))
print("Difference Operation:")
print(x1 - x2)
print(x1.difference(x2))
print(x2 - x1)
print(x1.difference(x2))
print("Symmetric difference Operation:")
print(x1^x2)
print(x1.symmetric_difference(x2))
#x1.isdisjoint(x2) returns True if x1 and x2 have no elements in common
print("Disjoint Operation:")
print(x1.isdisjoint(x2))
