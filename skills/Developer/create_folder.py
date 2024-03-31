import os
from agents import Developer

@Developer._AGENT.register_for_execution()
@Developer._AGENT.register_for_llm(description="Create folder")
def create_folder(folder_name):
    # Check if the folder already exists
    if not os.path.exists('generated/' + folder_name):
        # Create the folder
        os.makedirs('generated'/ + folder_name)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")