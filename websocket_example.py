#websocket example
import socket
import threading
import time


class TCP_server():
	def __init__(self, host="127.0.0.1", port=6000, code="utf-8", buffer_size=1024, timeout=3):
		try:
	        self.host=host
	        self.port=port
	        self.code=code
	        self.buffer_size=buffer_size
	        self.timeout=timeout
	        self.addr = (self.host, self.port)
	        self.sock = socket(AF_INET, SOCK_STREAM) #建立socket
	        self.sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #讓socket可以reuse
	        self.sock.bind(ADDR) #self.addr
	        print("server start")
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
        while True:
        	conn, addr = self.sock.accept()
        	conn.settimeout(self.timeout)
        	while True:
        		try:
        			msg=conn.recv(self.buffeer_size)
        			msg=msg.decode(self.code)
        			print("recv msg: ",msg)

        		except socket.timeout:
        			print("socket timeout")
        			print("socket close")
        			self.sock.close()
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
		            print("socket close")
        			self.sock.close()
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
	        self.sock = socket(AF_INET, SOCK_STREAM) #建立socket
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
			break
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


     
