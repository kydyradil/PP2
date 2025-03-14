#1 
import os

def list_contents(path):
    try:
        
        entries = os.listdir(path)
        
        
        directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
        files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]
        
        print("Directories:")
        for directory in directories:
            print(directory)
        
        print("\nFiles:")
        for file in files:
            print(file)
        
        print("\nAll Entries:")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print("The file does not exist")
    except PermissionError:
        print("Permission denied to access the specified path ")

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    list_contents(path)

#2 
import os

def check_access(path):
    try:
        print(f"Checking access for: {path}\n")
        
        if os.path.exists(path):
            print("The path exists")
        else:
            print("The path does not exist")
            return
        
        if os.access(path, os.R_OK):
            print("The path is readable")
        else:
            print("The path is not readable")
        
        if os.access(path, os.W_OK):
            print("The path is writable")
        else:
            print("The path is not writable")
        
        if os.access(path, os.X_OK):
            print("The path is executable")
        else:
            print("The path is not executable")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    path = input("Enter the directory or file path: ")
    check_access(path)
#3
import os

def check_path(path):
    if os.path.exists(path):
        print(f"The path exists: {path}\n")
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        print(f"Directory portion: {directory}")
        print(f"Filename portion: {filename}")
    else:
        print("The specified path does not exist")

if __name__ == "__main__":
    path = input("Enter the path to check: ")
    check_path(path)
#4
import os

def count_lines(file_path):
    if not os.path.exists(file_path):
        print("The specified file does not exist")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for _ in file)
        print(f"The file '{file_path}' has {line_count} lines.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the text file path: ")
    count_lines(file_path)
#5
import os

def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"List successfully written to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path to write to: ")
    data_list = input("Enter list items separated by commas: ").split(',')
    write_list_to_file(file_path, data_list)
  #6
  import os
import string

def generate_text_files(directory):
    os.makedirs(directory, exist_ok=True)
    
    for letter in string.ascii_uppercase:
        file_path = os.path.join(directory, f"{letter}.txt")
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"This is {letter}.txt\n")
            print(f"Created: {file_path}")
        except Exception as e:
            print(f"An error occurred while creating {file_path}: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory to save files: ")
    generate_text_files(directory)
#7
import shutil

def copy_file(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print(f"File copied from '{source_path}' to '{destination_path}'.")
    except FileNotFoundError:
        print("The source file does not exist")
    except PermissionError:
        print("Permission denied. Cannot copy the file")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    source = input("Enter the source file path: ")
    destination = input("Enter the destination file path: ")
    copy_file(source, destination)
#8
import os

def delete_file(file_path):
    if not os.path.exists(file_path):
        print("The specified file does not exist.")
        return
    
    if not os.access(file_path, os.W_OK):
        print("Permission denied. Cannot delete the file.")
        return
    
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path to delete: ")
    delete_file(file_path)
