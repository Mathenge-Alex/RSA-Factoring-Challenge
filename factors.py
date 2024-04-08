import sys
from math import isqrt

def find_factors(n):
    for i in range(isqrt(n), 1, -1):
        if n % i == 0:
            return i, n // i
    return n, 1

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()

    for number in numbers:
        n = int(number.strip())
        p, q = find_factors(n)
        print(f"{n}={p}*{q}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    factorize_file(sys.argv[1])
