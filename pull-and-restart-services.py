import subprocess
import os

local_path = "G:/Devops/repos/terraform-aws-ec2-instance"

# Clone if the repo doesn't exist
if not os.path.exists(local_path):
    subprocess.run(["git", "clone", "https://github.com/cloudposse/terraform-aws-ec2-instance.git", local_path], check=True)

# Now pull latest changes
subprocess.run(["git", "pull"], cwd=local_path, check=True)

# Restart service or run anything else
# subprocess.run(["systemctl", "restart", "your-service-name"], check=True)



# # Restart systemd service
# subprocess.run(["sudo", "systemctl", "restart", "myapp.service"], check=True)

# # Check status
# status = subprocess.run(["systemctl", "status", "myapp"], capture_output=True, text=True)
# print(status.stdout)