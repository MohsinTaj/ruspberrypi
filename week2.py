#function is a set of code it is used to minimize the complexity of code
def say_hello():
    print("hello")
say_hello()
say_hello()
#function parameters
def print_max(a,b):    #these are called parameters parameters
    if a>b:
        print(a, 'is maximum')
    elif a==b:
        print(a, 'is equal to',b)
    else:
        print(b,'is maximum')
        
c=int(input("enter a no: "))
d=int(input("enter a no: "))
print_max(c,d) #these are called arguments
#when we called a fun

#local variable
x=50
def func(x):
    print("x is ", x)
    x=2
    print("changed local x to", x) #value will change 
func(x)
print("x is still", x)


#global variable
x=50
def func():
    global x
    print("x is ", x)
    x=2
    print("changed global x to", x) #value will change 
func()
print("value of x is", x)
#keyword arguments
def func1(a,b=5,c=10):
    print("a is", a, "and b is ",b," c is ",c )
func1(3,7)
func1(25,c=24)
func1(c=50, a=100)
#return statement : 
def maximum(x,y):
    if x>y:
        return x
    elif x==y:
        return "the numbers are equal"
    else:
        return y

print(maximum(2,3))