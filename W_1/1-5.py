import math

def is_fibo(N):
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    if N < 0:
        return False

    return is_perfect_square(5 * N * N + 4) or is_perfect_square(5 * N * N - 4)

N = int(input("Nhập số nguyên N: "))
result = is_fibo(N)
print("N có phải là số Fibonacci không?", result)
