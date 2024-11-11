import fade
import os
import requests
from colorama import Fore, Style

os.system("cls")

print(fade.fire(fr"""                                                                                                         
        $$$$$$\  $$\                         $$\                 $$\   $$\           $$\                           
        $$  __$$\ \__|                        $$ |                $$$\  $$ |          $$ |                          
        $$ /  \__|$$\ $$$$$$\$$$$\   $$$$$$\  $$ | $$$$$$\        $$$$\ $$ |$$\   $$\ $$ |  $$\  $$$$$$\   $$$$$$\  
        \$$$$$$\  $$ |$$  _$$  _$$\ $$  __$$\ $$ |$$  __$$\       $$ $$\$$ |$$ |  $$ |$$ | $$  |$$  __$$\ $$  __$$\ 
        \____$$\ $$ |$$ / $$ / $$ |$$ /  $$ |$$ |$$$$$$$$ |      $$ \$$$$ |$$ |  $$ |$$$$$$  / $$$$$$$$ |$$ |  \__|
        $$\   $$ |$$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$   ____|      $$ |\$$$ |$$ |  $$ |$$  _$$<  $$   ____|$$ |      
        \$$$$$$  |$$ |$$ | $$ | $$ |$$$$$$$  |$$ |\$$$$$$$\       $$ | \$$ |\$$$$$$  |$$ | \$$\ \$$$$$$$\ $$ |      
        \______/ \__|\__| \__| \__|$$  ____/ \__| \_______|      \__|  \__| \______/ \__|  \__| \_______|\__| v1.0      
                                    $$ |                                                                
                                    $$ |                                                                            
                                    \__|
        by: Phantom Services
      """))

while True:
    WEBHOOK_URL = input(f"{Fore.LIGHTRED_EX}[+]{Style.RESET_ALL} Enter your Discord webhook: ")
    
    if not WEBHOOK_URL.startswith("https://discord.com/api/webhooks/"):
        print(f"{Fore.LIGHTRED_EX}[-]{Style.RESET_ALL} This doesn't look like a Discord webhook's url. Please try again.")
        continue
        
    test_webhook = input(f"{Fore.LIGHTRED_EX}[+]{Style.RESET_ALL} Would you like to test your webhook? [y/n] ")
    
    if test_webhook.lower() == "y":
        response = requests.post(WEBHOOK_URL, json={"username":"Simple Nuker by Phantom","content":"Your webhook is working!"})
        if response.status_code == 204:
            print(f"{Fore.LIGHTRED_EX}[+]{Style.RESET_ALL} Your webhook is working!")
            break
        else:
            print(f"{Fore.LIGHTRED_EX}[-]{Style.RESET_ALL} Something went wrong: ({response.status_code})")
    elif test_webhook.lower() == "n":
        break
    else:
        print(f"{Fore.LIGHTRED_EX}[-]{Style.RESET_ALL} Invalid input! Please try again.")
    
while True:
    start = input(f"{Fore.LIGHTRED_EX}[+]{Style.RESET_ALL} Are you sure you want to proceed? [y/n] ")
    if start.lower() == "y":
        print("Press CTRL+C when you would like to quit...")
        while True:
            requests.post(WEBHOOK_URL, json={"username":"Simple Nuker by Phantom","content":"||@everyone|| This channel is getting nuked by Simple Nuker. This tool was created by Phantom Services."})
    elif start.lower() == "n":
        exit()
    else:
        print("Invalid input! Please try again.")