import subprocess
import sys
# print("get email.....")
email = subprocess.check_output("git --no-pager show -s --format=%ae".split())
# email = "aaaa"
sys.stdout.write(email.decode())
# print(email.decode())