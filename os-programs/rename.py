import os


def rename_file(old_name, new_name):
    """Rename a file from old_name to new_name."""
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}.")
    except FileNotFoundError:
        print(f"File '{old_name}' not found.")
    except FileExistsError:
        print(f"File '{new_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    rename_file("old_file.txt", "new_file.txt")