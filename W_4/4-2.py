def print_last_5_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for line in lines[-5:]:
        print(line, end='')

filename = input("Nhập tên tập tin: ")
print_last_5_lines(filename)
