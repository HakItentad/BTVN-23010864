def sum_of_divisors(x):
    total = 0
    for i in range(1, x):
        if x % i == 0:
            total += i
    return total

def find_numbers(n):
    result = []
    for i in range(1, n):
        if sum_of_divisors(i) < i:
            result.append(i)
    return result

n = int(input("Nhập số nguyên n: "))
numbers = find_numbers(n)
print("Các số nguyên dương nhỏ hơn n có tổng các ước nhỏ hơn chính nó là:")
for number in numbers:
    print(number)
