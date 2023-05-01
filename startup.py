from os import system

try:
    system("pip install scapy")
    try:
        system("cls")
    except:
        try:
            system("clear")
        except:
            print("\n\n\n")
except:
    system("pip3 install scapy")