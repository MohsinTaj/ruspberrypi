#sets
#sequence examples 
bri=set(["brazil","russia","pakistan"])
print('india' in bri)
print('usa' in bri)
bric=bri.copy()
bri.add("china")
print(bric.issuperset(bri))
bri.remove("russia")
print(bric)
print(bri & bric) #or bri .intersection(bric)