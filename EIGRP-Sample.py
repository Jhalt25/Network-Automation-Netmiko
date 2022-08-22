from netmiko import ConnectHandler

from getpass import getpass

 

user = getpass('User: ')

passw = getpass('Passwd: ')

sec = getpass('Secret: ')

 

ir1100 = { 'device_type': 'cisco_ios', 'ip': '10.0.0.1', 'username': user, 'password': passw, 'secret': sec }

connect = ConnectHandler(**ir1100)

connect.enable()

 

# various setup commands

setup = [ 'vtp mode transparent', 'no cdp run' , 'no lldp run',

          'clock timezone CST -6 0', 'clock summer-time CDT recurring',

          'ip route 0.0.0.0 0.0.0.0 10.0.100.254',

          'ntp server 192.168.2.1'

          ]

 

# Eigrp advertisements for both WANs, Loopback, and LAN

eigrp = ['router eigrp 10',

         'network 10.0.100.0 0.0.0.255',

         'network 10.0.200.0 0.0.0.255',

         'network 10.0.255.0 0.0.0.63',

         'network 192.168.1.1 0.0.0.0'

         ]

 

# three vlans | 2 WAN Connections | 1 62 host LAN

vlan = ['interface vlan 1', 'shut', 'vlan 100', 'exit', 'vlan 200', 'exit', 'vlan 300', 'exit',

        'interface vlan 100', 'ip address 10.0.100.1 255.255.255.0', 'no shut', 'description Wan Connection',

        'interface vlan 200', 'ip address 10.0.200.1 255.255.255.0', 'no shut', 'description Wan Connection',

        'interface vlan 300', 'ip address 10.0.255.1 255.255.255.192', 'no shut', 'description Lan /26(62 Host)'

        ]

 

# interfaces

int = [ 'interface fastEthernet 0/0/1', 'switchport mode access', 'switchport access vlan 100', 'no shut', 'exit',

    'interface fastEthernet 0/0/2', 'switchport mode access', 'switchport access vlan 200', 'no shut', 'exit',

    'interface fastEthernet 0/0/3', 'switchport mode access', 'switchport access vlan 300', 'no shut', 'exit',

    'interface fastEthernet 0/0/4', 'shut', 'exit', 'interface loopback 0', 'ip address 192.168.1.1 255.255.255.255'

        ]

 

 

send = connect.send_config_set(setup)

print(send)

input('Press Enter...')

send = connect.send_config_set(vlan)

print(send)

input('Press Enter...')

send = connect.send_config_set(int)

print(send)

input('Press Enter...')

send = connect.send_config_set(eigrp)

print(send)

input('Press Enter...')

input('Enter to exit')
