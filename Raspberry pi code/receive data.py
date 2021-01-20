import socket
import time
import threading
import schuifregister
import ledstrip
import servo
import button
import pieper
import afstandmeter
s = socket.socket()
host = '192.168.1.139' #ip of raspberry pi
port = 12345
s.bind((host, port))

s.listen(5)
c, addr = s.accept()

def send_data():
    afstandthread = threading.Thread(target=afstandmeter.sr04, args=(24, 23,))
    afstandthread.start()
    thread = threading.Thread(target=button.button).start()
    AFK = False
    while True:
        count = 0
        
        while afstandmeter.distance < 9:
            if button.switchstate:
                print('send')
                data = 'FLASHBANG'
                c.send(data.encode())
            time.sleep(0.1)
            count += 1
            if not AFK:
                print('send')
                data = 'AFK'
                c.send(data.encode())               
                AFK = True
            pieper.piepertje()
                
                
                
        count = 0
        while afstandmeter.distance > 9:
            if button.switchstate:
                print('send')
                data = 'FLASHBANG'
                c.send(data.encode())
                time.sleep(1)
            time.sleep(0.1)
            count += 1
            if AFK:
                print('send')
                data = 'not AFK'
                c.send(data.encode())
                time.sleep(1)
                AFK = False
        
def receive_data():    
    while True:
        new_data=''
        new_data = c.recv(1024).decode()
        print(len(new_data))
        
        if len(new_data) > 0:
            schuifregister.stop = True
            servo.startservo()
            data = list(map(int, new_data.split(',')))
            
            ledstrip.apa102(5, 6, ledstrip.colors(8, [data[1], data[2], data[3], data[4]],)[:8])
            schuifregister.stop = False
            thread = threading.Thread(target=schuifregister.achievementleds,args=(data[0],))
            thread.start()
            
            
        
        

sendthread = threading.Thread(target=send_data)
receivethread = threading.Thread(target=receive_data)
sendthread.start()
receivethread.start()
sendthread.join()