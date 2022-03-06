# is Prime?

def isPrime(x):
    if x == 1:
        return True
    else:
        for i in range(2, int(x**0.5)):
            if x % i == 0:
                return False
    return True

print(isPrime(2))
print(isPrime(222))
