

def multiplication_table(tab_number):
    print("The Multiplication Table of: ", tab_number)

    for i in range(1, 11):
        print("{} x {} = {}".format(tab_number, i, (tab_number*i)))
num = int(input("Enter the number:"))
multiplication_table(num)
