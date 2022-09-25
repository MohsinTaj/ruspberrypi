# References
print("simple assignment")
shoplist=["apple",'mango','carrot','banana']
mylist=shoplist
del shoplist[0]
print("my list is ",mylist)
print("my shoplist is ",shoplist)
mylist= shoplist[:]
del shoplist[0]
print("my list is ",mylist)
print("my shoplist is ",shoplist)

#Strings
name="swaroop"
if name.startswith("swa"):
    print("yes ")
if "a" in name:
    print("yes it contains")   
if name.find    ("war")!=-1:
    print("yes")
#-1=false=0 same
delimiter='_*_'
mylist=["brazil", "russia",'India' ,'china']    
print(delimiter.join(mylist))
delimiter=','  
mylist=["apple",'mango','carrot','banana']    
print(delimiter.join(mylist))