import paramiko


def execute_command(ssh_client, command):
    try:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        stdout.channel.recv_exit_status()  # Wait for the command to complete
        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')
        return output, errors
    except Exception as e:
        return str(e), ""


def main():
    # Initialize SSH client
    ssh_client = paramiko.SSHClient()

    # Set policy to automatically add host keys of new servers
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Path to your private key file
    private_key_path = r"C:\path\to\privatekey"  # Use raw string for Windows path
    # private_key_path = "/home/user/.ssh/id_rsa"  # For Linux/Mac

    # Load the private key
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

    # Connect to the remote host
    try:
        ssh_client.connect(hostname='10.30.0.201', username='ubuntu', pkey=private_key)

        # Example command to change directory and run jmeter-server
        commands = [
            "cd /path/to/apache-jmeter-<version>/bin",
            "./jmeter-server"
        ]

        for command in commands:
            output, errors = execute_command(ssh_client, command)
            if output:
                print(f"Output:\n{output}")
            if errors:
                print(f"Errors:\n{errors}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SSH connection
        if ssh_client:
            ssh_client.close()


if __name__ == "__main__":
    main()
