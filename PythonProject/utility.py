# Math utilities
def add(a, b):
    return a + b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_even(n):
    return n % 2 == 0

# String utilities
def to_uppercase(text):
    return text.upper()

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')