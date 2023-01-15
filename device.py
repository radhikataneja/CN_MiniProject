import os
import sys
# Used to capture packets from pcap
import pyshark
# Getting device type from useragent
from user_agents import parse
# GUI
from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont

root = Tk()
fontStyle = tkFont.Font(family="Lucida Grande", size=15)
root.geometry("1500x600")


def isMobileDevice(useragent):
    user_agent = parse(useragent)
    if user_agent.is_mobile:
        return True
    else:
        return False


def isTabletDevice(useragent):
    user_agent = parse(useragent)
    if user_agent.is_tablet:
        return True
    else:
        return False


def isPC(useragent):
    user_agent = parse(useragent)
    if user_agent.is_pc:
        return True
    else:
        return False


def getUserAgent():
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file")

    if root.filename == '':
        print("No file selected")
        sys.exit()
    else:
        useragents = []
        cap = pyshark.FileCapture(
            root.filename, display_filter='frame contains "GET"')
        for packet in cap:
            print(packet['http'].user_agent)
            useragents.append(packet['http'].user_agent)
        i = 0
        for useragent in useragents:
            i = i+1
            if isMobileDevice(useragent):
                myLabel = Label(
                    root, text="Device Type : Mobile", font=fontStyle)
                myLabel.pack()
            elif isTabletDevice(useragent):
                myLabel = Label(
                    root, text="Device Type : Tablet", font=fontStyle)
                myLabel.pack()
            elif isPC(useragent):
                myLabel = Label(
                    root, text="Device Type : PC", font=fontStyle)
                myLabel.pack()
            else:
                myLabel = Label(
                    root, text="Device Type : Unknown", font=fontStyle)
                myLabel.pack()

            myLabel = Label(root, text="Packet"+str(i) +
                            ":  " + useragent+"\n", font=fontStyle)

            myLabel.pack()

        cap.close()


fileInputBtn = Button(root, text="Choose file to scrape", font=fontStyle,
                      command=getUserAgent)

fileInputBtn.pack()

root.mainloop()
