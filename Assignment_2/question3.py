numbers = [1, 2, 3, 4, 2, 3, 5]
rep = []
for n in numbers:
    if numbers.count(n) > 1:
        if n not in rep:
            print("Repeated number: ", n)
            rep.append(n)