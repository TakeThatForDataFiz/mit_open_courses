"""
finger_exer_prime.py -- create a function that prints the sum of all prime numbers greater than
2 and less than 1000
"""

def is_prime(num: int):
    if num in (0, 1):
        return False
    if num % 2 == 0:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def get_sum_primes():
    prime_sum = 0
    for i in range(3, 1000, 2):
        if is_prime(i):
            prime_sum += i
    return prime_sum


if __name__ == "__main__":
    print(f"The Sum of primes greater than 2 and less than 1000 is {get_sum_primes()}")