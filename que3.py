try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That was not a valid number.")
else:
    print(f"You entered the number {number}.")
