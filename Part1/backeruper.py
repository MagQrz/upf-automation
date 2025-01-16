import shutil
from datetime import datetime

# Byt ut mot mappar på din dator
source = "/Users/magnuskurtz/2024/Programmering/Prog1Code/upf-automation/source"
destination = "/Users/magnuskurtz/2024/Programmering/Prog1Code/upf-automation/backups/backup"
# Skapa en säkerhetskopia av filer
def backup_files():
    # Lägg till datumen i mappnamnet
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    target = f"{destination}_{timestamp}"
    shutil.copytree(source, target, dirs_exist_ok=True)
    print('Backup completed.')
# Kör funktionen
if __name__== "__main__":
    backup_files()