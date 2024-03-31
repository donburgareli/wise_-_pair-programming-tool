from agents import Developer

# Function to append content to the file
@Developer.register_for_llm(description="Append content to a file")
def append_content(file_path, text_to_append):
    with open(file_path, 'a') as file:
        file.write(text_to_append)