import subprocess
import time


def get_ips(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


def get_username_and_password(filename):
    with open(filename, 'r') as file:
        credentials = file.readlines()
        if len(credentials) < 2:
            raise ValueError(
                "The credentials file must contain at least two lines: one for username and one for the password.")
        return credentials[0].strip(), credentials[1].strip()


def open_putty(ip, username, password):
    try:
        # Construct the command for PuTTY
        command = [
            'putty.exe',
            '-ssh', f'{username}@{ip}',
            '-pw', password,
            '-m', 'commands.txt'  # Use a commands file for sending commands
        ]

        # Open PuTTY
        subprocess.Popen(command)

        print(f"Opening PuTTY for {ip}")

    except Exception as e:
        print(f"An error occurred: {e}")


def run_command_in_putty(ip, username, password, command):
    try:
        # Construct the command for PuTTY to change directory to Apache JMeter bin folder
        command = f'cd /loadtesting/jmeter/apache-jmeter/bin && {command}\n'  # Replace with actual path

        # Write command to a temporary file
        with open('commands.txt', 'w') as file:
            file.write(command)

        # Open PuTTY with the command
        open_putty(ip, username, password)

        print(f"Running command in PuTTY session for {ip}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    ip_file = 'ips.txt'  # File containing IP addresses, one per line
    credentials_file = 'credentials.txt'  # File containing username on the first line and password on the second line
    command = 'ls -l'  # Command to run in each PuTTY session

    # Get the list of IPs and credentials
    ips = get_ips(ip_file)
    username, password = get_username_and_password(credentials_file)

    # Run the command in each PuTTY session
    for ip in ips:
        run_command_in_putty(ip, username, password, command)
        time.sleep(1)  # Small delay to avoid issues with opening too many sessions at once


if __name__ == "__main__":
    main()
