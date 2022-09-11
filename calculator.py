# calculator made by mohsin taj

c=str
while(c!=0):
    a=int(input("enter no 1: "))
    c=input("enter operator: ")
    b=int(input("enter no 2: "))
    if (c== '+'):
         print("answer is ",a+b)
    elif (c=='-'):
         print("answer is ",a-b)
    elif (c=='*'):
         print("answer is ",a*b)
    elif (c=='/'):
         print("answer is ",a/b)
    elif (c=='^'):
        g=pow(a,b)
        print("answer is ",g)
    elif (c=='sq'):
        n=int(input("enter the power: "))
        g=pow(a,n)+pow(b,n)
        
        print("answer is ",g)
    else:
        break