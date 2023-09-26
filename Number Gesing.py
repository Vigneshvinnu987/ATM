import numpy as np
print("\n\tIts Game for to guess the number for range 10")
print("------Your only chances it 10---------")
while True:
    cantidate = int(input("Enter the Number:"))
    a = np.random.randint(10)
    print("The a random number of generate:", a)
    if a == cantidate:
        count = 0
        count += 1
        print("Your calculate average guess 10 of", count)
    else:
        a = 0
        a += 1
        print("Your calculate average no match 10 of", a)
    b = 0
    b += 1
    if b == 10:
        break



