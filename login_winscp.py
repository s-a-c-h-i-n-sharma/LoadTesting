import subprocess
import time


def get_ips(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


def get_username_and_keyfile(filename):
    with open(filename, 'r') as file:
        credentials = file.readlines()
        if len(credentials) < 2:
            raise ValueError(
                "The credentials file must contain at least two lines: one for username and one for the path to the private key file.")
        return credentials[0].strip(), credentials[1].strip()


def open_winscp(ip, username, keyfile):
    try:
        # Construct the command for WinSCP
        command = [
            'C:\\Program Files (x86)\\WinSCP\\WinSCP.exe',  # Full path to WinSCP.exe
            f'sftp://{username}@{ip}/',
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
    ip_file = 'ips.txt'  # File containing IP addresses, one per line
    credentials_file = 'credentials.txt'  # File containing username on the first line and private key file path on the second line

    # Get the list of IPs and credentials
    ips = get_ips(ip_file)
    username, keyfile = get_username_and_keyfile(credentials_file)

    # Iterate over each IP and open WinSCP
    for ip in ips:
        open_winscp(ip, username, keyfile)
        time.sleep(1)  # Small delay to avoid issues with opening too many sessions at once


if __name__ == "__main__":
    main()
