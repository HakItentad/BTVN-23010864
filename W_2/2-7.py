def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit) if is_prime[p]]

limit = 1000000
primes = sieve_of_eratosthenes(limit)
P = tuple(primes)

print("Số lượng số nguyên tố nhỏ hơn 1 triệu:", len(P))
