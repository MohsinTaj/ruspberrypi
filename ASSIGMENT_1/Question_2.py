#Question # 2:
#Write a Python function that takes a list of words and returns the length of the longest 
#one.

# function to find the longest
# length in the list
def longestLength(a):
    max = len(a[0])
    leng = a[0]

# for loop to traverse the list
    for i in a:
     if(len(i) > max):
               max = len(i)
               leng = i 
    print("The word with the longest length is:",leng," and length is ", max)
    print(a)
        
   


 
a = input("Enter the list of word separated by comma:").split(",")
longestLength(a)

