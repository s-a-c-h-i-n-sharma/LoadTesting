import paramiko
import time

def execute_command(ssh_client, command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    stdout.channel.recv_exit_status()  # Wait for the command to complete
    output = stdout.read().decode('utf-8')
    errors = stderr.read().decode('utf-8')
    return output, errors

def transfer_file(ssh_client, local_path, remote_path):
    sftp_client = ssh_client.open_sftp()
    sftp_client.put(local_path, remote_path)
    sftp_client.close()

def start_jmeter_server(ip, username, private_key_path):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh_client.connect(hostname=ip, username=username, pkey=private_key)

        command = "cd /path/to/apache-jmeter-<version>/bin && ./jmeter-server"
        output, errors = execute_command(ssh_client, command)
        if output:
            print(f"Output from {ip}:\n{output}")
        if errors:
            print(f"Errors from {ip}:\n{errors}")

        ssh_client.close()
    except Exception as e:
        print(f"Error on {ip}: {e}")

def run_jmeter_master(ip, username, private_key_path, jmx_file, remote_ips):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh_client.connect(hostname=ip, username=username, pkey=private_key)

        remote_ips_str = ','.join(remote_ips)
        command = f"cd /path/to/apache-jmeter-<version>/bin && ./jmeter -n -t {jmx_file} -R {remote_ips_str}"
        output, errors = execute_command(ssh_client, command)
        if output:
            print(f"Output from master {ip}:\n{output}")
        if errors:
            print(f"Errors from master {ip}:\n{errors}")

        ssh_client.close()
    except Exception as e:
        print(f"Error on master {ip}: {e}")

def main():
    # Configuration
    master_ip = "192.168.1.100"  # Master machine IP
    remote_ips = ["192.168.1.101", "192.168.1.102"]  # Remote machines IPs
    username = "username"  # SSH username
    private_key_path = r"C:\path\to\privatekey"  # Path to private key file (PEM format)
    local_jmx_path = r"C:\path\to\test.jmx"  # Local path to .jmx file
    remote_jmx_path = "/path/to/apache-jmeter-<version>/bin/test.jmx"  # Remote path to .jmx file

    # Start JMeter servers on remote machines
    for ip in remote_ips:
        start_jmeter_server(ip, username, private_key_path)

    # Wait a bit to ensure servers are up
    time.sleep(10)

    # Transfer .jmx file to master machine
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
        ssh_client.connect(hostname=master_ip, username=username, pkey=private_key)
        transfer_file(ssh_client, local_jmx_path, remote_jmx_path)
        ssh_client.close()
    except Exception as e:
        print(f"Error transferring .jmx file to master: {e}")

    # Run JMeter test on master machine
    run_jmeter_master(master_ip, username, private_key_path, remote_jmx_path, remote_ips)

if __name__ == "__main__":
    main()