from paramiko import SSHClient
from scp import SCPClient
import os
from dotenv import load_dotenv
from string import Template

load_dotenv()
server = os.environ["DESTINATION_SERVER"].strip()
port = int(os.environ["DESTINATION_PORT"])
user = os.environ["DESTINATION_USER"]
host_path = os.environ["DESTINATION_HOST_PATH"]


def sendSCP(path):
    # load environment variables

    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(server, port, user)
    client = SCPClient(ssh.get_transport())
    client.put(path, host_path, recursive=True)
    ssh.close()
    print("file(s) sent successfully")


def sendFolder(path, askPrompt=True):
    if (askPrompt == True):
        print(f"Do you want to upload folder '{path}' (y/n)?")
        __answer = input()
    else:
        __answer = "y"
    if (__answer == "y"):
        sendSCP(path)
    else:
        print("stopping program")
        quit()


def sendFile(path):
    sendSCP(path)
