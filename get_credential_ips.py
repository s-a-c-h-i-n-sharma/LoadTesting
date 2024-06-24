

def get_ips():
    with open("ips.txt", 'r') as file:
        return [line.strip() for line in file.readlines()]


def get_username_and_password():
    with open("credentials.txt", 'r') as file:
        credentials_file = file.readlines()
        if len(credentials_file) < 2:
            raise ValueError(
                "The credentials file must contain at least two lines: one for username and one for the password.")
        credentials = {
            'username': credentials_file[0].strip(),
            'ppk': credentials_file[1].strip(),
            'pem': credentials_file[2].strip()
        }
        return credentials