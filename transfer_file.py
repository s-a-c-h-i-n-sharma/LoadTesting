import paramiko
import os
from get_credential_ips import get_ips, get_username_and_password
from paramiko_utils import get_ssh_client, transfer_file
from csv_utils import ensure_n_csv_files

def transfer_jmx(local_path, remote_filename, ips, username, private_key):
    for ip in ips:
        ssh_client = get_ssh_client(ip=ip, username=username, pem_key_path=private_key)
        transfer_file(ssh_client=ssh_client, local_path=local_path, filename=remote_filename)

def transfer_csvs(csv_dir, remote_filename, ips, username, private_key):
    csv_file_paths = ensure_n_csv_files(csv_dir, len(ips))

    for csv_path, ip in zip(csv_file_paths, ips):
        ssh_client = get_ssh_client(ip=ip, username=username, pem_key_path=private_key)
        transfer_file(ssh_client=ssh_client, local_path=csv_path, filename=remote_filename)

def main(file_type):
    local_jmx_path = r"D:\Magicbox-loadtesting\JMX_files\graph-questions-assessment.jmx"
    remote_jmx_filename = "graph-questions-assessment.jmx"
    local_csv_path = r"D:\Magicbox-loadtesting\CSVs\new_csvs"
    remote_csv_filename = "updated_list_teacher1000.csv"

    print("Please check the configurations before transferring:\n")
    print(f"Local jmx path : {local_jmx_path}")
    print(f"Local CSV dir : {local_csv_path}")

    print(f"Remote jmx name :{remote_jmx_filename}")
    print(f"Remote jmx name :{remote_csv_filename}")
    print(f"Enter Y/y to continue ....")
    conf = input()
    if conf == "Y" or conf == "y":
        ips = get_ips()
        credentials = get_username_and_password()
        if file_type == "JMX":
            transfer_jmx(local_jmx_path, remote_jmx_filename, ips, credentials['username'], credentials['pem'])

        if file_type == "CSV":
            transfer_csvs(local_csv_path, remote_csv_filename, ips, credentials['username'], credentials['pem'])

        if file_type == "Both":
            transfer_jmx(local_jmx_path, remote_jmx_filename, ips, credentials['username'], credentials['pem'])
            transfer_csvs(local_csv_path, remote_csv_filename, ips, credentials['username'], credentials['pem'])



# if __name__ == "__main__":
#     main()