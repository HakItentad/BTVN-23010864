def sort_words(input_string):
    words = input_string.split()
    sorted_words = sorted(words)
    return sorted_words

input_string = input("Nhập chuỗi từ tiếng Anh: ")
sorted_words = sort_words(input_string)
print("Các từ theo thứ tự từ điển là:")
for word in sorted_words:
    print(word)
