import socket
from tkinter import *
import tkinter
import threading
import time
import random
import datetime
from time import strftime


class relojHilo(threading.Thread):
    hora = datetime.datetime.now()
    tiempo = 1000
    uno = 1

    def run(self):
        root = tkinter.Tk()
        root.title(threading.currentThread().getName())
        myClock1 = tkinter.Label(root)
        today = datetime.datetime.now()
        hora = today
        myClock1['text'] = today
        myClock1['font'] = 'Tahoma 50 bold'
        myClock1.grid(row=0, column=0, columnspan=3)
        # myClock1.pack()

        def tic():
            self.hora = self.hora+datetime.timedelta(seconds=self.uno)
            myClock1['text'] = self.hora.strftime('%H:%M:%S')

        def tac():
            tic()
            myClock1.after(int(self.tiempo), tac)
        tac()
        root.mainloop()

class Comunicador(threading.Thread):
    msgFromClient = "Hello UDP Server"
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = ("127.0.0.1", 20002)
    bufferSize = 1024
    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    def run(self):
        r1 = relojHilo(name="principal")
        r1.start()
        # Send to server using created UDP socket
        self.UDPClientSocket.sendto(self.bytesToSend, self.serverAddressPort)
        
        while (True):
            msgFromServer = self.UDPClientSocket.recvfrom(self.bufferSize)
            msg = "mensaje del servidor: "+str(msgFromServer[0], encoding)
            print(msg)
            r1.hora = datetime.datetime.strptime(str(msgFromServer[0], encoding), '%H:%M:%S')

encoding = 'utf-8'
c1=Comunicador(name="hilo1")
c1.start()
