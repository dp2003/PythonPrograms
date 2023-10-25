tup=(1,2,3,4,5)
for i in tup:
	if i==tup[0]:
		flag=True
	else:
		flag=False
		break
if flag==True:
	print("All the elements in the tuple are same")
else:
	print("All the elements in the tuple are not same")