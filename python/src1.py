'''myStr=' '
for x in range(10):
    #myStr=myStr+str(x)#concatenate the string
     myStr+=str(x)
    #print x,
     print myStr

print '\n'

i=100
while i>90:
    i-=1
    print i,
    if i<95:
        break'''
    
#break terminates the lopo at a point and transfers the execution to the statement immediately folloeing the loop
#continue causes the loop to skip the remainder of its body and immediately executes the starting condition
#pass is used when a statement is required syntactically but does nothing or you do not want the command to be executed

#to check if a number is prime or not

'''n=input('enter n:')
print n
for i in range(2,n):
    if n%i is not 0:
        continue
    else:
        break
if i is n-1:
    print 'number is prime'
else:
    print'number is not prime'
#to find factorial of a number

print'\n'
a=input('enter a:')
print a
for i in range(1,a):
    a=a*i
print a

#to find greatest common divisor

print '\n'
b=input('enter number:')
print b
a=input('enter number:')
print a
t=1
while b%a is not 0:
    t=a
    a=b%a
    b=t
print a'''
'''strings in python are immutable(cant be modified)
strings are stored as individual characters in cotinuopus memory locations
creating strings:
using single quotes''/double quotes""
both forward (0 1 2 3 4 5)and backward indexing(-1 -2 -3 -4 -5 -6) are posssible in python'''
#concatenation operator
str1='string 1'
str2="string 2"
print str1+str2
print 5*str1
print '\n'
#membership operators
# in returns true if a variable is in sequence of another variaqble, else false
# not in returns true if a variable is not in sequence of another variable, else false
str1='python is a easy lang'
str2="pytho"
print str2 in str1
print '\n'
#relational operators
#the strings are compared based on the ascii value
str1='python'
str2='python'
print str1==str2 

print'\n'
#slice notation
#string slice is a substring which is the part of string we can use forward as well as backward indexing to access elements 
str1='python is a easy language'
print str1[0:5+1]
print str1[-6:-1]+str1[-1]
#
