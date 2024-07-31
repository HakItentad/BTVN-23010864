import math

def F(N):
    return sum(math.factorial(i) for i in range(1, N + 1))

N = int(input("Nhập số nguyên N: "))
result = F(N)
print("Giá trị của F(N) là:", result)
