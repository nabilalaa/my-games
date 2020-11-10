# even or odd v 3.0

def even_or_odd_v3():
    choose = input("1:even or 2:odd: ")

    num = int(input("enter your number: "))

    if num % 2 == 0 and choose == "even":
        for i in range(0, num + 1, 2):
            print(i)
    elif num % 2 != 0 and choose == "odd":
        for i in range(1, num + 1, 2):
            print(i)


even_or_odd_v3()
