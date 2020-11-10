# The program takes a number and prints all the numbers that this number can divide from 1 to 10

def print_numbers():
    num = int(input("enter your number: "))

    for number in range(1,11):
        if num % number == 0:
            print(number)


print_numbers()