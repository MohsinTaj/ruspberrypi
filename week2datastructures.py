#"arrays are one dimensional in python there is list in python"
shoplist=['apple','mango','carrot','banana']
print('I have ',len(shoplist), 'items to purchase')
print("these items are:", end=' ')
for item in shoplist:

    print(item, end=' ')
    
print("\nI also have to buy rice")
shoplist.append("rice")
print("my shopping list is now ", shoplist)
#immuatble is tuple, tuple is memory efficient
#list is mutable
print("I will sort my list now")
shoplist.sort()             #alphabetical order

print("sorted shop list is now",shoplist)
print("The first item I will buy is",shoplist[0])
olditem=shoplist[0]
del shoplist[0]
print("I bought the ",olditem)
print("My shopping list is now", shoplist)
print("checking position ",shoplist[0])
shoplist.sort(reverse=True)
#10 methods for list assignment
print(shoplist)