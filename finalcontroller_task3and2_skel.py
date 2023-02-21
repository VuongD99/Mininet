# Final Skeleton
#
# Hints/Reminders from Lab 3:
#
# To check the source and destination of an IP packet, you can use
# the header information... For example:
#
# ip_header = packet.find('ipv4')
#
# if ip_header.srcip == "1.1.1.1":
#   print "Packet is from 1.1.1.1"
#
# Important Note: the "is" comparison DOES NOT work for IP address
# comparisons in this way. You must use ==.
# 
# To send an OpenFlow Message telling a switch to send packets out a
# port, do the following, replacing <PORT> with the port number the 
# switch should send the packets out:
#
#    msg = of.ofp_flow_mod()
#    msg.match = of.ofp_match.from_packet(packet)
#    msg.idle_timeout = 30
#    msg.hard_timeout = 30
#
#    msg.actions.append(of.ofp_action_output(port = <PORT>))
#    msg.data = packet_in
#    self.connection.send(msg)
#
# To drop packets, simply omit the action.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):
    # This is where you'll put your code. The following modifications have 
    # been made from Lab 3:
    #   - port_on_switch: represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet.
    #      (for example, s1 would have switch_id == 1, s2 would have switch_id == 2, etc...)
    # You should use these to determine where a packet came from. To figure out where a packet 
    # is going, you can use the IP header information.
    

    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)
    msg_idle_timeout = 100
    msg_hard_timeout = 100

    def flood():
       msg.data = packet_in
       msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
       self.connection.send(msg)

    def drop():
       self.connection.send(msg)

    #check whether packet is ARP, ICMP, or TCP
    isARP = packet.find('arp')
    isICMP = packet.find('icmp')
    isTCP = packet.find('tcp')
    #variables for all host addresses
    h1 = "10.1.1.13"
    h2 = "10.1.1.14"
    h3 = "10.1.1.15"
    h4 = "10.1.1.16"
    d1 = "10.2.2.15"
    d2 = "10.2.2.16"
    CC1 = "10.3.3.1"    

    ip_packet = packet.payload          
    #if packet is not an arp packet
    if (isARP==None):
       #extract source and destination address
       sourceIP = ip_packet.srcip
       destIP = ip_packet.dstip
       #print "------------------------------------"
       #print sourceIP
       #print destIP
       #print "--------------"
       if (isICMP != None or isTCP != None):
          if (switch_id==1):
             if (destIP == h1):
                #print "Going to h1, --> port 1 (switch1)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=1))
                self.connection.send(msg)
             elif (destIP == h2):
                #print "Going to h2, --> port 2 (switch1)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=2))
                self.connection.send(msg)
             elif (destIP == h3):
                #print "Going to h3, --> port 3 (switch1)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=3))
                self.connection.send(msg)
             elif (destIP == h4):
                #print "Going to h4, --> port 4 (switch1)"
                msg.data = packet_in  
                msg.actions.append(of.ofp_action_output(port=4))
                self.connection.send(msg)
             elif (destIP == d1):
                #print "Going to d1, --> port 7 (switch1)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=7))
                self.connection.send(msg)
             elif (destIP == d2):
                #print "Going to d2, --> port 7 (switch1)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=7))
                self.connection.send(msg)
             elif (destIP == CC1):
                #print "Going to CC1, --> port 5 (switch1)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=5))
                self.connection.send(msg)
          elif (switch_id==2):
             if (destIP == CC1):
                #print "Going to CC1, --> port 2 (switch2)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=2))
                self.connection.send(msg)
             elif (destIP == h1 or destIP == h2 or destIP == h3 or destIP == h4):
                #print "Going to h1234, --> port 1 (switch2)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=1))
                self.connection.send(msg)
          elif (switch_id==3):
             if (port_on_switch == 1):
                #print "Going out from d1, DROPPING"
                drop()
             elif (port_on_switch == 2):
                #print "Going out from d2, DROPPING"
                drop()
             elif (destIP == d1):
                #print "Going to d1, --> port 1(DROPPING)"
                drop()
             elif (destIP == d2):
                #print "Going to d2, --> port 2 (DROPPING)"
                drop()
             elif (destIP == h1):
                #print "Going to h1, --> port 3 (switch3)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=3))
                self.connection.send(msg)
             elif (destIP == h2):
                #print "Going to h2, --> port 3 (switch3)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=3))
                self.connection.send(msg)
             elif (destIP == h3):
                #print "Going to h3, --> port 3 (switch3)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=3))
                self.connection.send(msg)
             elif (destIP == h4):
                #print "Going to h4, --> port 3 (switch3)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=3))
                self.connection.send(msg)
          elif (switch_id==4):
             if (destIP == CC1):
                #print "Going to CC1, --> port 3 (switch4)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=3))
                self.connection.send(msg)
             elif (destIP == h1 or destIP == h2 or destIP == h3 or destIP == h4):
                #print "Going to h1234, --> port 1 (switch4)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=1))
                self.connection.send(msg)
    #if packet is an arp packet
    else:
       #print "Is an ARP Packet"
       flood()
       #if (switch_id != 3):
       #   print "ARP packet from Switch 1/2/4/5, flooding"
       #   flood()
       #else:
       #   if (port_on_switch == 1 or port_on_switch == 2):
       #      print "ARP coming from d1 or d2, DROPPING"
       #      drop()
       #   else:
       #      print "ARP on switch 3 but NOT from d1 or d2, flooding"
       #      flood()
    #print "-----------------------------------------"


  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
