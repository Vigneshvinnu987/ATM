try:
    n = int(input("Enter the Number:"))
    while 0 < n:
        print("\n\tWhat Table Excepted")
        print("\n\t1.Addtion(+)\n\t2.Substraction(-)\n\t3.Multiplication(*)\n\t4.Division(/)")
        choose = int(input("Enter the option:"))
        if choose == 1:
            print("Addition Table for", n)
            for i in range(1, 11):
                print(i, "+", n, "=", i + n)
        elif choose == 2:
            print("Subtraction Table for", n)
            for i in range(1, 11):
                print(i, "-", n, "=", i - n)
        elif choose == 3:
            print("Multiplication table for", n)
            for i in range(1, 11):
                print(i, "*", n, "=", i * n)
        elif choose == 4:
            print("Division Table for", n)
            for i in range(1, 11):
                print(i, "/", n, "=", i // n)
        else:
            print("Please Enter the value option")

        break
except Exception:
    print("Enter the Value Number")

finally:
    print("------------THANKS FOR USING------------")