import argparse
import scapy.all as scapy

class ARPPing():
    def __init__(self):
        print("Arp Ping Started...")

    def get_Input(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i","--ipaddress",type=str,help="You must enter your IP address")

        args = parser.parse_args()

        if args.ipaddress != None:
            return args
        else:
            print("Please enter ip address with -i argument.")

    
    def arp_request(self,ip):
        arp_request_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packet = broadcast_packet/arp_request_packet

        (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=2)
        answered_list.summary()


if __name__ == "__main__":
    arp_ping = ARPPing()
    input = arp_ping.get_Input()
    arp_ping.arp_request(input.ipaddress)