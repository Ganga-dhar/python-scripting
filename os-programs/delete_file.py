import os 


def delete_file(file_name):
    """Delete a file if it exists."""
    if not os.path.isfile(file_name):
        print(f"File '{file_name}' does not exist.")
        return
    else:
        try:
            os.remove(file_name)
            print(f"File '{file_name}' deleted successfully.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    delete_file("file_to_delete.txt")