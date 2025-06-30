
print(" mirrored right angle triangle (*):")
rows=int (input("enter the number of rows :" ))
for i in range (1, rows ,1 ):
    for i in range (rows+1): 

        print('  ' * (rows - i) + '* ' * i)
    print()
# This code prints a mirrored right angle triangle pattern of stars (*).
# The number of rows is determined by the user input.
