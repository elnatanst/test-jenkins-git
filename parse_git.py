
import subprocess


f = subprocess.check_output("git --no-pager show -s --format=%ae".split())

f = str(f.strip())
print(f)