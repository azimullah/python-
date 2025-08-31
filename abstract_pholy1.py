from abc import ABC, abstractmethod

class Absclass(ABC):
    def print (self , x):
        print("passed value", x)

    def task (self ):
       print("inside abstract class")
    

class test_class(Absclass):
    def task (self  ):
        print("inside test class")
        
obj = test_class()
obj.task()
obj.print(100)