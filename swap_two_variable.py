

def swap_two_variable(var1, var2):
    var2, var1 = var1, var2

    return var1, var2


a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
print("before swapping the values are:")
print("a = {}, b = {}".format(str(a), str(b)))
a, b = swap_two_variable(a, b)
print("After swapping the values are:")
print("a = {}, b = {}".format(str(a), str(b)))