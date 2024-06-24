import login_putty, login_winscp, transfer_file, run_jmeter_Server, check_jmeter_status


def putty_login():
    login_putty.main()

def winscp_login():
    login_winscp.main()

def file_transfer(file_type):
    transfer_file.main(file_type)

def run_jmeter_server():
    run_jmeter_Server.main()

def check_jmeter():
    check_jmeter_status.main()

def display_menu():
    print("\nMenu:")
    print("1. Perform Putty login")
    print("2. Perform Winscp login")
    print("3. Perform File transfer")
    print("4. Perform Run jmeter in Putty sessions ")
    print("5. Check JMeter status ")
    print("6. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            putty_login()
        elif choice == '2':
            winscp_login()
        elif choice == '3':
            print("Enter the choice for file type ")
            print("1: CSV")
            print("2: JMX")
            print("3: Both")
            ft_dict = {
                "1": "CSV",
                "2": "JMX",
                "3": "Both"
            }
            choice = input("Enter choice")
            file_transfer(ft_dict[choice])
        elif choice == '4':
            run_jmeter_server()
        elif choice == '5':
            check_jmeter()
        elif choice == '6':
            print("Exiting the setup....")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()