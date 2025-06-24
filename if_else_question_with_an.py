# Write a program to check if a number is divisible by 3.

a=int(input("Enter a number : "))
if a%3==0:
    print(f"{a} This number is divisible by 3")
else:
    print(f"{a} This number is not divisible by 3")



# Input two numbers and print if they are equal or not.

num1=int(input("Enter a Num1 : "))
num2=int(input(f"Enter a Num2 : "))
if num1==num2:
    print("This number are equal")
else:
    print("This number are not equal")



#  Check if a number is a multiple of 4 or 6.
num=int(input("Enter a number : "))
if num%4==0 and num%6==0:
    print(f"the {num} is a multiple of 4 and 6 ")
else:
    print(f"the {num} is not a multiple of 4 and 6 ")



# Input a number and check if it is greater than 100.
number=int(input("Enter a number : "))
if number>=100:
    print("This number is greater than 100")
else:
    print("This number is not greater than 100")
    print("is less than 100")


# Input a number and print if it is a single-digit or multi-digit number.
number=int(input("Enter a number : "))
if -9 <= number <= 9:
    print("This number is single digit number")
else:
    print("This number is multi-digit number")


# Input three numbers and print the smallest.
num1=int(input("Enter a num1 : "))
num2=int(input("Enter a num2 : "))
num3=int(input("Etner a num3 : "))
if num1 <= num2 and num1 <= num3:
    print(f"{num1} is the smallest number")
elif num2 <= num1 and num2 <= num3:
    print(f"{num2} is the smallest number")
else:
    print(f"{num3} is the smallest number")



# Input a character and check if it is a digit or not.
character=input("Enter a value  : ")
character = input("Enter a value  : ")
if character.isdigit():
    print("This is digit")
else:
    print("This is not digit")


# Input a number and check if it is positive and even.

number = int(input("Enter a number : "))
if number > 0 and number % 2 == 0:
    print("This number is positive and even")
else:
    print("This number is not positive and even")




# Input a number and check if it is negative and odd.
number = int(input("Enter a number : "))
if number < 0 and  number % 2 != 0:
    print("This number is negetive and odd")
else:
    print("This number is not positive and odd")

