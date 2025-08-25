from fileinput import filename
import os
from functions.get_files_info import get_files_info
from config import *

def get_files_content(working_directory, file_path):

    # Get absolute working directory
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    # Check if target file is within working directory
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'

    # Check if file exists
    if not os.path.isfile(target_file):
        return f'Error: "File not found or is not a regular file: "{file_path}"'

    try:
        max_chars = MAX_CHARS
        with open(target_file, 'r') as f:
            content = f.read(max_chars)
            extra = f.read(1)  # Try to read one more character to check for truncation

        extra_text = ""
        if extra:
            extra_text = f"Note: File content has been truncated to {max_chars} characters."

        return content + extra_text

    except Exception as e:
        return f"Error reading file: {e}"
