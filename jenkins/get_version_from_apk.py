import subprocess
import argparse
parser = argparse.ArgumentParser(description="get apk file path and print version name")
parser.add_argument("-file", dest="apk_path")
apk_file = parser.parse_args().apk_path
apk_properties = subprocess.check_output("aapt dump badging {} | grep version".format(apk_file).split()).decode().split()
for i in apk_properties:
    if 'versionName=' in i:
        print(i.split('=\'')[1][:-1])
