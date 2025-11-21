import random

numbers = [random.randint(1, 1000001) for _ in range(100)]




# Write a function that checks whether a number is prime. 
# Define a function called is_prime that takes one integer as input.
def is_prime(n):
    # A prime number is a number 
    # greater than 1 
    # that has no divisors other than 1 and itself.
    if n <= 1:
        return False
    # Return True if the number is prime and False otherwise.
    # Use a loop to check divisibility
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for num in numbers:
    print(num, is_prime(num))