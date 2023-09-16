try:
    n1 = int(input("Enter the Number:"))
    n2 = int(input("Enter the Number:"))
    option = "Chosse the opetion:\n\t 1.Add(+)\n\t2.Subtract(-)\n\t3.Multiplication(*)\n\t4.Divide(/)"
    print(option)
    choose = int(input("Select The Option:"))
    if choose == 1:
        print(f"Your add number {n1} + {n2}:", n1 + n2)
    elif choose == 2:
        print(f"Your subtract number {n1} - {n2}:", n1 - n2)
    elif choose == 3:
        print(f"Your multiplication number {n1} * {n2}:", n1 * n2)
    elif choose == 4:
        print(f"Your divistion number {n1} / {n2}:", n1 / n2)
    else:
        print("Thank you for using")
except ValueError:
    print("Please check the values")

#print(result)