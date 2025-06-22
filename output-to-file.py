import subprocess

with open("output.txt", "w") as f:
    subprocess.run(["tasklist"], stdout=f)


