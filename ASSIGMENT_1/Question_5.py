# # Question # 5:
# # Write a Python function that takes two lists and returns True if they have at least one 
# # common member.
def comp(a,b):
    for x in a:
        for y in b:
            if x==y:
                return True
            else:
                return False

list1=list(input("enter list 1:").split(","))
list2=list(input("enter list 2:").split(","))
print(comp(list1,list2))
