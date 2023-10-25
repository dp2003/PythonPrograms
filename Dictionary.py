Dict = {}

Dict[0] = 'Folks'
Dict[2] = 'For'
Dict[3] = 1
print("Dictionary after adding 3 elements: ",Dict)

Dict['Value_set'] = 2, 3, 4
print("After adding set of values: ",Dict)

Dict[2] = 'Welcome'
print("Updated key value: ",Dict)

Dict[5] = {'Nested' :{'1' : 'Male', '2' : 'Female'}}
print("Adding a Nested Key:",Dict)
