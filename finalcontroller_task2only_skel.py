#File for task 2 implementation

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

    #find whether the packet is ARP, ICMP, or TCP
    isARP = packet.find('arp')
    isICMP = packet.find('icmp')
    isTCP = packet.find('tcp')
    #variables for all the host addresses
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
          #print "Is an ICMP or TCP packet"
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
             if (destIP == d1):
                #print "Going to d1, --> port 1 (switch3)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=1))             
                self.connection.send(msg)
             elif (destIP == d2):
                #print "Going to d2, -->  port 2 (switch3)"
                msg.data = packet_in
                msg.actions.append(of.ofp_action_output(port=2))
                self.connection.send(msg)
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
       #print "Is an ARP packet, flooding"
       flood()
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
