from agents import Developer

# Function to read a file
@Developer.register_for_llm(description="Read file content")
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()