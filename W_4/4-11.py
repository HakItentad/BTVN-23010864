def is_jpg(filename):
    with open(filename, 'rb') as file:
        data = file.read()
    
    return data[6:10] == b'JFIF'

filename = input("Nhập tên tập tin: ")
if is_jpg(filename):
    print("Đây là tập tin ảnh JPG.")
else:
    print("Đây không phải là tập tin ảnh JPG.")
