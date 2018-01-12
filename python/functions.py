def myfunc(x,y,z):
    print 'hola!'
    print 'welcome to DIP WS'
    print x+y
    return x*y*z
    

print myfunc(5,6,7)
#in c language we can return only one value but in python we can return more then one values
def myfunc1(x,y,z):
    return x**2,y+1,z*3

a,b,c=myfunc1(5,6,7)
print a,b,c
#returned values are in the form of a tuple because they are enclosed within paranthesis

#modules
# if we have defined number of functions...... a module is a file where classes, functions and variables are defined.
#grouping similar code into a single file makes it easier to access.... we import certain functions and modify them according to our needs
#aggregate thousands of codes into a single file

