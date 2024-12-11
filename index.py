import requests
import whois
import json

def lookup_ip(ip):
    print("\n[IP Information]")
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            for key, value in data.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Error: Unable to fetch IP information.")
    except Exception as e:
        print(f"Error: {e}")

def lookup_domain(domain):
    print("\n[Domain WHOIS Information]")
    try:
        domain_info = whois.whois(domain)
        print(domain_info)
    except Exception as e:
        print(f"Error: {e}")

def lookup_email(email):
    print("\n[Email Breach Check]")
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        headers = {
            'User-Agent': 'PythonOSINTTool',
            'hibp-api-key': '4539992'  # Replace with your HaveIBeenPwned API key
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            breaches = response.json()
            print(f"{email} has been found in the following breaches:")
            for breach in breaches:
                print(f"- {breach['Name']}: {breach['Description']}")
        elif response.status_code == 404:
            print(f"No breaches found for {email}.")
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("OSINT Tool")
    print("1. Lookup IP Address")
    print("2. Lookup Domain")
    print("3. Lookup Email")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        ip = input("Enter IP Address: ")
        lookup_ip(ip)
    elif choice == "2":
        domain = input("Enter Domain: ")
        lookup_domain(domain)
    elif choice == "3":
        email = input("Enter Email: ")
        lookup_email(email)
    else:
        print("Invalid option.")
