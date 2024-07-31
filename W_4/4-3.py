def print_longest_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    longest_line = max(lines, key=len)
    print("Dòng dài nhất là:", longest_line.strip())

filename = input("Nhập tên tập tin: ")
print_longest_line(filename)
