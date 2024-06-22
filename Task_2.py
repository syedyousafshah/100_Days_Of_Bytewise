#Palindrome Checker (Word)
word = input("Enter a word: ")
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

#FizzBuzz
for number in range(0, 100):
    
    if number % 3 == 0 and number % 5 == 0:
        print("boomboom")
    elif number % 3 == 0:
        print("Hawww")
    elif number % 5 == 0:
        print("Buzzzzzz")
    else:
        print(number)


#Nth Fibonacci Number
n = int(input("Enter the term number to find the nth Fibonacci number: "))
def fibo(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

n_fibo = fibo(n)
print(f"The {n}th Fibonacci number is {n_fibo}.")

#Prime Number Checker
num = int(input("Enter a number to check if it is prime: "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
result = "is" if is_prime(num) else "is not"
print(f"{num} {result} a prime number.")

#Guess the Number Game
import random
guess = random.randint(1, 100)
def number():
    print("Welcome to the Guess the Number Game!")
    print("I have generated a random number between 1 and 100.")
    print("Can you guess what it is?")

    while True:
        try:
            user = int(input("Enter your guess: "))
            if user < guess:
                print("Your guess is too low. Try again!")
            elif user >guess:
                print("Your guess is too high. Try again!")
            else:
                print(f"Congratulations! You guessed the correct number: {guess}")
                break  
        except ValueError:
            print("Invalid input. Please enter an integer.")
number()


#List Comprehension
sq = [x**2 for x in range(1, 11)]
print(sq)


# Temperature Converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
kelvin = celsius_to_kelvin(celsius)

print(f"{celsius} degrees Celsius equal to {fahrenheit} degrees Fahrenheit and {kelvin} degrees Kelvin.")
