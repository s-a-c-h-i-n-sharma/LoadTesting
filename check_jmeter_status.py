import paramiko
import time
from get_credential_ips import get_ips, get_username_and_password

def check_jmeter_status(ip, username, password):
    try:
        # Connect to the SSH server
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password)

        # Execute command to check JMeter server process
        stdin, stdout, stderr = client.exec_command('pgrep -f jmeter-server')

        # Check if any output is returned (process is running)
        output = stdout.read().decode().strip()
        if output:
            print(f"JMeter server is running on {ip}")
        else:
            print(f"JMeter server is not running on {ip}")

        # Close SSH connection
        client.close()

    except Exception as e:
        print(f"Error occurred while checking JMeter status on {ip}: {e}")

def main():

    ips = get_ips()
    credentials = get_username_and_password()

    for ip in ips:
        check_jmeter_status(ip, credentials['username'], credentials['pem'])
        time.sleep(1)  # Adjust delay between SSH connections if needed

# if __name__ == "__main__":
#     main()