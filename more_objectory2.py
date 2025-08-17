class Employee:

    def __init__(self,):
       print("employee created")
    
    def __del__(self):
        print("employee deleted")

def create_obj():
    print("Making object ...")
    x = Employee()
    print("Object end")
    return x
obj=create_obj()