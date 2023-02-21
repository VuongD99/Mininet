#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
from mininet.link import TCLink

class final_topo(Topo):
  def build(self):
    # Examples!
    # Create a host with a default route of the ethernet interface. You'll need to set the
    # default gateway like this for every host you make on this assignment to make sure all 
    # packets are sent out that port. Make sure to change the h# in the defaultRoute area
    # and the MAC address when you add more hosts!
     h1 = self.addHost('h1',mac='00:00:00:00:00:01',ip='10.1.1.13/24', defaultRoute="h1-eth0")
     h2 = self.addHost('h2',mac='00:00:00:00:00:02',ip='10.1.1.14/24', defaultRoute="h2-eth0")
     h3 = self.addHost('h3',mac='00:00:00:00:00:03',ip='10.1.1.15/24', defaultRoute="h3-eth0")
     h4 = self.addHost('h4',mac='00:00:00:00:00:04',ip='10.1.1.16/24', defaultRoute="h4-eth0")
     d1 = self.addHost('d1',mac='00:00:00:00:00:05',ip='10.2.2.15/24', defaultRoute="d1-eth0")
     d2 = self.addHost('d2',mac='00:00:00:00:00:06',ip='10.2.2.16/24', defaultRoute="d2-eth0")
     CCServer1 = self.addHost('CCServer1',mac='00:00:00:00:00:07',ip='10.3.3.1/29', defaultRoute="CCServer1-eth0")
     CCServer2 = self.addHost('CCServer2',mac='00:00:00:00:00:08',ip='10.3.3.2/29', defaultRoute="CCServer2-eth0")
    
    # Create a switch. No changes here from Lab 1.
     s1 = self.addSwitch('s1')
     s2 = self.addSwitch('s2')
     s3 = self.addSwitch('s3')
     s4 = self.addSwitch('s4')
     s5 = self.addSwitch('s5')


    # Connect Port 8 on the Switch to Port 0 on Host 1 and Port 9 on the Switch to Port 0 on 
    # Host 2. This is representing the physical port on the switch or host that you are 
    # connecting to.
    #
    # IMPORTANT NOTES: 
    # - On a single device, you can only use each port once! So, on s1, only 1 device can be
    #   plugged in to port 1, only one device can be plugged in to port 2, etc.
    # - On the "host" side of connections, you must make sure to always match the port you 
    #   set as the default route when you created the device above. Usually, this means you 
    #   should plug in to port 0 (since you set the default route to h#-eth0).
    #
    
    #connect all 4 hosts to switch1 
     self.addLink(s1,h1, port1=1, port2=0, bw=3)
     self.addLink(s1,h2, port1=2, port2=0, bw=3)
     self.addLink(s1,h3, port1=3, port2=0, bw=3)
     self.addLink(s1,h4, port1=4, port2=0, bw=3) 

    #connect all 2 hosts to switch3
     self.addLink(s3,d1, port1=1, port2=0, bw=3)
     self.addLink(s3,d2, port1=2, port2=0, bw=3)

    #Connections for the CCServers
     self.addLink(s4,CCServer1, port1=3, port2=0, bw=10)
     self.addLink(s5,CCServer2, port1=4, port2=0, bw=3)

     #switch to switch connections
     self.addLink(s1,s2, port1=5, port2=1, bw=3)
     self.addLink(s1,s5, port1=6, port2=2, bw=3)
     self.addLink(s1,s3, port1=7, port2=3, bw=3)
     self.addLink(s2,s4, port1=2, port2=1, bw=3)
     self.addLink(s4,s5, port1=2, port2=1, bw=3)
     self.addLink(s3,s5, port1=4, port2=3, bw=3)

def configure():
  topo = final_topo()
  net = Mininet(topo=topo, link=TCLink, controller=RemoteController)
  net.start()

  CLI(net)
  
  net.stop()


if __name__ == '__main__':
  configure()
