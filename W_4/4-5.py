from collections import Counter
import re

def print_letter_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()
    
    letters = re.findall(r'[a-zA-Z]', text)
    frequency = Counter(letters)
    
    print("Số lần xuất hiện của các chữ cái:")
    for letter, count in frequency.items():
        print(f"{letter}: {count}")

filename = input("Nhập tên tập tin: ")
print_letter_frequency(filename)
