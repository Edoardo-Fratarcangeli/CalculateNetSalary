from Settings.settings import User
from colorama import init, Style, Fore
    
 # solo queste verranno importate con *
__all__ = ['intro'] 

def intro():
    init(autoreset=True)
    print(Style.BRIGHT + Fore.BLUE +  "Calculate Net Salary App")
    print(f"- by {User.name} {User.surname} -\n")
