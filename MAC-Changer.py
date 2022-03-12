#!/usr/bin/env python3

title = '''
  __  __          _____       _____ _    _          _   _  _____ ______ _____  
 |  \/  |   /\   / ____|     / ____| |  | |   /\   | \ | |/ ____|  ____|  __ \ 
 | \  / |  /  \ | |   ______| |    | |__| |  /  \  |  \| | |  __| |__  | |__) |
 | |\/| | / /\ \| |  |______| |    |  __  | / /\ \ | . ` | | |_ |  __| |  _  / 
 | |  | |/ ____ \ |____     | |____| |  | |/ ____ \| |\  | |__| | |____| | \ \ 
 |_|  |_/_/    \_\_____|     \_____|_|  |_/_/    \_\_| \_|\_____|______|_|  \_\

[+] WARNING: Execute this at your own risk.                                                                               
'''

import subprocess

def SelectInterface(choice):
    interfaces = {1:'eth0',2:'wlan0'}
    new_mac = input("Enter desired MAC addreess (Default: 00:11:22:33:44:55): ") or '00:11:22:33:44:55'
    print("[+] Changing MAC Address to "+new_mac+" .....")
    subprocess.call("ifconfig >> config.txt",shell=True)
    subprocess.call("ifconfig "+interfaces.get(choice)+" down",shell=True)
    subprocess.call("ifconfig "+interfaces.get(choice)+" hw ether "+new_mac,shell=True)
    subprocess.call("ifconfig "+interfaces.get(choice)+" up",shell=True)


subprocess.call("netstat -i", shell=True)
print("\n\n1. eth0\n2. wlan0\n")    
choice = int(input("Enter the choice: "))
SelectInterface(choice)

