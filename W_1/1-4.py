def total(N):
    return sum(int(digit) for digit in str(abs(N)))

N = int(input("Nhập số nguyên N: "))
result = total(N)
print("Tổng các chữ số của N là:", result)
