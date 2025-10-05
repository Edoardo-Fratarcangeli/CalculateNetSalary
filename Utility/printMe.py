import platform
from Settings.settings import User, App
from colorama import init, Style, Fore
    
 # solo queste verranno importate con *
__all__ = ['intro'] 

def intro():
    match platform.system():
        case "Linux":
            introLinux() 
        case "Darwin":
            introOs() 
        case "Windows", _:
            introWindows()  # default

def introLinux():
    init(autoreset=True)
    print(Style.BRIGHT + Fore.BLUE + f"{App.name}")
    print(f"- by {User.name} {User.surname} -\n")

def introOs():
    introLinux()

def introWindows():
    init(autoreset=True)
    print(Style.BRIGHT + Fore.BLUE + f"{App.name}")
    print(f"- by {User.name} {User.surname} -\n")
