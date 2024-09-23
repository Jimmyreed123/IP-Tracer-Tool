import requests
import json
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to display a welcome screen
def welcome_screen():
    print("="*50)
    print(f"{Fore.GREEN} Welcome to IP Tracer Tool ".center(50, "="))
    print(f"{Fore.GREEN}This tool will provide geographical information about an IP address.")
    print("="*50)

# Function to get IP information
def get_ip_info(ip):
    try:
        # API request to get geolocation information about the IP
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        # Check if the request was successful
        if data['status'] == 'fail':
            print(f"{Fore.RED}Error: {data['message']}")
        else:
            # Display all the IP information in green
            print(f"\n{Fore.GREEN}IP Information:")
            print(f"{Fore.GREEN}IP: {data['query']}")
            print(f"{Fore.GREEN}Country: {data['country']}")
            print(f"{Fore.GREEN}Region: {data['regionName']}")
            print(f"{Fore.GREEN}City: {data['city']}")
            print(f"{Fore.GREEN}ZIP: {data['zip']}")
            print(f"{Fore.GREEN}Lat/Lon: {data['lat']}, {data['lon']}")
            print(f"{Fore.GREEN}ISP: {data['isp']}")
            print(f"{Fore.GREEN}Org: {data['org']}")
            print(f"{Fore.GREEN}Timezone: {data['timezone']}")
    except requests.ConnectionError:
        print(f"{Fore.RED}Error: Unable to connect to the internet. Please check your connection.")
    except requests.Timeout:
        print(f"{Fore.RED}Error: The request timed out.")
    except requests.RequestException as e:
        print(f"{Fore.RED}Error: An error occurred. {e}")

# Main function to handle user input and execution
def main():
    welcome_screen()

    while True:
        # Prompt the user for an IP address or option to quit
        ip = input("\nPlease enter an IP address to trace (or type 'quit' to exit): ").strip()

        if ip.lower() == 'quit':
            print(f"{Fore.GREEN}Exiting the program. Goodbye!")
            break

        if ip == "":
            print(f"{Fore.RED}Error: IP address cannot be empty. Please try again.")
        else:
            get_ip_info(ip)

if __name__ == "__main__":
    main()