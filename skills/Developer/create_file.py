import os
from agents import Developer

@Developer.register_for_llm(description="Create a file inside a folder")
def create_file_in_folder(folder_name, file_name):
    # Construct the full path
    file_path = os.path.join(folder_name, file_name)
    
    # Check if the folder exists
    if os.path.exists(folder_name):
        # Create the file
        with open(file_path, 'w') as file:
            file.write("# Your generated code goes here")
            print(f"File '{file_name}' created in '{folder_name}'.")
    else:
        print(f"The folder '{folder_name}' does not exist.")