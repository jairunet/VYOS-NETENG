import paramiko
hostname = 'x.x.x.x'
myuser = 'user'
mySSHK = '/home/user/.ssh/id_rsa.pub'
sshcon = paramiko.SSHClient()

sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshcon.connect(hostname, username=myuser, key_filename=mySSHK)
# stdin, stdout, stderr = sshcon.exec_command('ls')
# print stdout.readlines()
# sshcon.close()
