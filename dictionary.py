#dictionary key:value
ab={
    "swaroop":"swaroop@swaroopch.com",
    "larry":"larry@wall.com",
    "Matsumoto":"matz@ruby-lang.org",
    "spammer":"spammer@hotmail.com"
    }
print("swaroop's address is ",ab["swaroop"])
#deleting a key-value pair
del ab["spammer"]
print("\nThere are {} contacts in the address".format(len(ab)))
for name,address in ab.items():
       print("Contact {} at {}".format(name,address))
       
#adding a key-value pair
ab["guido"]="guido@python.org"

for name,address in ab.items():
       print("Contact {} at {}".format(name,address))
       
if "guido" in ab:
    print("\n Guido's address is ", ab["guido"])
    
c={
    "sufy":"buisnessman",
    "misbah":"shaparter",
    "huzaifa":"bahadur"
    }
print(c["sufy"])
print(c["misbah"])
print(c["huzaifa"])
for name,address in c.items():
       print("Contact {} the {}".format(name,address))
       
       
shoplist=["apple","mango","carrot","banana",]
name="swaroop"
#slicing on a list
print("item 1 to 3 is ",shoplist[1:3])
print("item 1 to end is ",shoplist[2:])
print("item 1 to -1 is ",shoplist[1:-1])
print("item 0 to last is ",shoplist[:])
print("item 0 to last is ",shoplist[:])
print(" 1 to 3 is ",name[1:3])
print(" 2 to last is ",name[2:])
print("1 to -1 is ",name[1:-1])
print("0 to last is ",name[:])
print("0 to last is ",name[:])



       




       