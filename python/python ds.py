#lists
#used to store differnt data types
list1=[5,'emr',26.5]
print list1[0]
print list1[-1]
print list1[:]#shows the entire string
#lists are mutable you can add elements or modify them accordingly. it is a container that holds other objects in given order
list1[0]='hola!'
list1.append('good morning')#takes the value and adds at the end of the list
print list1
#tuples
#a tuple is immutable . if you try to edit them it will show errors
#tuples are defined using () and separated by commas
#procesesing of tuples is faster than list. it makes the data safe as tuples are immutable
tup1=(5,6,'hola')
tup2=(50.6,)
print tup1[0]
print tup1[-1]

print len (tup1)
print tup2

str1='akhil'
print len(str1)
print'\n'

#type casting
a=raw_input('enter a number')
if a==6:
    print'yes'
else:
    print'no'
a=int(raw_input('enter a number'))
if a==6:
    print'yes'
else:
    print'no'
print '\n'
#dictionary
# an unordered setv of key and value pair, a container that contains data,enclosed within curly braces
# the pair that is key and value is known as item(the key passed must be unique)
# the key and value is separated by a colon. items are separated from each other by a comma
dict1={1:'S.No','name':'akhil',5:25}
print dict1[1]
print dict1['name']
print dict1[5]

print dict1.items()
print dict1.keys()
print dict1.values()
print type(dict1)

dict1[4]=999
print dict1
