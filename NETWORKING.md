### Networking Setup Guide

### Ethernet
What's wired:
- Jukebox PC
- 5 Brains (teensy + ethernet)

Hardware:
NETGEAR F5108 Fast Ethernet Switch (8 Ports)

Name | IP 
Red Jukebox (desktop) | 169.254.18.31
Red Jukebox (laptop) | 169.254.231.56
Orange | 169.254.18.32
Yellow | 169.254.18.33
Green Motherbrain | 169.254.18.34
Blue | 169.254.18.35
Purple | 169.254.18.36

To change these and see serial numbers, edit `ld-braincode::updateIp()`
Resolume -> Advanced Output needs these IPs

### Wireless
What's wireless:
- Jukebox PC
- "Remote controllers"

Hardware:
Netis WF2411


Name | MAC Address | IP
First remote | ec:fa:bc:62:1d:63 | 192.168.1.3
Marten-PC | a0:f3:c1:19:fc:18 | 192.168.1.4

To change these, log into the router at http://192.168.1.1. Assigns IPs based on MAC addresses. Visit Network->LAN->DHCP Client List.

Remotes send UDP to TouchDesigner (192.168.1.4:7005)
TouchDesigner uses the peer IP to identify who's sending the message.

