#coding=utf-8
#websocket example
import socket
import threading
import time
import os
import sys
import traceback

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
    def __init__(self, host="127.0.0.1", port=6000, code="utf-8", buffer_size=1024, timeout=3):
        try:
            self.host=host
            self.port=port
            self.code=code
            self.buffer_size=buffer_size
            self.timeout=timeout
            self.addr = (self.host, self.port)
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #建立socket
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


     
