def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

prime_l = []
for p in range(1, 616):
    if is_prime(p):
        print(f"{p} is a prime number")
        prime_l.append(p)
    else:
        print(f"{p} is not a prime number")
    
print(prime_l)
