import nmap
import subprocess
import getpass
import xml.etree.ElementTree as ET

def run_sudo_nmap_command(command, password):
    """Run nmap command with sudo and capture output."""
    result = subprocess.run(['sudo', '-S'] + command.split(), input=password + '\n', text=True, capture_output=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {result.stderr}")
    return result.stdout

def scan_network(hosts, ports, arguments, use_sudo, password):
    nm = nmap.PortScanner()
    command = f'nmap {arguments} -p {ports} {hosts}'
    if use_sudo:
        print(f'Executing command: sudo {command}')
        output = run_sudo_nmap_command(command, password)
    else:
        print(f'Executing command: {command}')
        output = subprocess.run(command.split(), capture_output=True, text=True).stdout
    
    if "Note: Host seems down" in output:
        print("El host parece estar abajo. Intentando con -Pn")
        command += " -Pn"
        if use_sudo:
            print(f'Executing command: sudo {command}')
            output = run_sudo_nmap_command(command, password)
        else:
            print(f'Executing command: {command}')
            output = subprocess.run(command.split(), capture_output=True, text=True).stdout
    
    with open('nmap_output.xml', 'w') as f:
        f.write(output)

    try:
        scan_result = nm.analyse_nmap_xml_scan(output)
    except ET.ParseError as e:
        raise nmap.PortScannerError(f"XML parse error: {e}\nOutput: {output}")
    
    print('Scan result:')
    for host in nm.all_hosts():
        print(f'Host: {host} ({nm[host].hostname()})')
        print(f'State: {nm[host].state()}')
        for proto in nm[host].all_protocols():
            print(f'Protocol: {proto}')
            lport = nm[host][proto].keys()
            for port in lport:
                print(f'Port: {port}\tState: {nm[host][proto][port]["state"]}')
    return scan_result

def main():
    print("Bienvenido al escáner de red Nmap en Python")
    hosts = input("Ingrese los hosts: ")
    ports = input("Ingrese los puertos: ")
    arguments = input("Ingrese los argumentos de Nmap: ")
    use_sudo = input("¿Desea ejecutar el comando como superusuario? (s/n): ").lower() == 's'
    
    password = None
    if use_sudo:
        password = getpass.getpass(prompt='Ingrese su contraseña de sudo: ')

    scan_result = scan_network(hosts, ports, arguments, use_sudo, password)

if __name__ == "__main__":
    main()
