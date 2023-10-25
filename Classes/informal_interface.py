class Fruits :
        def __init__( self, ele):
                print(id(ele))
                print(ele)
                self.__ele = ele
        def __contains__( self, ele):
                print(ele)
                return ele in self.__ele
        def __len__( self ):
                return len( self.__ele)
        def __iter__( self):
               return self
l1=["Apple", "Banana", "Orange"]
print(id(l1))
Fruits_list = Fruits(l1)
# protocol to get size
print(len(Fruits_list))
# protocol to get container
print("Apple" in Fruits_list)
print("Mango" in Fruits_list)
print("Orange" not in Fruits_list)
