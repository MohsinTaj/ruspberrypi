#sets
#sequence examples 
bri=set(["brazil","russia","pakistan"])
'india' in bri
'usa' in bri
bric=bri.copy()
bri.add("china")
bric.issuperset(bri)
bri.remove("russia")
bri & bric #or bri .intersection(bric)