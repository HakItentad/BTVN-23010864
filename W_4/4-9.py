def files_are_equal(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()

file1 = input("Nhập tên tập tin thứ nhất: ")
file2 = input("Nhập tên tập tin thứ hai: ")

if files_are_equal(file1, file2):
    print("Nội dung của hai tập tin giống nhau.")
else:
    print("Nội dung của hai tập tin khác nhau.")
