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
<<<<<<< Updated upstream
elif functionality == "copy":
    destination_directory = input("Enter the destination directory: ")
=======

    if not file_found:
        result_label.config(text="The specified file was not found in the source directory.", fg="red")
    else:
        result_label.config(text="File moved successfully.", fg="green")

def copy_file():
    source_directory = source_entry.get()
    destination_directory = destination_entry.get()
    file_name = file_entry.get()

    files = os.listdir(source_directory)

    file_found = False

>>>>>>> Stashed changes
    for file in files:
        if file.startswith(file_name):
            source_path = os.path.join(source_directory, file)
            destination_path = os.path.join(destination_directory, file)
            shutil.copy(source_path, destination_path)
            file_found = True
<<<<<<< Updated upstream
elif functionality == "delete":
=======

    if not file_found:
        result_label.config(text="The specified file was not found in the source directory.", fg="red")
    else:
        result_label.config(text="File copied successfully.", fg="green")

def delete_file():
    source_directory = source_entry.get()
    file_name = file_entry.get()

    files = os.listdir(source_directory)

    file_found = False

>>>>>>> Stashed changes
    for file in files:
        if file.startswith(file_name):
            file_path = os.path.join(source_directory, file)
            os.remove(file_path)
            file_found = True
else:
    print("Invalid functionality choice. Please choose either move, copy, or delete.")

<<<<<<< Updated upstream
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
=======
    if not file_found:
        result_label.config(text="The specified file was not found in the source directory.", fg="red")
    else:
        result_label.config(text="File deleted successfully.", fg="green")

def refresh_fields():
    source_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    file_entry.delete(0, tk.END)
    result_label.config(text="", fg="black")

def browse_source_directory():
    source_directory = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_directory)

def browse_destination_directory():
    destination_directory = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, destination_directory)

# Create the main window
window = tk.Tk()
window.title("File Management Program")

# Set the background color
window.configure(bg="#000000")

# Set the font styles
title_font = ("Arial", 20, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# Create and place the title label
title_label = tk.Label(window, text="File Manager", font=title_font, fg="#00FF00", bg="#000000")
title_label.pack(pady=20)

# Create and place the labels and entry fields
source_label = tk.Label(window, text="Source Directory:", font=label_font, fg="#00FF00", bg="#000000")
source_label.pack()
source_entry = tk.Entry(window, font=label_font)
source_entry.pack()

browse_source_button = tk.Button(window, text="Browse", font=button_font, command=browse_source_directory)
browse_source_button.pack(pady=10)

destination_label = tk.Label(window, text="Destination Directory:", font=label_font, fg="#00FF00", bg="#000000")
destination_label.pack()
destination_entry = tk.Entry(window, font=label_font)
destination_entry.pack()

browse_destination_button = tk.Button(window, text="Browse", font=button_font, command=browse_destination_directory)
browse_destination_button.pack(pady=10)

file_label = tk.Label(window, text="File Name:", font=label_font, fg="#00FF00", bg="#000000")
file_label.pack()
file_entry = tk.Entry(window, font=label_font)
file_entry.pack()

# Create and place the buttons
move_button = tk.Button(window, text="Move File", font=button_font, command=move_file)
move_button.pack(pady=10)

copy_button = tk.Button(window, text="Copy File", font=button_font, command=copy_file)
copy_button.pack(pady=10)

delete_button = tk.Button(window, text="Delete File", font=button_font, command=delete_file)
delete_button.pack(pady=10)

refresh_button = tk.Button(window, text="Refresh", font=button_font, command=refresh_fields)
refresh_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(window, text="", font=label_font, fg="black", bg="#000000")
result_label.pack(pady=20)

# Run the main window loop
window.mainloop()
>>>>>>> Stashed changes
