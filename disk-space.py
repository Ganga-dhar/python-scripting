import subprocess

result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
lines = result.stdout.splitlines()
if len(lines) > 1:
    usage = lines[1].split()[4]  # Example: "80%"
    percent = int(usage.strip('%'))
    if percent > 75:
        print("WARNING: Disk usage above 75%")



# import subprocess

# with open("deploy.log", "w") as logfile:
#     subprocess.run(["bash", "deploy.sh"], stdout=logfile, stderr=subprocess.STDOUT)