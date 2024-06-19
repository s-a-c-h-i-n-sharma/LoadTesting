import paramiko
import os

def transfer_file(local_path, remote_path, ip_address, username, private_key):
    sftp_client = None
    ssh_client = None
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        private_key = paramiko.RSAKey.from_private_key_file(private_key)
        ssh_client.connect(hostname=ip_address, username=username, pkey=private_key)

        sftp_client = ssh_client.open_sftp()

        try:
            sftp_client.stat(remote_path)
            print(f"File '{remote_path}' already exists on {ip_address}, replacing...")
            sftp_client.remove(remote_path)  # Remove existing file
        except FileNotFoundError:
            pass

        sftp_client.put(local_path, remote_path)

        print(f"Successfully transferred {local_path} to {remote_path}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    local_path = r"D:\Magicbox-loadtesting\JMX_files\BJU_consolidated_scenarios.jmx"
    remote_path = "/loadtesting/jmeter/apache-jmeter/bin/BJU_consolidated_scenarios.jmx"
    ip_address = "10.30.0.201"
    username = "ubuntu"
    private_key = r"D:\Magicbox-loadtesting\magicbox-qc-prod.ppk"

    transfer_file(local_path, remote_path, ip_address, username, private_key)

if __name__ == "__main__":
    main()