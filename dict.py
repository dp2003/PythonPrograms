Dict = {'d1':100,'d2':54,'d3':200}
print(Dict)
print("SUM OF ALL ITEMS")
print(sum(Dict.values()))
print()

 

dict={}
num=int(input("Enter the number till which you want to find the square root:"))
for i in range(1,num+1):
    dict[i]=i*i
print(dict)
print()

 

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print("Updated dictionary:")
print(dic4)
print()

 

from collections import defaultdict, Counter
str1 = 'Python Programming' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(str1)
print(my_dict)