# Sum of Two Numbers
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
sum = first_number + second_number
print("The sum of number is:", sum)


#Area of a Circle
pi = 3.14
radius = float(input("Enter the radius of the circle: "))
area = pi * (radius ** 2)
print("The Area of the circle is:", area)


# Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")


#Exercise: Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
opr = input("Enter operation (+, -, *, /): ")
if opr == '+':
    print(num1 + num2)
elif opr == '-':
    print(num1 - num2)
elif opr == '*':
    print(num1 * num2)
elif opr == '/':
    if num2 != 0:  # Check if num2 is not zero to avoid division by zero error
        print(num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")


# Find the Largest Number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1>=num2 and num1>=num3:
    larg =num1
elif num2>=num1 and num2>=num3:
    larg= num2
else:
    larg=num3
print("Large number is " ,larg)


# Reverse a String
input = input("Enter a string: ")
reverse = input[::-1]
print("The reversed string is:", reverse)


#Count Vowels
input = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in input:
    if char in vowels:
        vowel_count += 1
print("The number of vowels is:", vowel_count)

#Fibonacci Sequence
n = int(input("How many terms? "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")  
    a, b = b, a + b 


#Check for Palindrome
string = input("Enter a string: ")

if string == string[::-1]:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
