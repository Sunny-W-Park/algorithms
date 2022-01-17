#Binominal Coefficient (이항 계수)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def binomial_coefficient(N, K):
    return factorial(N) // (factorial(N - K) * factorial(K))



