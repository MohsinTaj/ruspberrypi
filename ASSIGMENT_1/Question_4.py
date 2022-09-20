#Question # 4:
#Write a Python program to test if a variable is a list or tuple.
#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
x = ('tuple', False, 3.2, 1)
# x= input("enter the data structure you wanted to check: ").split(",")

if type(x) is list :
   print('x is a list')
elif type(x) is set:
   print('x is a set')
elif type(x) is tuple:
   print('x is a tuple')    
else:
   print('Neither a list or a set or a tuple.')

