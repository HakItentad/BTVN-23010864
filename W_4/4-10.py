import os

def group_files_by_content(directory):
    file_groups = {}
    file_contents = {}
    
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            with open(os.path.join(directory, filename), 'r') as file:
                content = file.read()
            file_contents[filename] = content
    
    groups = {}
    for filename, content in file_contents.items():
        if content not in groups:
            groups[content] = []
        groups[content].append(filename)
    
    print("Các nhóm tập tin có cùng nội dung:")
    group_number = 1
    for group in groups.values():
        print(f"Nhóm {group_number}: {', '.join(group)}")
        group_number += 1

directory = '.'
group_files_by_content(directory)
