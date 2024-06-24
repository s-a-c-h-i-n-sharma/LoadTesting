import time
import keyboard
from pywinauto.application import Application

def send_command_to_putty(window_title, command):
    try:
        # Connect to the PuTTY window
        app = Application().connect(title_re=window_title)
        dlg = app.window(title_re=window_title)

        # Activate the window and send Ctrl+C
        dlg.set_focus()
        dlg.type_keys('^c')
        time.sleep(1)

        # Send the command to start JMeter server
        keyboard.write(command)
        keyboard.send('enter')
        print(f"Command sent to {window_title}")

    except Exception as e:
        print(f"An error occurred: {e}")