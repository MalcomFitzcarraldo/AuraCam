# AuraCam SETTINGS

# Example of network path \\server\PCcam\capture.jpg - NO SPACES!, Must be capture.jpg
save_location = r'\\server\AuraCam1\capture.jpg'

# Quality (1-100)
output_quality = 40

# Refresh Rate (seconds)
refresh_rate = 3

# END OF SETTINGS
# END OF SETTINGS
# END OF SETTINGS



import socket
import time
import pyautogui
import random
import os
import keyboard
import datetime
from PIL import Image
from colorama import Fore, Back, Style, init
# pillow
start_time = datetime.datetime.now()
init(autoreset=True)
colors = [ Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Back.BLACK, Back.GREEN, Back.MAGENTA, Back.CYAN
]

count = 0
broadcast_active = False
menu_active = True

cwd = os.getcwd()
cam_path = os.path.abspath(__file__)

ip_address = socket.gethostbyname(socket.gethostname())
hostname = socket.gethostname()

def stop_cast():
    global broadcast_active
    global menu_active
    broadcast_active = False
    menu_active = True   
    print(Fore.RED + "Broadcasting Stopped Manually")
    lambda: os.system(cam_path)
    # !add offline img!
    time.sleep(7)

def get_random_color():
    return random.choice(colors)
os.system('cls')
print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "AuraCam" + Style.RESET_ALL)
print(Fore.GREEN + "")
print(Fore.GREEN + Style.BRIGHT + "Starting...")
print(Fore.GREEN + "")
print("Current Time:", start_time.strftime("%H:%M:%S"))

def start_cast():
    global broadcast_active
    global menu_active
    menu_active = False
    broadcast_active = True
    print(Fore.GREEN + "Broadcasting Started")
    # !add offline img!

def handle_start():
    keyboard.add_hotkey('alt + X', start_cast)
    
while menu_active:
    os.system('cls')
    print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "AuraCam" + Style.RESET_ALL)
    print(Fore.GREEN + "")
    print(Fore.YELLOW + "Not Broadcasting")
    print(Fore.GREEN + "")
    print("IP Address:", ip_address)
    print("Hostname:", hostname)
    print("Python Path:", cwd)
    print("Local Path:", cam_path)
    print(Fore.GREEN + "")
    print(Fore.BLUE + "- - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(Fore.WHITE + "Ispy Camera Path:", save_location)
        # Check if the network folder is accessible
    if os.path.exists(save_location):
        print(Fore.GREEN + "Connected.")
    else:
        print(Fore.RED + "Not connected to network folder.")
    print(Fore.BLUE + "- - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(Fore.GREEN + "")
    print(Fore.GREEN + "")
    print(Fore.GREEN + "")
    print(Fore.GREEN + "")
    print(Fore.CYAN + "Alt + X to start broadcasting") 
    handle_start()
    time.sleep(3)

def handle_enter():
    keyboard.add_hotkey('alt + S', stop_cast)
while broadcast_active:
  screenshot = pyautogui.screenshot()
  screenshot.save(save_location, quality=output_quality)
  for i in range(1):
    random_color = get_random_color()
    update_time = datetime.datetime.now()
    count += 1
    os.system('cls')
    print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "AuraCam" + Style.RESET_ALL)
    print(Fore.GREEN + "")
    print(Fore.GREEN + "")
    print(random_color + "Running...")
    print("Last Transmit:", update_time.strftime("%H:%M:%S"),"     Frames Sent:", count)
    print(Fore.GREEN + "")
    print(Fore.GREEN + "")
    print("Start Time:", start_time.strftime("%H:%M:%S"))
    print(Fore.GREEN + "")    
    print(Fore.GREEN + "")
    print(Fore.GREEN + "")    
    print(Fore.GREEN + "")
    print(Fore.CYAN + "Alt + S to stop broadcasting")        
    handle_enter()
  time.sleep(refresh_rate) 
