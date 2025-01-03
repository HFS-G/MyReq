
from colorama import Fore, Style, init
import requests
import os
import getpass
import time

init()  # Инициализация colorama

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    username = getpass.getuser()
    logo = f"""
{Fore.CYAN}
___  ___     ______           
|  \/  |     | ___ \          
| .  . |_   _| |_/ /___  __ _ 
| |\/| | | | |    // _ \/ _` |
| |  | | |_| | |\ \  __/ (_| |
\_|  |_/\__, \_| \_\___|\__, |
         __/ |             | |
        |___/              |_|
{Style.RESET_ALL}
{Fore.GREEN}Current User: {username}{Style.RESET_ALL}
"""
    print(logo)

def make_request(url, request_type):
    try:
        if request_type == "1":  # GET request
            response = requests.get(url)
        elif request_type == "2":  # POST request
            response = requests.post(url)
        elif request_type == "3":  # HEAD request
            response = requests.head(url)
        elif request_type == "4":  # OPTIONS request
            response = requests.options(url)
        
        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response.text[:500] + "..." if len(response.text) > 500 else response.text
        }
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    while True:
        clear_screen()
        print_logo()
        
        # Получаем URL
        url = input(f"{Fore.YELLOW}Enter URL (e.g., http://example.com): {Style.RESET_ALL}")
        
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        while True:
            clear_screen()
            print_logo()
            print(f"{Fore.CYAN}Current URL:{Style.RESET_ALL} {url}")
            print(f"\n{Fore.GREEN}Choose request type:{Style.RESET_ALL}")
            print("1. GET Request")
            print("2. POST Request")
            print("3. HEAD Request")
            print("4. OPTIONS Request")
            print("5. Change URL")
            print("6. Exit")
            
            choice = input(f"\n{Fore.YELLOW}Enter your choice (1-6): {Style.RESET_ALL}")
            
            if choice == "6":
                clear_screen()
                print(f"{Fore.GREEN}Thank you for using Web Tools! Goodbye!{Style.RESET_ALL}")
                return
                
            if choice == "5":
                break
                
            if choice in ["1", "2", "3", "4"]:
                print(f"\n{Fore.CYAN}Sending request...{Style.RESET_ALL}")
                result = make_request(url, choice)
                
                if isinstance(result, dict):
                    print(f"\n{Fore.GREEN}Status Code:{Style.RESET_ALL} {result['status_code']}")
                    print(f"\n{Fore.GREEN}Headers:{Style.RESET_ALL}")
                    for key, value in result['headers'].items():
                        print(f"{key}: {value}")
                    print(f"\n{Fore.GREEN}Content Preview:{Style.RESET_ALL}")
                    print(result['content'])
                else:
                    print(f"\n{Fore.RED}{result}{Style.RESET_ALL}")
                
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
                os.system("clear")
            else:
                print(f"\n{Fore.RED}Invalid choice! Please try again.{Style.RESET_ALL}")
                time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{Fore.GREEN}Program terminated by user. Goodbye!{Style.RESET_ALL}")
      
