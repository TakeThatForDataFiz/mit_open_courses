"""
finger_exer_roots.py -- func that returns root using multiple methods
"""

def find_root_exhaustive(guess, power, epsilon):
    low = min(-1, guess)
    high = max(1, guess)

    iters = 0
    for ans in range(low, high, 1):
        iters += 1
        if abs(ans**power - guess) < epsilon:
            print(f"Exhaustive Enumeration took {iters} iterations")
            return ans
    print(f"Exhaustive Enumeration took {iters} iterations")
    return None

def find_root_bisection(guess, power, epsilon):
    if guess < 0 and power % 2 == 0:
        return None # Negative number has no even-powered roots
    low = min(-1, guess)
    high = max(1, guess)
    iters = 0
    ans = (high + low) / 2

    while abs(ans**power - guess) >= epsilon:
        iters += 1
        if ans**power < guess:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    print(f"Bisection Search took {iters} iterations to caclulate.")
    return ans

def find_root_newton_raphson(guess, power, epsilon):
    ans = guess / power
    iters = 0
    while abs(ans**power - guess) >= epsilon:
        iters += 1
        ans = ans - (((ans**power) - guess) / (power*ans**(power-1)))
    print(f"Newton-Raphson took {iters} iterations to calculate.")
    return ans