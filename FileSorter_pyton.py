# Importing necessary modules
import os
import shutil

# Path to the directory containing the files you want to sort
path = r"D:/portfolio project/File Sorter Py project/dataa/"

# Step 1: List the files in the specified directory
file_names = os.listdir(path)
print(file_names)  # Outputs the list of files in the directory

# Step 2: Check if folders for file types exist, if not, create them
# List of folder names where files will be sorted
folder_names = ["image files", "video files", "excel files", "PDF files"]

# Check if each folder exists; if not, create it.
for folder in folder_names:
    if not os.path.exists(os.path.join(path, folder)):
        os.makedirs(os.path.join(path, folder))

# Step 3: Organize files by moving them to respective folders based on file extension
for file in file_names:
    # If the file is a .jpg (image file)
    if ".jpg" in file:
        if not os.path.exists(os.path.join(path, "image files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "image files", file))
        else:
            os.remove(os.path.join(path, file))  # If the file already exists in the folder, delete the duplicate

    # If the file is an .xlsx (Excel file)
    elif ".xlsx" in file:
        if not os.path.exists(os.path.join(path, "excel files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "excel files", file))
        else:
            os.remove(os.path.join(path, file))  # Remove duplicate

    # If the file is an .mp4 (video file)
    elif ".mp4" in file:
        if not os.path.exists(os.path.join(path, "video files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "video files", file))
        else:
            os.remove(os.path.join(path, file))  # Remove duplicate

    # If the file is a .pdf (PDF file)
    elif ".pdf" in file:
        if not os.path.exists(os.path.join(path, "PDF files", file)):
            shutil.move(os.path.join(path, file), os.path.join(path, "PDF files", file))
        else:
            os.remove(os.path.join(path, file))  # Remove duplicate

# Step 4: Confirm that the sorting is complete.
print("Done")

# Step 5: List the sorted folders to verify
sorted_folders = os.listdir(path)
print(sorted_folders)  # Outputs the list of folders after sorting

