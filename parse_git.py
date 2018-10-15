import subprocess

email = subprocess.check_output("git --no-pager show -s --format=%ae")
print(str(email.decode()))