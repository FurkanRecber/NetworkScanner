import scapy.all as scapy
import optparse


def get_ip():
    option_parser = optparse.OptionParser()
    option_parser.add_option("-i", "--ipaddress", dest="ipaddress", help="specify the ip address")
    (user_input, args) = option_parser.parse_args()

    if not user_input.ipaddress:
        print("Please specify the ip address")

    return user_input.ipaddress


def scan_network(ipaddress):
    arp_request = scapy.ARP(pdst=ipaddress)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast / arp_request
    (answered, unanswered) = scapy.srp(combined_packet, timeout=1)
    answered.summary()


user_inputs = get_ip()
scan_network(user_inputs)
