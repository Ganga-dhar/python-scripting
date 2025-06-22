import os


def walk_directory_tree(directory):
    """Walk through the directory tree and print all files and directories."""
    for root, dirs, files in os.walk(directory):
        print(f"Current Directory: {root}")
        for dir_name in dirs:
            print(f"  Directory: {dir_name}")
        for file_name in files:
            print(f"  File: {file_name}")

if __name__ == "__main__":
    directory_to_walk = "."  # Change this to the desired directory path
    walk_directory_tree(directory_to_walk)
    # This will walk through the current working directory by default
    # You can change the path to any directory you want to explore