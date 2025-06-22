import subprocess
#subprocess.run(["tasklist"], ...)
process = subprocess.run(["pgrep", "nginx"], capture_output=True, text=True)
if process.returncode == 0:
    print("nginx is running")
else:
    print("nginx is not running")

########################################
import subprocess

usage = subprocess.run(["df", "-h"], capture_output=True, text=True)
print(usage.stdout)
###############################################
import subprocess

result = subprocess.run("ps aux | grep ssh", shell=True, capture_output=True, text=True)
print(result.stdout)
#############################################
import subprocess

ip = "8.8.8.8"
result = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True)
print("Output:\n", result.stdout)
print("Exit code:", result.returncode)
