import sys
from scapy.all import ARP, Ether, srp

def arp_scan(network):

    # Construindo pacote ARP + IP
    package = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network)

    reply, _ = srp(package, timeout=2, verbose=False) # É enviado dois pacotes (pck_enviados, pck_recebidos)

    hosts = []
    for _, host in reply:
        hosts.append({'ip': host.psrc, 'mac': host.hwsrc, 'lenght': len(host)})
    return hosts


if __name__ == "main":
    if len(sys.argv) != 2:
        print(f"Uso {sys.argv[0]} <rede/CIDR>")
        sys.exit(1)

net = sys.argv[1]
print(f"\n[...] Escaneando a rede {net} via ARP...")
ips_found = arp_scan(net)

if ips_found:
    print("\nHosts ativos: ")
    for host in ips_found:
        print(f"[+] - IP {host['ip']} MAC: {host['mac']} | Tamanho do Pacote: {host['lenght']} bytes")
else:
    print("[-] Nenhum host encontrado :/ ")