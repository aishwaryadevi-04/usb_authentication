
                        ##### WRITING THE deviceID to authfile.txt #####

import subprocess

def connected():
        cmd = 'wmic path Win32_PnPEntity where "ClassGuid=\'{36fc9e60-c465-11cf-8056-444553540000}\'" get DeviceId,Name'
        output = subprocess.check_output(cmd, shell=True)
        serial_number=""
        # Decode the output into a string
        output_str = output.decode('utf-8')

        # Split the string into lines
        output_lines = output_str.split('\r\r\n')
        print(output_lines)
        # Look for the line containing the USB drive's serial number
        for line in output_lines:
            if 'USB Mass Storage Device' in line:
                serial_number += line.split()[0]+'\n'


        # Write the serial number to a file
        with open('authfile.txt', 'w') as f:
            f.write(serial_number)

connected()
