import subprocess

subprocess.run(["dpkg", "-l"])  # Debian/Ubuntu
# Or subprocess.run(["rpm", "-qa"]) for RedHat/CentOS
