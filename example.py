#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
example.py - 2011.11.09

Author : Aalouane Soufiane - aalouane.s@gmail.com
Licence : GPL v3 or any later version


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import inmap                         # import inmap.py module

scan = inmap.ScanController()
host = inmap.HostModel()
port = inmap.PortModel()

scan.scan_ports(host="10.10.10.3", ports="20-200")
# the results of scan are saved in db sqlite

results = inmap.host_select()
# Data structure looks like :
#
#       Host:
#      [
#        {
#           'ip_address':           '192.168.1.1',
#           'mac_address':          '08:01:26:F3:5B:2F',
#           'hostname':             'scantest.nmap.org',
#           'os_family':            'Linux 3.X',
#           'os_cpe':               'cpe:/o:linux:linux_kernel:3',
#           'os_details':           'Linux 3.5 - 3.8',
#           'device_type':          'general purpose'
#           'info_host':            '',
#           'info_cpe':             '['CPE:', 'cpe:/o:linux:linux_kernel']',
#           'info_os':              '['localhost']',
#           'network_distance':     '1 hop'
#        },
#        ....
#
#       ]
#
#       Port:
#       [
#         {
#           'ip_address' :          '192.168.1.1',
#           'port'       :          '22',
#           'proto'      :          'tcp',
#           'state'      :          'open',
#           'service'    :          ' OpenSSH 2.4p1 Debian 16ubuntu1',
#         },
#         {
#           'ip_address' :          '192.168.1.1',
#           'port'       :          '23',
#           'proto'      :          'tcp',
#           'state'      :          'open',
#           'service'    :          ' Microsoft Windows XP telnetd',
#         },
#         ....
#       ]
#
#
#
#
#


# for the scan_all method you need the root privileges
scan.scan_all(host='192.168.1.1')  # scan host 192.168.1.1, all information that we can have about this host
result  = host.host_select(ip_address='192.168.1.1')   # get all information about this host
result['hostname']                  # get the host name
result['mac_address']               # get the mac address
result['os_family']                 # get the os_family

scan.scan_ports(host="192.168.1.", ports="0-200") # scan all tcp ports(0-200)
scan.scan_ports(host="192.168.1.", ports="0-200", udp = True) # scan all tcp & upd(root privilege is needed) ports(0-200)

scan.scan_version_ports(host="192.168.1.", ports="0-200") # scan all tcp ports(0-200) try to get their version
scan.scan_version_ports(host="192.168.1.", ports="0-200", upd = True, pn = True)
# The pn arguments for nmap -Pn

scan.scan_most_ports(host='10.10.10.3') # scan the 10 most ports
scan.scan_most_ports(host='10.10.10.3', number = 20) # scan the 20 most ports
# You can use the udp and|or pn option
scan.scan_most_ports(host='10.10.10.3', number = 20, udp = True, pn = True)


results = host.host_select()       # get all hosts that were scanned
for result in results:
    print(result['ip_address'], ' - ', result['mac_address'], ' - ', result['hostname'], ' - ', result['os_family'])

