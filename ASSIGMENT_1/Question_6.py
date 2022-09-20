# Question # 6:
# Write a Python program to reverse a tuple (in both string and numbers).
zoo = ('python', 'elephant', 'penguin',2,2,3)
# print(sorted(zoo))
result = reversed(zoo)
result = tuple(result)
print(result)