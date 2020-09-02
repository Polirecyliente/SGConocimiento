
#   Firewall

#T# Table of contents

#T# Uncomplicated Firewall

#T# Beginning of content

#T# Uncomplicated Firewall

# |-------------------------------------------------------------
#T# the ufw program serves to manage the firewall, UFW stands for Uncomplicated Firewall, it acts as a wrapper for iptables
ufw status verbose

#T# enable or disable the firewall
# SYNTAX ufw enable|disable

# |--------------------------------------------------\
#T# firewall rules decide whether or not to allow connections, set the default policies which are the rules that apply when there is no rule defined

# SYNTAX ufw default deny|reject|allow incoming|outgoing
#T# this denies, rejects, or allows, incoming or outgoing connections, unless overruled by an explicit rule

#T# the difference between deny and reject is that reject sends and error message to the connecting agent, while deny just ignores the connection attempt

ufw default deny incoming
ufw default allow outgoing
#T# these are normally the default policies for a firewall
# |--------------------------------------------------/

#T# from now on, the deny, reject, and allow arguments will be used for other commands, but their meaning is the same as with the default policies

# |--------------------------------------------------\
#T# create explicit rules to allow or deny different connections

# SYNTAX ufw deny|reject|allow port1|service_name1
#T# port1 is a port number, service_name1 is a string with a service name, they are interchangeable, their equivalencies are set in the /etc/services file

ufw allow 22
ufw allow ssh
#T# both examples are equivalent
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# create rules with port ranges and protocols

# SYNTAX ufw deny|reject|allow port1:port2/[protocol1]
#T# the port range is from the port1 number to the port2 number, protocol1 is the network protocol, such as tcp, udp, and if it's not written is the same as both tcp and udp

ufw reject 5000:6030/tcp
#T# this rejects all IPs connecting to ports 5000 to 6030 using tcp
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# the IP addresses can follow the Classless Inter Domain Routing style (CIDR numbers), CIDR numbers represent IP ranges

#T# an IPv4 address is made up with four 8 bit numbers, separated by dots, for a total of 32 bits, such as 10110010.11001011.11010001.11101111

# SYNTAX byte1.byte2.byte3.byte4/CIDR_number1
#T# the CIDR_number1 number is the amount of bits that do not change in the IP range, starting at the first bit

IP_RANGE1=192.168.255.0/31
#T# as the CIDR number is 31, the first 31 bits of the IP range remain unchanged, so the resulting IP range only has the last bit, the bit 32, varying
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# create rules about specific IPs

# SYNTAX ufw deny|reject|allow from ip1 to ip2 port port1
#T# ip1, ip2 are IP numbers or IP ranges, this sets a rule for a connection from ip1 to ip2 in port port1

ufw allow from 192.168.0.0/24 to 192.168.0.13 port 443
#T# IPs in the range [192.168.0.0, 192.168.0.255] are allowed to connect in port 443, this host is 192.168.0.13
# |--------------------------------------------------/

# |--------------------------------------------------\
#T# create rules about network interfaces

# SYNTAX ufw deny|reject|allow incoming|outgoing on net1 from ip1
#T# net1 is the network interface protected by the rule, ip1 is the connecting IP number or range

ufw deny incoming on wlp3s0 from 236.217.38.92
#T# this denies connections from the IP 236.217.38.92 to the wireless network interface identified by wlp3s0
# |--------------------------------------------------/

#T# list the available firewall rules by number
ufw status numbered

#T# delete a rule by number
ufw delete 2

#T# reset the firewall rules to default settings
ufw reset
# |-------------------------------------------------------------