class MyGame:
    # even or odd

    # A simple program that takes a number and prints whether it is even or odd

    def even_or_odd(self):
        print("A simple program that takes a number and prints whether it is even or odd")
        num = int(input("Enter Your Number: "))

        if num % 2 == 0:
            print("Your Number is Even")

        else:
            print("Your Number is Odd")

    # even or odd v 2.0

    # The program takes a set of numbers and prints the even for one and the odd ones for one

    def even_or_odd_v2(self):
        print("The program takes a set of numbers and prints the even for one and the odd ones for one")
        num = input("enter your number: ")

        list_numbers = list(num)

        for number in list_numbers:
            if int(number) % 2 == 0:
                print(f"your number is even {number}")

            elif int(number) % 2 != 0:
                print(f"your number is odd {number}")

    # even or odd v 3.0

    def even_or_odd_v3(self):
        print("print the numbers odd and even")

        choose = input("1:even or 2:odd: ")

        num = int(input("enter your number: "))

        if num % 2 == 0 and choose == "even":
            for i in range(0, num + 1, 2):
                print(i)
        elif num % 2 != 0 and choose == "odd":
            for i in range(1, num + 1, 2):
                print(i)

    # The program takes a number and prints all the numbers that this number can divide from 1 to 10

    def print_numbers(self):
        print("The program takes a number and prints all the numbers that this number can divide from 1 to 10")
        num = int(input("enter your number: "))

        for number in range(1, 11):
            if num % number == 0:
                print(number)

    def __init__(self):
        print("hello and welcome to my first game")
        choose = input("""
            press the game number
                1- even or odd v 1.0
                2- even or odd v 2.0
                3- even or odd v 3.0
                4- print numbers
                your choice: 
                """)
        if choose == "1":
            self.even_or_odd()
        elif choose == "2":
            self.even_or_odd_v2()
        elif choose == "3":
            self.even_or_odd_v3()
        elif choose == "4":
            self.print_numbers()


test = MyGame()
