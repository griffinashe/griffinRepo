"""Find all the Prime Numbers up to a given number.
"""

n = raw_input("Give me all the primes up to: ")
num = int(n)

for p in range(2, num+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print p
