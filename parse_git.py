import logging
import subprocess
import os

f = subprocess.check_output("git --no-pager show -s --format=%ae".split())
# subprocess.check_output("echo .>out111.txt".split())
with open("out111.txt", 'w') as r:
    r.write('aa')
f = str(f.strip().decode())
os.environ["author_email"] = f
logging.info("commiter {}".format(f))
print(f)