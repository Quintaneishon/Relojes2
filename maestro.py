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

        def anaSeg():
            self.hora = self.hora+datetime.timedelta(seconds=1)
            myClock1['text'] = self.hora.strftime('%H:%M:%S')
            print('añadi segundos al hilo: ',
                  threading.currentThread().getName())

        bSeg = tkinter.Button(root, text='añade segundo', command=anaSeg)
        bSeg.grid(row=1, column=2)
        # bSeg.pack()

        def anaMin():
            self.hora = self.hora+datetime.timedelta(minutes=1)
            myClock1['text'] = self.hora.strftime('%H:%M:%S')
            print('añadi minutos al hilo: ',
                  threading.currentThread().getName())

        bMin = tkinter.Button(root, text='añade minuto', command=anaMin)
        # bMin.pack()
        bMin.grid(row=1, column=1)

        def anaHor():
            self.hora = self.hora+datetime.timedelta(hours=1)
            myClock1['text'] = self.hora.strftime('%H:%M:%S')
            print('añadi horas al hilo: ', threading.currentThread().getName())

        bHor = tkinter.Button(root, text='añade hora', command=anaHor)
        # bMin.pack()
        bHor.grid(row=1, column=0)

        def redSeg():
            self.hora = self.hora-datetime.timedelta(seconds=1)
            myClock1['text'] = self.hora.strftime('%H:%M:%S')
            print('reduje segundos al hilo: ',
                  threading.currentThread().getName())

        brSeg = tkinter.Button(root, text='reduce segundo', command=redSeg)
        brSeg.grid(row=2, column=2)
        # bSeg.pack()

        def redMin():
            self.hora = self.hora-datetime.timedelta(minutes=1)
            myClock1['text'] = self.hora.strftime('%H:%M:%S')
            print('reduje un minuto al hilo: ',
                  threading.currentThread().getName())

        brMin = tkinter.Button(root, text='reduce minuto', command=redMin)
        # bMin.pack()
        brMin.grid(row=2, column=1)

        def redHor():
            self.hora = self.hora-datetime.timedelta(hours=1)
            myClock1['text'] = self.hora.strftime('%H:%M:%S')
            print('reduje una hora al hilo: ',
                  threading.currentThread().getName())

        brHor = tkinter.Button(root, text='reduce hora', command=redHor)
        # bMin.pack()
        brHor.grid(row=2, column=0)

        def acelerar():
            self.tiempo = self.tiempo/2

            # myClock1['text'] = self.hora.strftime('%H:%M:%S')
            print('acelere el reloj : ', threading.currentThread().getName())

        bAce = tkinter.Button(root, text='acelera reloj', command=acelerar)
        # bMin.pack()
        bAce.grid(row=3, column=1)

        def realentiza():

            self.tiempo = self.tiempo*2

            # myClock1['text'] = self.hora.strftime('%H:%M:%S')
            print('realentize el reloj : ', threading.currentThread().getName())

        bDece = tkinter.Button(
            root, text='realentiza reloj', command=realentiza)
        # bMin.pack()
        bDece.grid(row=4, column=1)

        def pauseReanude():
            if (self.uno == 0):
                self.uno = 1
            else:
                self.uno = 0

            # myClock1['text'] = self.hora.strftime('%H:%M:%S')
            print('pause/reanude el reloj : ',
                  threading.currentThread().getName())

        bPause = tkinter.Button(
            root, text='pause/reanude reloj', command=pauseReanude)
        # bMin.pack()
        bPause.grid(row=5, column=1)

        def randDate():
            self.hora = self.hora + \
                datetime.timedelta(seconds=random.randint(1, 1000000))
            myClock1['text'] = self.hora

        def tic():
            self.hora = self.hora+datetime.timedelta(seconds=self.uno)
            myClock1['text'] = self.hora.strftime('%H:%M:%S')

        def tac():
            tic()
            myClock1.after(int(self.tiempo), tac)

        if (threading.currentThread().getName() != 'reloj 1'):
            randDate()
            pass
        tac()

        root.mainloop()


class Comunicador(threading.Thread):
    localIP = "127.0.0.1"
    localPort = 20001
    bufferSize = 1024

    # Create a datagram socket
    UDPServerSocket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))
    print("UDP server up and listening")

    def run(self):

        # Listen for incoming datagrams
        while(True):

            bytesAddressPair = self.UDPServerSocket.recvfrom(self.bufferSize)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]

            clientMsg = "Message from Client:{}".format(message)
            clientIP = "Client IP Address:{}".format(address)
            msgFromServer = r1.hora.strftime('%H:%M:%S')
            bytesToSend = str.encode(msgFromServer)

            print(clientMsg)
            print(clientIP)

            # Sending a reply to client
            self.UDPServerSocket.sendto(bytesToSend, address)


class Comunicador2(threading.Thread):
    localIP = "127.0.0.1"
    localPort = 20002
    bufferSize = 1024

    # Create a datagram socket
    UDPServerSocket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))
    print("UDP server up and listening")

    def run(self):

        # Listen for incoming datagrams
        while(True):

            bytesAddressPair = self.UDPServerSocket.recvfrom(self.bufferSize)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]

            clientMsg = "Message from Client:{}".format(message)
            clientIP = "Client IP Address:{}".format(address)
            hour = r1.hora+datetime.timedelta(hours=1.5)
            msgFromServer = hour.strftime('%H:%M:%S')
            bytesToSend = str.encode(msgFromServer)

            print(clientMsg)
            print(clientIP)

            # Sending a reply to client
            self.UDPServerSocket.sendto(bytesToSend, address)


class Comunicador3(threading.Thread):
    localIP = "127.0.0.1"
    localPort = 20003
    bufferSize = 1024

    # Create a datagram socket
    UDPServerSocket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))
    print("UDP server up and listening")

    def run(self):

        # Listen for incoming datagrams
        while(True):

            bytesAddressPair = self.UDPServerSocket.recvfrom(self.bufferSize)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]

            clientMsg = "Message from Client:{}".format(message)
            clientIP = "Client IP Address:{}".format(address)
            hour = r1.hora-datetime.timedelta(hours=1.5)
            msgFromServer = hour.strftime('%H:%M:%S')
            bytesToSend = str.encode(msgFromServer)

            print(clientMsg)
            print(clientIP)

            # Sending a reply to client
            self.UDPServerSocket.sendto(bytesToSend, address)


def prueba():
    print("prueba")


r1 = relojHilo(name="maestro")
but = tkinter.Button(r1.root, text='prueba', command=prueba)
# bMin.pack()
r1.brMin.grid(row=6, column=1)
r1.start()
c1 = Comunicador(name="co1", args=(r1))
c1.start()
c1 = Comunicador2(name="co2", args=(r1))
c1.start()
c1 = Comunicador3(name="co3", args=(r1))
c1.start()
