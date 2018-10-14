
import subprocess


f = subprocess.check_output("git --no-pager show -s --format=%ae".split())
# subprocess.check_output("echo .>out111.txt".split())
with open("out111.txt", 'w') as r:
    r.write('aa')
f = str(f.strip())
print(f)