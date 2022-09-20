# Question # 7:
# Write a Python Function to check if a given key already exists in a dictionary
def check(a):
    x=input("enter the data you want to check: ")
    if x in a:
           print(x + " is present & \n"+ x + " address is ", a[x])
    else:
        print("Invalid key ")

ab = {
 'Swaroop': 'swaroop@swaroopch.com',
 'Larry': 'larry@wall.org',
 'Matsumoto': 'matz@ruby-lang.org',
 'Spammer': 'spammer@hotmail.com',
 'Guido':"123"
}


check(ab)