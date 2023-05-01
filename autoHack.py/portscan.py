from socket import *
import time
from tqdm import tqdm
startTime = time.time()

openPorts = []

if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)
   
    for i in tqdm(range(50, 500), desc="Scanning..."):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            openPorts.append('Port %d: OPEN' % (i,))
        s.close()
for i in openPorts:
    print(i)

print('Time taken:', time.time() - startTime)