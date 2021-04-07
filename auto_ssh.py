#!/usr/bin/python3

import paramiko
import sys

results = []

def ssh_conn():

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname= '192.168.1.8', username='cedrick',key_filename='/home/cedrick/.ssh/id_rsa',port=22)
    stdin, stdout, stderr = ssh.exec_command('systemctl --type service --state running')

    for line in stdout:
        results.append(line.strip('\n'))

ssh_conn()

for i in results:
    print(i.strip())

sys.exit()


