def division():
    try:
        num1=int(input("Enter a number: "))
        num2=int(input("Enter another number: "))
        divide=num1/num2
        print(f"The number after divisible is {divide}")
    except ZeroDivisionError:
        print("please choose any number except 0")
division()