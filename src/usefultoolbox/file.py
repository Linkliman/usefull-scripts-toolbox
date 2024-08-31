import os
import shutil


# File Operations
def read_file(file_path):
    """Read the content of a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, "r") as file:
        content = file.read()
    return content


def write_file(file_path, content, mode="w"):
    """Write content to a file. Supports writing ('w') and appending ('a')."""
    with open(file_path, mode) as file:
        file.write(content)


def copy_file(source_path, destination_path):
    """Copy a file from source to destination."""
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"The source file {source_path} does not exist.")

    shutil.copy(source_path, destination_path)


def move_file(source_path, destination_path):
    """Move a file from source to destination."""
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"The source file {source_path} does not exist.")

    shutil.move(source_path, destination_path)


def delete_file(file_path):
    """Delete a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    os.remove(file_path)


# Directory Operations
def create_directory(directory_path):
    """Create a directory. Does nothing if the directory already exists."""
    os.makedirs(directory_path, exist_ok=True)


def list_directory(directory_path):
    """List all files and directories in a directory."""
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory {directory_path} does not exist.")

    return os.listdir(directory_path)


def delete_directory(directory_path):
    """Delete a directory and all its contents."""
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory {directory_path} does not exist.")

    shutil.rmtree(directory_path)


# Utility Functions
def file_exists(file_path):
    """Check if a file exists."""
    return os.path.isfile(file_path)


def directory_exists(directory_path):
    """Check if a directory exists."""
    return os.path.isdir(directory_path)
