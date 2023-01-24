

def is_even_odd(num):
    if num % 2 == 0:
        print("{} is even number".format(num))
    else:
        print("{} is odd number".format(num))

num=int(input("Enter the Number:"))
is_even_odd(num)