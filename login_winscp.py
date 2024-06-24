import subprocess
import time
from get_credential_ips import get_ips, get_username_and_password


def open_winscp(ip, username, keyfile):
    try:
        # Construct the command for WinSCP
        command = [
            'C:\\Program Files (x86)\\WinSCP\\WinSCP.exe',  # Full path to WinSCP.exe
            f'sftp://{username}@{ip}',
            f'/privatekey="{keyfile}"',
            '/ini=nul',  # Do not load any stored configuration
            '/log=winscp.log',  # Log session details (optional)
        ]

        # Open WinSCP
        subprocess.Popen(command)

        print(f"Opening WinSCP for {ip}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    ips = get_ips()
    credentials = get_username_and_password()

    for ip in ips:
        open_winscp(ip, credentials['username'], credentials['ppk'])
        time.sleep(1)

# if __name__ == "__main__":
#     main()
