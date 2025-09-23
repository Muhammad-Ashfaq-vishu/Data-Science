# Q no 1: Print numbers from 1 to 20 using a for loop.

for i in range(1, 21):
    print(i)


# Q no 2: Print even numbers from 2 to 50 using a while loop.

count = 2
while count <= 50:
    print(count)
    count += 2


# Q no 3: Sum of numbers from 1 to 100.

sum = 0
for i in range(1, 101):
    sum += i
print(sum)


# Q no 4: Print the multiplication table of a number input by user.

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# Q no 5: Factorial of a number using loop.

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print(factorial(num))


# 9. Function to check if number is prime.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 10. Function to return max of 3 numbers.

def max_of_three(a, b, c):
    return max(a, b, c)


# 11. Function to calculate simple interest.

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


# 12. Function to calculate factorial (using loop inside function).

def factorial_loop(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


# 13. Function that accepts a list and returns sum of even numbers only.

def sum_of_even(nums):
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
    return sum


# 14. Function that prints if number is positive, negative, or zero.

def sign(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

