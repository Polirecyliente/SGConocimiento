<!--
#   Ubuntu software

#T# Table of contents

#C# Connect two computers with an Ethernet cable

#T# Beginning of content
-->

# Connect two computers with an Ethernet cable

These steps require the `network-manager` service and the `nm-connection-editor` command
1. Label the computers as computer A and computer B.
2. Connect the computers with an Ethernet cable (both patch and crossover cables should be good).

On computer A

3. : Right-click on the network tray icon > Click on "Edit Connections". The "Network Connections" window opens.
    - Note: If right-click doesn't work, execute the `nm-connection-editor` command in a shell.
4. Click the plus sign to add a new connection.
5. Select "Ethernet" from the drop-down menu.
6. In the "Ethernet" tab, "Cloned MAC address" text field, type the MAC address of computer A (this can be checked with the `ifconfig` command)
7. In the "IPv4 Settings" tab, "Method" drop-down menu, select "Manual".
8. In the "Addresses" pane, click the "Add" button. Type a unique IP address in the "Address" field, e.g. "10.0.0.1". Type the network mask in the "Netmask" field, e.g. "255.255.255.0" so that IPs can only change the last number.
9. Click save.

On computer B

10. Repeat steps 3 to 9, but with computer B, i.e. using the MAC address of computer B, and a unique IP address suchas "10.0.0.2".

After these steps

11. Ping computer B using computer A and vice versa, using the unique IP. If the ping works then the connection is established.