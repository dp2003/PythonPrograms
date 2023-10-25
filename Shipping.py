class Transport:
    def __init__(self, vectype,total):
        self.__vectype = vectype
        self.__total= total
    def gettransport(self):
        print('Type of vehicle=',vectype)
        print('Total no.of transport vehicle=',total)
class Bus(Transport):
    def _init_(self, number,color):
        super()._init_(vectype,total)
        self.__number = number
        self.__color= color
    def getbus(self):
        print('Bus number=',number)
        print('Bus color=',color)
    def cal_speed(dist, time):
        print(" Distance(km) :", dist)
        print(" Time(hr) :", time)
        return = dist / time
    def cal_dis(speed, time):
       print(" Time(hr) :", time) 
       print(" Speed(km / hr) :", speed)
       return speed * time
    def cal_time(dist, speed):
       print(" Distance(km) :", dist)
       print(" Speed(km / hr) :", speed)
       return speed * dist
class Train(Transport):
    def _init_(self,train_no,train_type):
        super()._init_(vectype,total)
        self.__train_no= train_no
        self.__train_type=train_type
    def gettrain(self):
         print("Train number=",train_no)
         print("Train type=",train_type)

print("Enter transport details")
vectype=input()
total=int(input())
t1 = Transport(vectype,total)
print("Enter bus details")
number=int(input())
color=input()
b1=Bus(number,color)
print("Enter train details")
train_no=int(input())
train_type=input()
e1= Train(train_no,train_type)
t1.gettransport()
b1.getbus()
e1.gettrain()
print(" The calculated Speed(km / hr) is :")
b1.cal_speed(45, 2)
 
print(" The calculated Distance(km) :")
b1.cal_dis(62, 2)

print(" The calculated Time(hr) :")
b1.cal_time(48, 4)