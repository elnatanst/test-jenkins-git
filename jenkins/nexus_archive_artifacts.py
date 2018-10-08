import os
import shutil
import subprocess
import argparse

parser = argparse.ArgumentParser(description="script that store artifacts on the nexus server")
parser.add_argument("--url", dest='server_url', action='store', default=False)
parser.add_argument("--user", dest='username')
parser.add_argument('--pass', dest='password')
parser.add_argument('--rep', dest='repository')
parser.add_argument('--groupId', dest='groupId')
parser.add_argument('--artId', dest='artifactId')
parser.add_argument('--v', dest='version')
parser.add_argument('--file', dest='asset1')
parser.add_argument('--file_ext', dest='extension')
parser.add_argument('--method', dest='method')

cmd_params = parser.parse_args()
print(cmd_params)
repository = cmd_params.repository if cmd_params.repository else os.environ.get('NEXUS_REPOSITORY', 'Leadermass')
username = cmd_params.username if cmd_params.username else os.environ.get('NEXUS_USERNAME', 'elnatan')
password = cmd_params.password if cmd_params.password else os.environ.get('NEXUS_PASS', 'elnatan1988')
server_url = cmd_params.server_url if cmd_params.server_url else os.environ.get('NEXUS_SERVER',
                                                                                'http://nexus.ravtech.co.il:8081')
url = '{server_url}/service/rest/beta/components?repository={repository}'.format(server_url=server_url,
                                                                                 repository=repository)
groupId = cmd_params.groupId if cmd_params.groupId else os.environ.get('NEXUS_GROUPID', "Leadermass")
artifactId = cmd_params.artifactId if cmd_params.artifactId else os.environ.get('NEXUS_ARTIFACTSID', "Leadermass")
version = cmd_params.version if cmd_params.version else os.environ.get('VERSION', "1.3")
asset1 = cmd_params.asset1 if cmd_params.asset1 else os.environ.get('FILE_TO_ARCHIVE',
                                                                    "app/build/outputs/apk/debug/app-debug.apk")
extension = cmd_params.extension if cmd_params.extension else os.environ.get('FILE_EXTENSION', "apk")
method = cmd_params.method if cmd_params.method else os.environ.get('REQUEST_METHOD', 'POST')
print("......uploading###############")

curlcmd = r'curl -v -u {username}:{password} -X {post} {url} -F maven2.groupId={groupId} -F maven2.artifactId={' \
          r'artifactId} -F maven2.version={version} -F maven2.asset1=@{asset1} -F maven2.asset1.extension={' \
          r'extension}'.format(
    username=username, password=password, post=method, url=url, groupId=groupId, artifactId=artifactId, version=version,
    asset1=asset1, extension=extension)
subprocess.Popen(curlcmd.split())
