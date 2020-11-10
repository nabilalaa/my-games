# even or odd v 2.0

# The program takes a set of numbers and prints the even for one and the odd ones for one

def even_or_odd_v2():
    num = input("enter your number: ")

    list_numbers = list(num)

    for number in list_numbers:
        if int(number) % 2 == 0:
            print(f"your number is even {number}")

        elif int(number) % 2 != 0:
            print(f"your number is odd {number}")


even_or_odd_v2()