a = 89   #it is a global variable 

def fun() :
    global aI   #it changes global variable a from 89 to 3
    a = 3
    print(a)


fun ()
print(a)