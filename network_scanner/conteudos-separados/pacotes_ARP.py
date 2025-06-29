from scapy.all import ARP, Ether, srp

requisicao_arp = ARP(pdst="192.168.1.0/24")
pacote = Ether(dst="ff:ff:ff:ff:ff:ff")

envio_de_pacote = pacote / requisicao_arp

envio_de_pacote.show()