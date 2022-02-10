# function that checks whether a number belongs to the fibonacci
def is_fibonacci(num):

    # these two variables contain digits belong to the finobacci
    a = 0
    b = 1
    
    # condition to check whether the user has entered any of the two numbers stored in the variables
    if num == a or num == b:
        return True
    else:
    
        # condition to loop through the sum of finobacci sequence digits as long as it is less than the input
        while b < num:
            c = a + b
            a = b
            b = c
            
        # condition to check if the input integer is part of the finobacci sequence
        if b == num or a == num:
            return True
        else:
            return False

# input the integer
num = int(input("Enter an integer: "))


# check whether the number is fibonacci
if is_fibonacci(num):
    print(f"{num} belongs to the fibonacci sequence.")
else:
    print(f"{num} does not belong to the fibonacci sequence.")
