#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
from mininet.link import TCLink

class example_topo(Topo):
  def build(self):
    switch1 = self.addSwitch('switch1')
    switch2 = self.addSwitch('switch2')
    switch3 = self.addSwitch('switch3')
    switch4 = self.addSwitch('switch4')
    switch5 = self.addSwitch('switch5')

    h1 = self.addHost('h1', ip='no ip defined/24')
    h2 = self.addHost('h2', ip='no ip defined/24')
    h3 = self.addHost('h3', ip='no ip defined/24')
    h4 = self.addHost('h4', ip='no ip defined/24')
    
    d1 = self.addHost('d1', ip='no ip defined/24')
    d2 = self.addHost('d2', ip='no ip defined/24')

    CCServer1 = self.addHost('CCServer1',ip='10.3.3.0')
    CCServer2 = self.addHost('CCServer2',ip='10.3.3.1')

    self.addLink(h1,switch1, bw=3)
    self.addLink(h2,switch1, bw=3)
    self.addLink(h3,switch1, bw=3)
    self.addLink(h4,switch1, bw=3)

    self.addLink(d1,switch2, bw=3)
    self.addLink(d2,switch2, bw=3)

    self.addLink(CCServer1,switch4, bw=10)
    self.addLink(CCServer2,switch5, bw=3)


def configure():
  topo = example_topo()
  net = Mininet(topo=topo, link=TCLink, controller=RemoteController)
  net.start()
  h1, h2, h3, h4, CCServer1, CCServer2, d1, d2= net.get('h1', 'h2', 'h3', 'h4', 'CCServer1', 'CCServer2', 'd1', 'd2')
  
  print("*** enable dhcpclient, and assign ip address ***")
  #h1.cmd('sudo dhclient h1-eth0')
  #h2.cmd('sudo dhclient h2-eth0')
  #h3.cmd('sudo dhclient h3-eth0')
  #h4.cmd('sudo dhclient h4-eth0')
  d1.cmd('sudo dhclient d1-eth0')
  d2.cmd('sudo dhclient d2-eth0')

  #intf_h1 = net.get('h1').defaultIntf()
  #intf_h2 = net.get('h2').defaultIntf()
  #intf_h3 = net.get('h3').defaultIntf()
  #intf_h4 = net.get('h4').defaultIntf()
  intf_d1 = net.get('d1').defaultIntf()
  intf_d2 = net.get('d2').defaultIntf()

  #intf_h1.updateIP()
  #intf_h2.updateIP()
  #intf_h3.updateIP()
  #intf_h4.updateIP()
  intf_d1.updateIP()
  intf_d2.updateIP()

  CLI(net)

  net.stop()


if __name__ == '__main__':
  configure()
