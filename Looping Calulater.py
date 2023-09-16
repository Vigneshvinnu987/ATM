try:

    n = int(input("Enter the how many datas:"))
    while 0 < n:
        value1 = int(input("Enter the value:"))
        option = "\n\t1.Add(+)\n\t2.Subtract\n\t3.Multiplication\n\t4.Division"
        print(option)
        choose = int(input("Enter the option:"))
        if choose == 1:
            value2 = int(input("Enter the next Value:"))
            print(f"{value1} add the {value2} =", value1 + value2)
            global value3
            value3 = value2 + value1
        elif choose == 2:
            value4 = int(input("Enter the next value:"))
            print(f"{value1} subtract the value {value4}=", value1 - value4)
        elif choose == 3:
            value5 = int(input("Enter the next value:"))
            print(f"{value1} multiplication of {value5} =", value1 * value5)
        elif choose == 4:
            value6 = int(input("Enter the next value:"))
            print(f"{value1} division of {value6} =", value1 / value6)
        else:
            print("Enter the value datas")
        break
except Exception:
    print("Please enter the value datas")
