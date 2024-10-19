# File Sorter by File Type

This project is a Python-based file sorter that organizes files in a given directory based on their file types (extensions). It helps declutter directories by sorting files into relevant folders automatically.

## Features
- Sorts files into folders based on common file types:
  - Image files (`.jpg`)
  - Video files (`.mp4`)
  - Excel files (`.xlsx`)
  - PDF files (`.pdf`)
- Creates new folders for each file type if they don’t exist.
- Handles duplicate files by removing them if they already exist in the target folder.

## Files in the Repository
- **Automatic file Sorter.ipynb**: The Jupyter Notebook containing the file sorter logic and explanations.
- **FileSorter_pyton.py**: The Python script version of the file sorter for easy execution.
- **README.md**: This documentation file.

## Prerequisites
- Python 3.x installed on your machine.

## Installation
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/adnanbhat7/File-Sorter.git
    ```

2. Navigate to the project directory:
    ```bash
    cd File-Sorter
    ```

3. Make sure Python is installed. You can check by running:
    ```bash
    python --version
    ```

## Usage
1. For the Python script, set the path to the directory where you want to sort files by updating the `path` variable in the `FileSorter_pyton.py` file:
    ```python
    path = r"D:/portfolio project/File Sorter Py project/dataa/"
    ```

2. Run the Python script:
    ```bash
    python FileSorter_pyton.py
    ```

3. Alternatively, you can open and run the `Automatic file Sorter.ipynb` in a Jupyter Notebook environment.

4. The script will automatically sort files into folders based on their file types (`.jpg`, `.mp4`, `.xlsx`, `.pdf`).
