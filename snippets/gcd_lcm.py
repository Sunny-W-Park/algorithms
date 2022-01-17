#Greatest Common Divisor (GCD)

def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

#Least Common Multiple (LCM)

def lcm(A, B):
    return A * B // gcd(A, B)
