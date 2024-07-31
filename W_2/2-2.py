def process_binary_strings(input_string):
    binary_strings = input_string.split(',')
    return binary_strings

input_string = input("Nhập các chuỗi nhị phân, nối nhau bằng dấu phẩy: ")
binary_strings = process_binary_strings(input_string)
print("Các chuỗi nhị phân đã nhập là:")
for binary in binary_strings:
    print(binary)
