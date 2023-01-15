import os
import sys
import pyshark
import requests
import time
try:
    # Please paste this in the terminal: files/pingedpackets.pcapng
    filename = input("Enter path of file to read: ").strip()
    cap = pyshark.FileCapture(filename, display_filter='arp')
    i = 0
    url = "https://api.macvendors.com/"
    for packet in cap:
        i = i+1
        try:
            print("\n------------- Packet ", i, " -----------------")

            sourceMac = packet['arp'].src_hw_mac
            destMac = packet['arp'].dst_hw_mac

            print("\nDevice 1")
            response1 = requests.get(url+sourceMac)
            time.sleep(1)
            print("src mac: ", sourceMac)
            print(response1.content.decode())

            print("\nDevice 2")
            print("dest mac: ", destMac)
            response2 = requests.get(url+destMac)
            time.sleep(1)
            print(response2.content.decode())

        except Exception as err:
            pass
            print('\nAn error has occurred: ')
            print(err)
            print()
    cap.close()

except Exception as err:
    pass
    print('\nAn error has occurred: ')
    print(err)
    print()
