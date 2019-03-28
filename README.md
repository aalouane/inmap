### inmap

inmap is a python library which helps in using nmap port scanner.
It allows to easilly manipulate nmap scan results and will be a perfect
tool for systems administrators who want to automatize scanning task
and reports. 

You have to install nmap


### Usage :: 

   #!/usr/bin/env python
    import inmap                         # import inmap.py module
    
    scan = inmap.ScanController()
    host = inmap.HostModel()
    port = inmap.PortModel()

    # Scan host :
    
    # nmap [-Pn] [-sU]  [-sU] -p ports scantest.nmap.org -T5
    scan.scan_ports(host='scantest.nmap.org', ports='0-200')
    # OR
    scan.scan_ports(host="192.168.1.0/24", ports='0-200')
    # udp ports scan : root privilege is needed
    scan.scan_ports(host="192.168.1.0/24", ports='0-200', udp = True)
    # For the -Pn option
    scan.scan_ports(host="192.168.1.0/24", pn = True, ports='0-200')
    
    # sudo nmap [-Pn] [-sU]  [-n] -sS -sV -O scantest.nmap.org
    # root privilege is needed for this method
    scan.scan_all(host="scantest.nmap.org")
    # OR
    scan.scan_all(host="192.168.1.0/24")
    
    # nmap [-Pn] [-sU]  -sV -p ports scantest.nmap.org -T5
    scan.scan_version_port(host="scantest.nmap.org", ports='0-200')
    # OR
    scan.scan_version_port(host="192.168.1.0/24", ports='0-200')
    
    # nmap [-Pn] [-sU]  [-sV] --top-ports 15 scantest.nmap.org -T5
    scan.scan_most_ports(host='scantest.nmap.org', number=15)
    # OR
    scan.scan_most_ports(host='192.168.1.0/24', number=15)
    
    # for use -Pn option:
    scan.scan_ports(host='scantest.nmap.org', ports='0-200', pn=True)
    
    # for use -sU(udp scan) option: root privilege is needed
    scan.scan_ports(host='scantest.nmap.org', ports='0-200', udp = True)
    
    ############### The results are stored in db sqlite ###############
    
    # To get and manipulate the results:
    
    # we can specify one of the possible argument of scanning results:
    # 'ip_address', 'mac_address', 'hostname', 'os_family', 'os_cpe', 'os_details',
    # 'device_type', 'info_host', 'info_cpe', 'info_os', 'network_distance'
    
    # Get all hosts scanned
    results = host.host_select()
    
    # For inspecting the results
    print(results)
    
    # the results is a list of dictionary 
    # Examples : 
    # For a single result :
    print(result['ip_address']) ==> 192.168.1.10
    
    # For multiple results:
    print(results[2]['os_family']) ==> "Linux"
    
    # one row that contain the information of this host
    result = host.host_select(ip_address='192.168.1.1')
    
    # To know the state of this host
    result['state']
    
    ######### To get and manipulate the results of port scanning ########
    
    # we can specify one of the possible argument of scanning results:
    # 'ip_address', 'port', 'proto', 'state', 'service', 'version'
    
    # Get all results for the 22 port
    results = port.port_select(port=22)
    
    # For inspecting the results
    print(results)
    
    # we can show the version
    # For a single result
    print(results['version'])
    
    # To know the host for this port
    # For multiple results
    print(results[3]['ip_address'])
    
    # To know the state of this port
    print(result['state'])
    

