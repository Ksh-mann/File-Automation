import os
import shutil

# Get user input for the desired functionality
functionality = input("Choose a functionality (move, copy, or delete): ")

# Get user input for source directory and file name
source_directory = input("Enter the source directory: ")
file_name = input("Enter the file name: ")

# Get a list of all files in the source directory
files = os.listdir(source_directory)

# Flag to check if the file is found
file_found = False

# Perform the selected functionality based on user input
if functionality == "move":
    destination_directory = input("Enter the destination directory: ")
    for file in files:
        if file.startswith(file_name):
            source_path = os.path.join(source_directory, file)
            destination_path = os.path.join(destination_directory, file)
            shutil.move(source_path, destination_path)
            file_found = True
elif functionality == "copy":
    destination_directory = input("Enter the destination directory: ")
    for file in files:
        if file.startswith(file_name):
            source_path = os.path.join(source_directory, file)
            destination_path = os.path.join(destination_directory, file)
            shutil.copy(source_path, destination_path)
            file_found = True
elif functionality == "delete":
    for file in files:
        if file.startswith(file_name):
            file_path = os.path.join(source_directory, file)
            os.remove(file_path)
            file_found = True
else:
    print("Invalid functionality choice. Please choose either move, copy, or delete.")

# Throw an error if the file is not found for move, copy, and delete operations
if not file_found:
    raise FileNotFoundError("The specified file was not found in the source directory.")

# Print success message based on the selected functionality
if functionality == "move":
    print("File moved successfully.")
elif functionality == "copy":
    print("File copied successfully.")
elif functionality == "delete":
    print("File deleted successfully.")
