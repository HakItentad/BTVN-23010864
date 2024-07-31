def area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

x1 = float(input("Nhập tọa độ x1: "))
y1 = float(input("Nhập tọa độ y1: "))
x2 = float(input("Nhập tọa độ x2: "))
y2 = float(input("Nhập tọa độ y2: "))
x3 = float(input("Nhập tọa độ x3: "))
y3 = float(input("Nhập tọa độ y3: "))

result = area(x1, y1, x2, y2, x3, y3)
print("Diện tích tam giác là:", result)
