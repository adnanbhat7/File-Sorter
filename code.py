import os 
import shutil  # Importing shutil module to perform high-level file operations

# Define the source directory where the files are located
source_directory = r"D:\portfolio project\python\File Sorter Py project\dataa"  # Change this path as needed

# Function to sort files based on their extensions
def sort_files(source_directory):
    # Get a list of all files in the source directory
    files = os.listdir(source_directory)

    # Iterate through each file in the directory
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(source_directory, file)

        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            # Extract the file extension and convert to lowercase
            file_extension = os.path.splitext(file)[1].lower()

            # Define the target folder name based on the file extension
            target_folder = os.path.join(source_directory, file_extension[1:] + "_files")

            # Create the target folder if it does not exist
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # Move the file to the target folder
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved {file} to {target_folder}")

# Function to check for duplicate files based on file names and sizes (optional enhancement)
def handle_duplicates(source_directory):
    seen_files = {}  # Dictionary to store files based on size and names to detect duplicates

    # Iterate through each file in the directory
    for file in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the file size
            file_size = os.path.getsize(file_path)

            # Combine file name and size to create a unique key
            file_key = (file, file_size)

            # Check if the file with the same name and size already exists
            if file_key in seen_files:
                print(f"Duplicate found: {file}")
                # Options to handle duplicates: Move, Delete, or Skip (user choice)
                duplicate_action = input("Choose action for duplicate (move/delete/skip): ").lower()
                if duplicate_action == 'move':
                    duplicates_dir = os.path.join(source_directory, 'duplicates')
                    if not os.path.exists(duplicates_dir):
                        os.makedirs(duplicates_dir)
                    shutil.move(file_path, os.path.join(duplicates_dir, file))
                elif duplicate_action == 'delete':
                    os.remove(file_path)
                    print(f"Deleted: {file}")
                else:
                    print(f"Skipped: {file}")
            else:
                # If not a duplicate, add it to the dictionary
                seen_files[file_key] = file_path

# Main function call to sort files
sort_files(source_directory)

# Optional: Uncomment the next line to handle duplicates
# handle_duplicates(source_directory)

print("File sorting completed!")
