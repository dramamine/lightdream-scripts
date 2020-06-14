### Networking Setup Guide

### Ethernet
What's wired:
- Jukebox PC
- 5 Brains (teensy + ethernet)

Hardware:
NETGEAR F5108 Fast Ethernet Switch (8 Ports)

Name | MAC Address | IP 
Motherbrain | 04 E9 E5 00 69 EC | 169.254.18.32
@TODO: we're setting the MAC manually, how about checkin the hardware MAC address and using a table to get the real ip?


### Wireless
What's connecting:
- Jukebox PC, unless I can get it to use the wired connection
- "Remote controllers"

Hardware:
Netis WF2411
Set it up at http://192.168.1.1
Assigns IPs based on MAC addresses. Visit Network->LAN->DHCP Client List. Table should look like this:

Name | MAC Address | IP
First remote | ec:fa:bc:62:1d:63 | 192.168.1.3
Marten-PC | a0:f3:c1:19:fc:18 | 192.168.1.4
