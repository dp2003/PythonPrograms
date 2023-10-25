class Transport:
    def _init_(self, vectype,total):
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
    def cal_speed(self):
        print("\n______Speed calculation if you know distance and time______\n")
        print("Enter distance and time taken: ")
        dist=float(input())
        time=float(input())
        print(" Distance(km) :", dist);
        print(" Time(hr) :", time);
        speed = dist / time;
        print("Speed of ship=",speed)

    def cal_dis(self):
        print("\n______Distance calculation if you know speed and time______\n")
        print("Enter speed and time taken: ")
        speed=float(input())
        time=float(input())
        print(" Speed(km/hr) :", speed);
        print(" Time(hr) :", time);
        dist = speed * time;
        print("Distance traveled by the ship=",dist)

    def cal_time(self):
        print("\n______Time calculation if you know speed and distance______\n")
        print("Enter speed and distance : ")
        speed=float(input())
        dist=float(input())
        print(" Speed(km/hr) :", speed);
        print(" Distance(km) :", dist);
        time = speed * dist;
        print("Time taken by ship=",time)
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
b1.cal_dis()
b1.cal_time()
b1.cal_speed()