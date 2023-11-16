
import nmap

# create a new nmap scanner object
scanner = nmap.PortScanner()

# scan the local network for open ports
scanner.scan(hosts='192.168.1.0/24', arguments='-p 1-65535')

# print out the results
for host in scanner.all_hosts():
    print('Host : %s (%s)' % (host, scanner[host].hostname()))
    print('State : %s' % scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('Protocol : %s' % proto)
        lport = scanner[host][proto].keys()
        for port in lport:
            print('port : %s\tstate : %s' % (port, scanner[host][proto][port]['state']))
