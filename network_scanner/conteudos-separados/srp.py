from scapy.all import ARP, Ether, srp

target = "192.168.10.0/24"
package = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target)

# Envia um requisição para cada host dentro do CIDR especificado em "target" e aguarda uma resposta de MAC/IP
reply, _ = srp(package, timeout=2, verbose=False)

# Itera sobre cada IP:
if reply:
    for _, recebido in reply:
        print(f"[+] Resposta recebida do IP {recebido.psrc} com o endereço MAC: {recebido.hwsrc}")
        # print(f"[-] Pacote não recebido no IP: {nao_enviado.psrc}")
else:
    print("Não foi recebido nenhum endereço MAC.")