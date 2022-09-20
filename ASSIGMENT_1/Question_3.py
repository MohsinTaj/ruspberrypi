#Question # 3:
#Write a Python function that can find the median among three numbers.


def median(a,b,c):
    return (a+b+c/3)


x=int(input("enter number 1:"))
y=int(input("enter number 2:"))
z=int(input("enter number 3:"))
print("median of three numbers is {0:.3f}".format(median(x,y,z)))
