class myclass:
    __private = 34

    def __privfunction(self):
       print("im inside class and this is a prive fuction")

    def hello(self):
       print("hello", myclass.__private)


obj =myclass()
obj.hello()
obj.__privfunction()