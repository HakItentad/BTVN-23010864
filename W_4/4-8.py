import re

def extract_numbers(input_filename, output_filename):
    with open(input_filename, 'r') as infile:
        content = infile.read()
    
    numbers = re.findall(r'\d+', content)
    
    with open(output_filename, 'w') as outfile:
        for number in numbers:
            outfile.write(number + '\n')

input_filename = 'abc.txt'
output_filename = 'number.txt'
extract_numbers(input_filename, output_filename)
