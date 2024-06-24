import subprocess
import time
from get_credential_ips import get_ips, get_username_and_password
from pywingauto_utils import send_command_to_putty
from run_jmeter_Server import get_window_titles


def open_putty(ip, username, password):
    try:
        # Construct the command for PuTTY
        command = [
            'putty.exe',
            '-ssh', f'{username}@{ip}',
            '-pw', password,
            #'-m', 'commands.txt'  # Use a commands file for sending commands
        ]
        # Open PuTTY
        subprocess.Popen(command)

        print(f"Opening PuTTY for {ip}")

    except Exception as e:
        print(f"An error occurred: {e}")


def run_command_in_putty(ips, username, password, command):
    window_titles = get_window_titles(ips)
    for window_title in window_titles:
        send_command_to_putty(window_title, command)
        time.sleep(2)

def main():
    command = r"cd loadtesting/jmeter/apache-jmeter-5.6.2/bin"
    ips = get_ips()
    credentials = get_username_and_password()


    for ip in ips:
        open_putty(ip, credentials['username'], credentials['ppk'])
        time.sleep(1)  # Small delay to avoid issues with opening too many sessions at once
    time.sleep(5)
    run_command_in_putty(ips,credentials['username'], credentials['ppk'], command)
