import os # Inbyggt i Python

# Skanna öppna portar på en värd
def scan_ports(host):
    for port in range(50, 1000): # Skanna portar 50-999
        # Använd nc-kommandot för att skanna porten (Linux)
        result = os.system(f"nc -zv {host} {port} 2>/dev/null")
        if result == 0: # Om porten är öppen
            print(f"Port {port} är öppen.")
        elif port % 100 == 0: # Skriv ut varje 100:e port
            print(f"Port {port} är stängd.", end="\r")

scan_ports("localhost") # Skanna localhost