def average(a, b, c, d, e):
    return (a + b + c + d + e) / 5

a = float(input("Nhập giá trị thứ nhất: "))
b = float(input("Nhập giá trị thứ hai: "))
c = float(input("Nhập giá trị thứ ba: "))
d = float(input("Nhập giá trị thứ tư: "))
e = float(input("Nhập giá trị thứ năm: "))

result = average(a, b, c, d, e)
print("Giá trị trung bình cộng là:", result)
