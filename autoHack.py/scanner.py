from scapy.all import ARP, Ether, srp

target = input("Target ip?")
if target == "":
    target_ip = "192.168.0.1/24"
else:
    target_ip = target

# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []
test = []

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc, 'op': received.op, 'hwtype': received.hwtype})
    test.append(received)

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC" + " "*20+"OP" + " "*4+"HWTYPE")
for client in clients:
    print("{:16}    {:16}  {:5} {:5}".format(client['ip'], client['mac'], client['op'], client['hwtype']))
print("")
