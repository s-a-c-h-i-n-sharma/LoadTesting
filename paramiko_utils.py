import paramiko

remote_path = r"/home/ubuntu/loadtesting/jmeter/apache-jmeter-5.6.2/bin/"

def get_ssh_client(ip, username, pem_key_path):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    private_key = paramiko.RSAKey.from_private_key_file(pem_key_path)
    ssh_client.connect(hostname=ip, username=username, pkey=private_key)
    return ssh_client


def execute_command(ssh_client, command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    stdout.channel.recv_exit_status()  # Wait for the command to complete
    output = stdout.read().decode('utf-8')
    errors = stderr.read().decode('utf-8')
    return output, errors

def delete_file(ssh_client, filename):
    file_path = remote_path + filename
    sftp_client = ssh_client.open_sftp()
    ip = ssh_client.get_transport().getpeername()[0]
    print(f"Checking if file '{filename}' already exists or not on {ip}...")
    try:
        sftp_client.stat(file_path)
        print(f"File '{filename}' already exists on {ip} , Deleting...")
        sftp_client.remove(file_path)  # Remove existing file
    except FileNotFoundError:
        pass
    return sftp_client

def transfer_file(ssh_client, local_path, filename):
    ip = ssh_client.get_transport().getpeername()[0]
    sftp_client = delete_file(ssh_client=ssh_client, filename=filename)
    print(f"Transferring {local_path} as {remote_path+filename} to {ip}")
    sftp_client.put(local_path, remote_path+filename)
    print(f"Successfully transferred to {ip}")


