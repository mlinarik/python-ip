import socket
import requests

def get_isp():
    # Get the hostname
    hostname = socket.gethostname()
    # Get the IP address
    ip_address = socket.gethostbyname(hostname)
    # Use the IP address to get ISP info
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = response.json()
    # Return the ISP
    return data['org']

print(get_isp())
