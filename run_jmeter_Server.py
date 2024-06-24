from get_credential_ips import get_ips
import time
from pywingauto_utils import send_command_to_putty

def get_window_titles(ips):
    window_titles = []
    for ip in ips:
        window_titles.append(f"ubuntu@ip-{ip.replace('.','-')}")
    return window_titles

def main():
    command = r'./jmeter-server'
    window_titles = get_window_titles(get_ips())

    for window_title in window_titles:
        send_command_to_putty(window_title, command)
        time.sleep(2)  # Small delay to avoid issues
#
# if __name__ == "__main__":
#     main()