count=0
l1=['abc','xyz','aba','1221']
for i in l1:
	if i[0]==i[len(i)-1]:
		count=count+1
print(l1,"=",count)