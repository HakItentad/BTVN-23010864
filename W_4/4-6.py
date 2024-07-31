from collections import Counter
import re

def print_word_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()
    
    words = re.findall(r'\b\w+\b', text.lower())
    frequency = Counter(words)
    
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    print("Tần suất xuất hiện của các từ:")
    for word, count in sorted_frequency:
        print(f"{word}: {count}")

filename = input("Nhập tên tập tin: ")
print_word_frequency(filename)
