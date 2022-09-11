"for loop"
a=int(input("enter a table"))
for i in range(1,11):
    print(a ,"*", i ,"is", a*i)
else:
    print("loop is over")
    
for b in range(1,11,2):
    print(b)
"table"
".format method"
d=int(input("enter a table"))
for c in range(1,11):
  
    print("{0} * {1} = {2}" .format(d,c,d*c))
else:
    print("loop is over")
    
"length method"    
while True:
    s=input("enter something: ")
    if s=='quit':
        break
    if len(s)<3:
        print("too small")
        continue
    print("input is of sufficient length")    
        
    
    print("length of the string is " , len(s))
print("done")



"functions"
def say_hello():
    print("hello world")
say_hello()
say_hello()

   