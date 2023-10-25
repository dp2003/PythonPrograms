#clear() and count()
#Defining a list
print()
list1=[1,2,3]
list1.clear()
print('List:',list1)
#Another way using del
list2=[10,20,30]
del list2[:]
print('List:',list2)
demo=['f','o','l','l','o','w']
print("Occurance of o=",demo.count('o'))
print("Occurance of l=",demo.count('l'))