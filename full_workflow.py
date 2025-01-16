import time

SLEEP_TIME = 4

def backup_files():
    print("Backing up files...")
    time.sleep(SLEEP_TIME)
    print("Backup done!")

def fetch_data():
    print("Fetching data...")
    time.sleep(SLEEP_TIME)
    print("Data fetched!")
    return "data"

def process_data():
    print("Processing data...")
    time.sleep(SLEEP_TIME)
    print("Data processed!")

def generate_report():
    print("Generating report...")
    time.sleep(SLEEP_TIME)
    print("Report Generated!")

def send_email():
    print("Sending email...")
    time.sleep(SLEEP_TIME)
    print("Sent!")    

def full_workflow():
    backup_files()
    data = fetch_data()
    process_data()
    generate_report()
    send_email()

if __name__== "__main__":
    full_workflow()