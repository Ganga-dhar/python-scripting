import os 

def current_working_directory():
    """Get the current working directory."""
    return os.getcwd()
if __name__ == "__main__":
    cwd = current_working_directory()
    print(f"Current working directory: {cwd}")  