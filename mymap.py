import requests

hi1 = "###################################################"
hi2 = "#                                                 #"
hi3 = "#    Ip locater   :     Hacker location           #"

print(hi1)
print(hi2)
print(hi3)
print(hi2)
print(hi1)

first = "Enter the IP: "
print(first)
ip = input()

url = f"https://ipapi.co/{ip}/json/"

print("Opening the link: " + url)

r = requests.get(url)
data = r.json()

for key, value in data.items():
    print(f"{key}: {value}")
