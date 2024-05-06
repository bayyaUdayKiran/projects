import requests
import sys

try:
    inp = sys.argv[1]

except IndexError:
    inp = input("Enter the package name: ")
    

try:
    response = requests.get(f'https://play.google.com/store/apps/details?id={inp}')
    response.raise_for_status()
    if response.status_code == 200:
        print("Duplicate package name")
    else:
        print("Package name is unique & ready to go..")
except requests.exceptions.HTTPError as errh:
    print("Package name is unique & ready to go..")
except requests.exceptions.ConnectionError as errc:
    print("Package name is unique & ready to go..")
except requests.exceptions.Timeout as errt:
    print("Package name is unique & ready to go..")
except requests.exceptions.InvalidURL as inv_url:
    print("Package name is unique & ready to go..")
except requests.exceptions.RequestException as err:
    print("Package name is unique & ready to go..")


