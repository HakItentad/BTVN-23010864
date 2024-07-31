def find_max_and_print_remaining(a, b, c):
    max_value = max(a, b, c)
    numbers = [a, b, c]
    max_count = numbers.count(max_value)
    
    if max_count >= 2:
        numbers.remove(max_value)
        remaining_value = numbers[0] if numbers else None
        print("Giá trị còn lại là:", remaining_value)
    else:
        print("Giá trị lớn nhất là:", max_value)

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

find_max_and_print_remaining(a, b, c)
