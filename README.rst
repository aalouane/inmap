======================
Inmap
======================

Introduction
------------

inmap is a python library which helps in using nmap port scanner.   
It allows to easilly manipulate nmap scan results and will be a perfect tool for systems administrators who want to automatize scanning task and reports.

Supported Python Versions
-------------------------

* Python 3.4+

Installing nmap scanner
-----------------------

inmap requires the nmap scanner : `<https://nmap.org/download.html>`_

**Debian based system**::  

    sudo apt-get install nmap

**Red Hat based system**::

    yum install nmap 

**ArchLinux**:: 

    pacman -S nmap                       

**OpenSuse**::

    yast2 -i nmap          

**Mac OS X**::  

    brew install nmap          

Install inmap package
---------------------

If you have `pip3 <https://pip.pypa.io/>`_ on your system, you can simply install or upgrade the Python bindings::

    pip3 install inmap

Alternately, you can download the source distribution from `PyPI <https://pypi.org/project/inmap/#files>`_ (e.g. inmap-1.2.7.tar.gz), unarchive it, and run::

    python setup.py install

Example 0: Port Scanning
------------------------

.. code-block:: python

    import inmap

    scan = inmap.ScanController()
    host = inmap.HostModel()
    port = inmap.PortModel()

    scan.scan_ports(host='scantest.nmap.org', ports='0-200')
    scan.scan_ports(host='scantest.nmap.org', ports='22')
    # You can use the udp and|or pn option
    scan.scan_ports(host="scantest.nmap.org", ports='80', udp = True, pn = True)

    # Fetch results
    # =============

    # for port infos the possible arguments are :  ip_address - port - proto - state - service -version

    results = port.select()

    # Or
    results = port.select(state = 'open')
    results = port.select(port = 80)
    results = port.select(ip_address = "10.10.10.5")

    # and so on

    # Display results
    # ===============
    print(results)

    # if we have a single line of result
    prints(results['ip_address'])
    prints(results['port'])
    prints(results['proto'])
    prints(results['state'])
    prints(results['service'])
    prints(results['version']) # for version info see the next example

    # for many results
    print(results[0]['port'])
    print(results[1]['service'])

    # Or
    for result in results:
        print(result['ip_address'], ' - ', result['port'], ' - ', result['proto'], ' - ', result['state'], ' - ', result['service'])

Example 1: Port Scanning with their version
-------------------------------------------

.. code-block:: python

    import inmap

    scan = inmap.ScanController()
    host = inmap.HostModel()
    port = inmap.PortModel()

    scan.scan_version_port(host="scantest.nmap.org", ports='0-200')

    # or
    scan.scan_version_port(host="scantest.nmap.org", ports='80')

    # You can use the udp and|or pn option
    scan.scan_version_port(host="scantest.nmap.org", ports='80', udp = True, pn = True)

    # For fetch and displaying results, see the example 0

Example 2: scan the 10 most ports
---------------------------------

.. code-block:: python

    import inmap

    scan = inmap.ScanController()
    host = inmap.HostModel()
    port = inmap.PortModel()

    scan.scan_most_ports(host='scantest.nmap.org')

    # Or scan the 20 most ports
    scan.scan_most_ports(host='10.10.10.3', number = 20)

    # You can use the udp and|or pn option
    scan.scan_most_ports(host='10.10.10.3', number = 20, udp = True, pn = True)

    # For fetch and displaying results, see the example 0

Example 3: all information that we can have about this host : OS Detection, Port Scanning ...
---------------------------------------------------------------------------------------------

.. code-block:: python

    import inmap

    scan = inmap.ScanController()
    host = inmap.HostModel()
    port = inmap.PortModel()

    # Take more time and need root privilege
    scan.scan_all(host='scantest.nmap.org')
    # You can use the udp and|or pn option
    scan.scan_most_ports(host='10.10.10.3', udp = True, pn = True)

    # Or scan the 20 most ports
    scan.scan_most_ports(host='10.10.10.3', number = 20)

    # You can use the udp and|or pn option
    scan.scan_most_ports(host='10.10.10.3', number = 20, udp = True, pn = True)

    # Fetch results
    # =============

    # for host infos the possible arguments are :
    # ip_address, mac_address, hostname, os_family, os_cpe, os_details, device_type, info_host, info_cpe, info_os, network_distance
    results = host.select()

    # Or
    results = host.select(state = 'Up') # state : Up | Down
    results = host.select(ip_address = "10.10.10.5")
    results = host.select(mac_address = "08:00:27:D3:EB:F1")
    results = host.select(hostname = "scantest.nmap.org")

    # and so on, for port infos the possible arguments are :  ip_address - port - proto - state - service -version

    # Display results
    # ===============
    print(results)

    # if we have a single line of result
    prints(results['ip_address'])
    prints(results['mac_address'])
    prints(results['hostname'])
    prints(results['state'])
    prints(results['os_details'])
    prints(results['network_distance']) # for version info see the next example

    # for many results
    print(results[0]['state'])
    print(results[1]['ip_address'])
    print(results[1]['network_distance'])
    print(results[1]['os_family'])

    # Or
    for result in results:
        print(result['ip_address'], ' - ', result['mac_address'], ' - ', result['hostname'], ' - ', result['os_family'])

    # For fetch and displaying port results, see the example 0
