import pyshark
import socket

data = pyshark.FileCapture('capture/fresh-install-update.pcapng')
data.encryption
http = 0
dns = 0
tcp = 0
dhcp = 0
ip = []
count_ip = []
x = 0
for i in data: 
    if hasattr(i, 'http'):
        http = http + 1
    if hasattr(i, 'dns'):
        dns = dns + 1
    if hasattr(i, 'tcp'):
        tcp = tcp + 1
    if hasattr(i, 'dhcp'):
        dhcp = dhcp + 1
    test = i.ip.src
    if test in ip:
        count_ip[ip.index(test)] = count_ip[ip.index(test)] + 1
    else: 
        ip.append(test)
        count_ip.append(1)
    x = x + 1
print(http, " http ", dns, " dns ", tcp, " tcp ", dhcp, " dhcp ")
i = 0
for x in ip:
    print(x, count_ip[i])
    i = i + 1
for x in ip:
    try:
        print(socket.gethostbyaddr(x))
    except:
        print(x, " has no host")
