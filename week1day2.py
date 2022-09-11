#format method
#values ki placing ke liye hota he
age =20
name='Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name,age))
print('why is {0} playing with that python?'.format(name))
#string concatination
print(name+' is '+str(age)+' years old ')
#print function
string1='hello'
string2='world'
print ((string1+' ' +string2+' '+'! '*3 )  *3)
print('{} was {} years old when he wrote this book'.format(name,age))
print('why is {} playing with that python?'.format(name))
print('{0:.3f}'.format(1.0/3))
print('{0:+^6}'.format('hello'))
print('{name} wrote {book}'.format(name='swaroop',book='python'))
 
 
"escape sequence"

print("'what' your name")
print('what\'s your name')
print('what\"s your name')
print('how\\\\who\'s')
print('this is the first line \n this is the second\tline')
print(5//4)

"ASCII CODE"
_A=3
a=3


"logical and physical line"
i=5
print(i)

i=5;  print(i)
"phyical line ko logicaL LINE ME CONVERT KRTA HE"
s='this is a string \
this continues a string'
print(s)

"if else statement"
answer="yes"
guess=input("is the sky is blue? ")
if guess==answer:
    print("correct")
else:
    print("wrong")
    
    
"mathematical operation"
print(2+3)
print(8-5)
print(4*6)
print(2**4)
print(5/4)
print(5//4)
print(5%3)

print(5<3)
print(5<=3)
print(5>3)
print(5>=3)
print(5==6)
print(5==5)
print(7!=6)


#logical operators
#and for && / or for ||
#boolean operators
x=True
y=False
print(x and y)


#logic building
a=2
a=a*3
print(a)
#same as
b=2
b*=3
print(b)
c=1
c+=1

print(c)


#practice question
length=5
breadth=2

print('Area is ', length*breadth)

print('perimeter is ' ,2*(length*breadth))


#control flow if else if statement
number1=23
guess=int(input("enter an integer"))
if guess==number1:
    print("congratulation")
elif guess<number1:
    print("no , it is a little higher")
else:
    print("no, it is a little lower")
    
print("done")

name=input("enter a name ")
guess1=input("guess the name ")
if name==guess1:
      print("bingo")
else:
      print("no your are wrong")
 
print("done")

#while loop
number=23
running=True
while running:
    guess=int(input("enter an integer "))
    if guess==number:
        print("congratulations")
        running=False
        
    elif guess<number:
        print("no it is a little higher")

    else:
        print("no it is a little lower")
else:
   print("the while loop is ended")         
    
print("done")  


#for loop
for i in range(1,55):
    print(i)
else:
    print("the loop is over")
    
    
"table building"
b=int(input("enter a number"))
for a in range(1,11):
      print( b*a)
else:      
    print( " loop is over")
    
for c in range(1,11,2):
    print(c)
else:
    print("loop is ended")
