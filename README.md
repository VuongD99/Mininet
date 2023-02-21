# Mininet Enterprise Network

Emulator implementation of a enterprise network comprises of a campus, home, and computing cluster network with multiple DHCP servers, user devices, switches, and a remote controller.

![NetworkTopo](https://user-images.githubusercontent.com/19192100/220479670-2c5624eb-b3f8-41ee-a919-38b34689fa78.PNG)

## Overview of code:

- final_dhcp.py - Mininet Tolopogy #1. DHCP servers assign random IP address to each of the hosts.

- final_skel.py - Mininet Topology #2 with the following criteria.

  **Campus Network:**

      ○ In the Campus network, there are 4 hosts, h1, h2, h3, h4.

      ○ IP address constraints: any IPv4 address, with network address 10.1.1.0, and subnet mask /24

      ○ h1, h2, h3, h4 connect to switch1

  **Home Network:**

      ○ The Home Network has two connected devices, d1 and d2.

      ○ IP address constraints: any IPv4 address, with network address 10.2.2.0, and subnet mask /24

      ○ d1, d2 connect to switch3

  **Computing Cluster:**

      ○ The computing cluster has two servers - CCServer1, CCServer2. The Computing Cluster subnet has the network address 10.3.3.0 /29. 

      ○ Note: IPv4 addresses are pre-assigned, no DHCP servers needed.

      ○ CCServer1 connects to Switch4

      ○ CCServer2 connects to Switch5

  **Link Parameters:**

      ○ The link between Switch 4 and CCServer 1 has bandwidth 10Mbps.

      ○ All other links in the topology have bandwidth 3Mbps.


- finalcontroller_task2only_skel.py - Contains code for routing functions of the network controller.

      ○ Clients in the campus network communicate with the devices in the Home Network through the shortest path.
      
      ○ Clients in the campus network communicate with one of the servers in the Computing Cluster Network through the shortest best performance links.
      
- finalcontroller_task3and2_skel.py - Implements a firewall to completely isolate Device 1 from the network as well as block all IP traffic from Device 2.

Project for Networking class at University of California, Santa Cruz. Written in Python.
