def convert_to_uppercase(input_filename, output_filename):
    with open(input_filename, 'r') as infile:
        content = infile.read()
    
    upper_content = content.upper()
    
    with open(output_filename, 'w') as outfile:
        outfile.write(upper_content)

input_filename = 'abc.txt'
output_filename = 'abc_upper.txt'
convert_to_uppercase(input_filename, output_filename)
