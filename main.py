import os
import shutil
import tkinter as tk
from tkinter import filedialog

def move_file():
    source_directory = source_entry.get()
    destination_directory = destination_entry.get()
    file_name = file_entry.get()

    files = os.listdir(source_directory)

    file_found = False

    for file in files:
        if file.startswith(file_name):
            source_path = os.path.join(source_directory, file)
            destination_path = os.path.join(destination_directory, file)
            shutil.move(source_path, destination_path)
            file_found = True

    if not file_found:
        result_label.config(text="The specified file was not found in the source directory.")
    else:
        result_label.config(text="File moved successfully.")

def copy_file():
    source_directory = source_entry.get()
    destination_directory = destination_entry.get()
    file_name = file_entry.get()

    files = os.listdir(source_directory)

    file_found = False

    for file in files:
        if file.startswith(file_name):
            source_path = os.path.join(source_directory, file)
            destination_path = os.path.join(destination_directory, file)
            shutil.copy(source_path, destination_path)
            file_found = True

    if not file_found:
        result_label.config(text="The specified file was not found in the source directory.")
    else:
        result_label.config(text="File copied successfully.")

def delete_file():
    source_directory = source_entry.get()
    file_name = file_entry.get()

    files = os.listdir(source_directory)

    file_found = False

    for file in files:
        if file.startswith(file_name):
            file_path = os.path.join(source_directory, file)
            os.remove(file_path)
            file_found = True

    if not file_found:
        result_label.config(text="The specified file was not found in the source directory.")
    else:
        result_label.config(text="File deleted successfully.")

def refresh_fields():
    source_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    file_entry.delete(0, tk.END)
    result_label.config(text="")

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

# Create and place the labels and entry fields
source_label = tk.Label(window, text="Source Directory:")
source_label.pack()
source_entry = tk.Entry(window)
source_entry.pack()

browse_source_button = tk.Button(window, text="Browse", command=browse_source_directory)
browse_source_button.pack()

destination_label = tk.Label(window, text="Destination Directory:")
destination_label.pack()
destination_entry = tk.Entry(window)
destination_entry.pack()

browse_destination_button = tk.Button(window, text="Browse", command=browse_destination_directory)
browse_destination_button.pack()

file_label = tk.Label(window, text="File Name:")
file_label.pack()
file_entry = tk.Entry(window)
file_entry.pack()

# Create and place the buttons
move_button = tk.Button(window, text="Move File", command=move_file)
move_button.pack()

copy_button = tk.Button(window, text="Copy File", command=copy_file)
copy_button.pack()

delete_button = tk.Button(window, text="Delete File", command=delete_file)
delete_button.pack()

refresh_button = tk.Button(window, text="Refresh", command=refresh_fields)
refresh_button.pack()

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main loop
window.mainloop()
