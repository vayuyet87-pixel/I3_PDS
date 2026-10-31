def is_prime(n):
    if n<2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
print("Primes below 50:", end=" ")
prime_below_50 = []
for i in range (2, 50):
    if is_prime(i):
        prime_below_50.append(str(i))
print(" ".join(prime_below_50))
prime_below_100_count = sum(1 for i in range(2, 100) if is_prime(i))
print(f"Total primes below 100: {prime_below_100_count}")

def goldbach(n):
    for p in range (2,n):
        if is_prime(p):
            q = n - p
            if is_prime(q):
                return (p,q)
    return None
for n in range(4, 31, 2):
    pair = goldbach(n)
    if pair:
        print(f"{n} = {pair[0]} + {pair[1]}")

all_hold = True
for n in range (4, 10001, 2):
    found = False
    for p in range(2, n):
        if is_prime(p):
            q = n-p
            if is_prime(q):
                found = True
                break
    if not found:
        all_hold = False
        break
print(f"Goldbach holds for every even number from 4 to 10000: {all_hold}")