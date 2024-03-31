from agents import Developer

# Function to change content in the file
@Developer.register_for_llm(description="Change content of a file")
def change_content(file_path, changes):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for old, new in changes:
        lines = [line.replace(old, new) for line in lines]
    with open(file_path, 'w') as file:
        file.writelines(lines)