# Question # 7:
# Write a Python Function to check if a given key already exists in a dictionary
def check(a):
    if 'Guido' in a:
           print("\nGuido's address is", a['Guido'])


ab = {
 'Swaroop': 'swaroop@swaroopch.com',
 'Larry': 'larry@wall.org',
 'Matsumoto': 'matz@ruby-lang.org',
 'Spammer': 'spammer@hotmail.com',
 'Guido':"123"
}


check(ab)