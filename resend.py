from scapy.all import rdpcap, sendp


def send_to_spec_ip(pkt, addr):
    pkt['IP'].dst = addr[0]
    pkt['Ether'].dst = addr[1]

    # del pkt['IP'].chksum
    # if pkt.haslayer('TCP'):
    #     del pkt['TCP'].chksum

    sendp(pkt, iface='以太网 2')



def main(path):
    '''
    Target IP addr and Target Mac addr
    '''
    ip = ''
    # mac = getmacbyip(ip)
    mac = '00:E0:4C:F3:01:AB'
    pkts = rdpcap(path)
    for pkt in pkts:
        send_to_spec_ip(pkt, (ip,mac))


if __name__ == '__main__':
    # path = raw_input('Please enter the file path: ')
    path = 'D:\dds.pcap'
    main(path)
