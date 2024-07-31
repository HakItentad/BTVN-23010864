def is_bmp(filename):
    with open(filename, 'rb') as file:
        header = file.read(18)
    
    if header[:2] != b'BM':
        return False
    
    width = int.from_bytes(header[18:22], 'little')
    height = int.from_bytes(header[22:26], 'little')
    
    return width, height

filename = input("Nhập tên tập tin: ")
dimensions = is_bmp(filename)
if dimensions:
    print(f"Đây là tập tin ảnh Bitmap có kích thước: {dimensions[0]} x {dimensions[1]}")
else:
    print("Đây không phải là tập tin ảnh Bitmap.")
