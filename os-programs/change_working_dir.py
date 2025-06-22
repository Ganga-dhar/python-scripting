import os 

def change_working_directory(new_path):
    """Change the current working directory to new_path."""
    try:
        os.chdir(new_path)
        print(f"Changed working directory to: {new_path}")
    except FileNotFoundError:
        print(f"Directory '{new_path}' not found.")
    except NotADirectoryError:
        print(f"'{new_path}' is not a directory.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    new_directory = "demo_directory"  # Change this to the desired directory path
    change_working_directory(new_directory)
    # This will change the current working directory to the specified path
    # Ensure that the directory exists before running this script