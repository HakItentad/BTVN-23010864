def print_longest_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    
    longest_word = max(words, key=len)
    print("Từ dài nhất là:", longest_word)

filename = input("Nhập tên tập tin: ")
print_longest_word(filename)
