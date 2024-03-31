from agents import Developer

# Function to remove lines from the file
@Developer.register_for_llm(description="Remove content from a file")
def remove_lines(file_path, line_indices):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line for i, line in enumerate(lines) if i not in line_indices]
    with open(file_path, 'w') as file:
        file.writelines(lines)