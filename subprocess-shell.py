import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True, shell=True)
print(result.stdout)