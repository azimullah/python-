medical_cause=input( "did you have a medical degree Y for yes and N for no ")
atten=int(input( "enter the ateendence of student  " ))


if medical_cause == "Y" :
     print("you are allowed")
else :
    if atten >75 :
         print( "you are allowed" )
    else:
         print(" you are not allowed")