
             ##### READING THE deviceID FROM authfile.txt #####

import subprocess
import tkinter as tk
from tkinter import simpledialog

def authentication():
    ## getting deviceID of connected USB ##
    cmd = 'wmic path Win32_PnPEntity where "ClassGuid=\'{36fc9e60-c465-11cf-8056-444553540000}\'" get DeviceId,Name'
    output = subprocess.check_output(cmd, shell=True)
    serial_number=""
    output_str = output.decode('utf-8')
    output_lines = output_str.split('\r\r\n')

    for line in output_lines:
        if 'USB Mass Storage Device' in line:
            serial_number = line.split()[0]
            break

    # Read the deviceID from a file ###
    with open('authfile.txt', 'r') as f:
        auth_devices = f.readlines()
        for line in auth_devices:
                auth_devices = line.strip()

                if serial_number in auth_devices:
                    ## if deviceID present in authfile.txt, then it is considered authenticated ###
                    tk.messagebox.showinfo("Authentication status", "Device Authenticated")
                    break
                else:
                    from pythonpopup import popup
                    break
    root = tk.Tk()
    root.withdraw()
