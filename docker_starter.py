import os # Inbyggt i Python

# Starta en Docker-container
def start_docker_container():
    os.system('docker run hello-world') # Kör en enkel container
    print("Docker container started.") # Skriv ut meddelande

# Kör funktionen
if __name__ == "__main__":
    start_docker_container()