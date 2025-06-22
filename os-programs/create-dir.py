import os


def create_directory(directory_name):
    """Create a new directory if it does not already exist."""
    try:
        os.mkdir(directory_name)
        print("Directory created successfully.")
    except FileExistsError:
        print("Directory already exists.")

if __name__ == "__main__":
    create_directory("demo_directory")
    # Change "demo_directory" to the desired directory name
    # This will create a new directory in the current working directory