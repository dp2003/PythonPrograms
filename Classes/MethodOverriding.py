class Parent():

    def __init__(self):
        self.value = "Inside Parent"          

    def show(self):
        #print(self.value) 
        print("Parent")  

class Child(Parent):
    def __init__(self):
        self.value = "Inside Child"         

    def show(self):
        super().show()
        print(self.value)         

# Testing Code

ob1 = Parent()
ob2 = Child()
ob1.show()
ob2.show()

#Note: The object which invokes the method, the reference of that object
# is passed to self.