import subprocess

email = subprocess.check_output("git --no-pager show -s --format=%ae".split())
print(email.decode())