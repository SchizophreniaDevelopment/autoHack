from os import system

try:
    system("cls")
except:
    system("clear")

def menu():
    try:
        system("color 0a")
    except:
        print("Hacker Mode")

    print("{:35} 1\n{:35} 2\n{:35} 3".format("Net Scan", "Port Scan", "Exit"))

while True:
    menu()
    i = input("What utility would you like to use?(1-3) ")
    if i == "1":
        system("lanscan_arp.py")
    elif i == "2":
        system("netScan.py")
    elif i == "3":
        break
    else:
        print("Invalid input")

system("color")
