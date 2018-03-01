import time
from datetime import datetime as dt

import platform

hosts_path="/etc/hosts"

redirect="127.0.0.1"

website_lists=["www.yahoo.com", "yahoo"]

print(platform.system())

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 1) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23, 59):
        print("working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect + "\t" + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
            file.truncate()
        print("non working hour")
    time.sleep(2)
