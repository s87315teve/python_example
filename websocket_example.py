#coding=utf-8
#websocket example
import socket
import threading
import time
import os
import sys
import traceback
import argparse

class TCP_server():
    def __init__(self, host="127.0.0.1", port=6000, code="utf-8", buffer_size=1024, timeout=None):
        try:
            self.host=host
            self.port=port
            self.code=code
            self.buffer_size=buffer_size
            self.timeout=timeout
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #建立socket
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)

    def start(self):
        try:

            self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #讓socket可以reuse
            bind_addr=(self.host, self.port)
            self.sock.bind(bind_addr) #self.addr
            self.sock.listen()
            print("server start")
            print("server is listening to {}".format(bind_addr))
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)
            print("server failed to start")
        while True:
            conn, addr = self.sock.accept()
            print("{} connected to server".format(addr))
            if self.timeout!=None:
                conn.settimeout(self.timeout)
            while True:
                try:
                    msg=conn.recv(self.buffer_size)
                    if not msg:
                        print("client is gone ")
                        print("connection closed")
                        conn.close()
                        print("sleep 1s and restart socket")
                        time.sleep(1)
                        break
                    msg=msg.decode(self.code)
                    print("recv msg: ",msg)

                except socket.timeout:
                    print("socket timeout")
                    print("connection closed")
                    conn.close()
                    print("sleep 1s and restart socket")
                    time.sleep(1)
                    break
                except Exception as e:
                    error_class = e.__class__.__name__ #取得錯誤類型
                    detail = e.args[0] #取得詳細內容
                    cl, exc, tb = sys.exc_info() #取得Call Stack
                    lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
                    fileName = lastCallStack[0] #取得發生的檔案名稱
                    lineNum = lastCallStack[1] #取得發生的行號
                    funcName = lastCallStack[2] #取得發生的函數名稱
                    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
                    print(errMsg)
                    print("connection closed")
                    conn.close()
                    print("sleep 1s and restart socket")
                    time.sleep(1)
                    break
class TCP_client():
    def __init__(self, host="127.0.0.1", port=6000, code="utf-8", buffer_size=1024):
        try:
            self.host=host
            self.port=port
            self.code=code
            self.buffer_size=buffer_size
            self.timeout=timeout
            self.addr = (self.host, self.port)
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #建立TCP socket
            self.sock.connect(self.addr) #self.addr
            print("connected to server")
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)
            print("connection failed ")
    def send_msg(self, msg=""):
        try:
            msg=msg.encode(self.code)
            self.sock.send(msg)
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)


class UDP_server():
    def __init__(self, host="127.0.0.1", port=6000, code="utf-8", buffer_size=1024):
        try:
            self.host=host
            self.port=port
            self.code=code
            self.buffer_size=buffer_size
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #建立UDP socket
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)

    def start(self):
        try:

            self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #讓socket可以reuse
            bind_addr=(self.host, self.port)
            self.sock.bind(bind_addr) #self.addr
            print("server start")
            print("server is listening to {}".format(bind_addr))
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)
            print("server failed to start")
        while True:
            while True:
                try:
                    msg, addr=self.sock.recvfrom(self.buffer_size)
                    if not msg:
                        print("no msg from {}",addr)
                        break
                    msg=msg.decode(self.code)
                    print("recv from {} : {}".format(addr,msg))
                except Exception as e:
                    error_class = e.__class__.__name__ #取得錯誤類型
                    detail = e.args[0] #取得詳細內容
                    cl, exc, tb = sys.exc_info() #取得Call Stack
                    lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
                    fileName = lastCallStack[0] #取得發生的檔案名稱
                    lineNum = lastCallStack[1] #取得發生的行號
                    funcName = lastCallStack[2] #取得發生的函數名稱
                    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
                    print(errMsg)
                    print("sleep 1s and restart socket")
                    time.sleep(1)
                    break
class UDP_client():
    def __init__(self, host="127.0.0.1", port=6000, code="utf-8", buffer_size=1024):
        try:
            self.host=host
            self.port=port
            self.code=code
            self.buffer_size=buffer_size
            self.addr = (self.host, self.port)
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #建立UDP socket
            #self.sock.connect(self.addr) #self.addr
            print("connected to server")
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)
            print("connection failed ")
    def send_msg(self, msg=""):
        try:
            msg=msg.encode(self.code)
            self.sock.sendto(msg,self.addr)
        except Exception as e:
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱
            errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
            print(errMsg)
def run(opt):
    if opt.mode=="TCP_server":
        server=TCP_server(host=opt.host, port=opt.port, code=opt.code, buffer_size=opt.buffer, timeout=opt.timeout)
        server.start()
    elif opt.mode=="TCP_client":
        client=TCP_client(host=opt.host, port=opt.port, code=opt.code, buffer_size=opt.buffer)
        client.start()
    elif opt.mode=="UDP_server":
        server=UDP_server(host=opt.host, port=opt.port, code=opt.code, buffer_size=opt.buffer)
        server.start()
    elif opt.mode=="UDP_client":
        client=UDP_client(host=opt.host, port=opt.port, code=opt.code, buffer_size=opt.buffer)
        client.start()
    else:
        print("argument illegal, please restart this program")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", "-m", type=str, default=None, help="select mode")
    parser.add_argument("--host", type=str,  default="127.0.0.1", help="set host IP")
    parser.add_argument("--port", "-p", type=int, default=6000, help="set host port")
    parser.add_argument("--code", "-c", type=str, default="utf-8", help="set how to encode/decode")
    parser.add_argument("--buffer", "-b", type=int, default=1024, help="setbuffer size")
    parser.add_argument("--timeout", "-t", type=int, default=None, help="set timeout")
    opt = parser.parse_args()
    print("your option:")
    print(opt)
    run(opt)
    


