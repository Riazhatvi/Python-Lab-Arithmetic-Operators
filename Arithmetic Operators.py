# Write a program that asks the user about the number of values he/she wants to enter. Than
# enter the values as per the required number, calculate its sum and identify the smallest value among
# them. The sample output is as follow:
# Enter the number of values to be input: 5
# Enter the number: 20
# Enter the number: 10
# Enter the number: 50
# Enter the number: 4
# Enter the number: 65
# The sum is: 149
# The smallest value of entered numbers is 4
def main():
    num_values = int(input("Enter the number of values to be input: "))
    values = []
    
    for i in range(num_values):
        value = float(input("Enter the number: "))
        values.append(value)
    
    # Calculate sum
    total_sum = sum(values)
    
    # Find the smallest value
    smallest_value = min(values)
    
    print("The sum is:", total_sum)
    print("The smallest value of entered numbers is", smallest_value)


# The factorial function is used frequently in probability problems. The factorial of a positive
# integer n (written n! and pronounced “n factorial”) is equal to the product of the positive integers
# from 1 to n.
# Write a function factorial that accepts an integer as parameter and returns its factorial.
# Using the factorial function, write a program that evaluates the factorials of the integers from 1 to 5.
# Print the results in tabular format as following.

if __name__ == "__main__":
    main()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("Integer   Factorial")
    print("--------------------")
    
    for i in range(1, 6):
        result = factorial(i)
        print(f"{i}         {result}")

if __name__ == "__main__":
    main()

# Write a program that plays an incredibly stupid number-guessing game. The user will try to
# guess the secret number until they get it right. That means it will keep looping as long as the guess is
# different from the secret number. You must store the secret number in a variable, and use that
# variable throughout. The secret number itself must not appear in the program at all, except in the
# one line where you store it into a variable. Sample output is as following:
# I have chosen a number between 1 and 10. Try to guess it.
# Your guess: 5
# That is incorrect. Guess again.
# Your guess: 4
# That is incorrect. Guess again.
# our guess: 8
# That is incorrect. Guess again.
# Your guess: 6
# That's right! You guessed it.
import random

def main():
    secret_number = random.randint(1, 10)
    print("I have chosen a number between 1 and 10. Try to guess it.")
    
    while True:
        guess = int(input("Your guess: "))
        
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("That is incorrect. Guess again.")

if __name__ == "__main__":
    main()
# The greatest common divisor (GCD) of two integers is the largest integer that evenly
# divides each of the two numbers. Write function gcd that returns the greatest common divisor of
# two integers.
# Use the gcd function in your program to determine the GCD of the numbers in the sample output:
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    num1 = 48
    num2 = 18
    
    result = gcd(num1, num2)
    print("The greatest common divisor of", num1, "and", num2, "is:", result)

if __name__ == "__main__":
    main()

# An integer is said to be prime if it is divisible only by 1 and itself. For example, 2, 3, 5 and 7
# are prime, but 4, 6, 8 and 9 are not.
# a) Write a function that determines if a number is prime.
# b) Use this function in a program that determines and prints all the prime numbers between 1 and
# 10,000.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("Prime numbers between 1 and 10,000:")
    
    for num in range(1, 10001):
        if is_prime(num):
            print(num, end=' ')

if __name__ == "__main__":
    main()
# Prime numbers between 1 and 10,000:
# 2 3 5 7 11 13 ... (truncated for brevity)

# Write a code that prints on screen all the 4-digit Armstrong numbers.
def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    return num == sum_of_powers

def main():
    print("All 4-digit Armstrong numbers:")
    
    for num in range(1000, 10000):
        if is_armstrong_number(num):
            print(num)

if __name__ == "__main__":
    main()
# Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. The
# output should look like the output below:
def main():
    for i in range(1, 101):
        print(f"Line {i}: Riaz Khan")

if __name__ == "__main__":
    main()
# Write a program that prints out a list of the integers from 1 to 20 and their squares. The
# output should look like this:
def main():
    print("Number | Square")
    print("--------------")
    for i in range(1, 21):
        square = i * i
        print(f"{i:6} | {square}")

if __name__ == "__main__":
    main()
# Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89.
def main():
    for num in range(8, 90, 3):
        print(num)

if __name__ == "__main__":
    main()
# Write a program that asks the user for their name and how many times to print it. The
# program should print out the user’s name the specified number of times.
def main():
    name = input("Enter your name: ")
    num_times = int(input("Enter the number of times to print your name: "))
    
    for i in range(num_times):
        print(name)

if __name__ == "__main__":
    main()
# Use a for loop to print a box like the one below. Allow the user to specify how wide and
# how high the box should be.

def print_box(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print("*" * width)
        else:
            print("*" + " " * (width - 2) + "*")

def main():
    width = int(input("Enter the width of the box: "))
    height = int(input("Enter the height of the box: "))
    
    print_box(width, height)

if __name__ == "__main__":
    main()

# Use a for loop to print a triangle like the one below. Allow the user to specify how high the
# triangle should be.
def print_triangle(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))

def main():
    height = int(input("Enter the height of the triangle: "))
    print_triangle(height)

if __name__ == "__main__":
    main()

# Use for loops to print a diamond like the one below. Allow the user to specify how high the
# diamond should be.
def print_diamond(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))

    for i in range(height - 1, 0, -1):
        print(" " * (height - i) + "*" * (2 * i - 1))

def main():
    height = int(input("Enter the height of the diamond: "))
    print_diamond(height)

if __name__ == "__main__":
    main()

# Write a program that prints a giant letter A like the one below. Allow the user to specify
# how large the letter should be.
def print_diamond(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))

    for i in range(height - 1, 0, -1):
        print(" " * (height - i) + "*" * (2 * i - 1))

def main():
    height = int(input("Enter the height of the diamond: "))
    print_diamond(height)

if __name__ == "__main__":
    main()
