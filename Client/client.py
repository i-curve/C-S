import tkinter as tk
import socket as sk
import time
class Client:
	def __init__(self):
		self.ip = '127.0.0.1'
		self.port = 4000
		self.data = None 
		self.client = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
		self.root = tk.Tk()
		self.root.geometry('300x300+250+250')
		self.et_ip = tk.Entry(self.root,text='127.0.0.1',width=30)
		self.et_port = tk.Entry(self.root,text=4000,width=6)
		self.ip_label = tk.Label(self.root,text='IP地址',width=10)
		self.port_label = tk.Label(self.root,text='IP端口',width=10)

		self.bt_conn = tk.Button(self.root,text='连接',width=5,height=1,command=self.conn)
		self.bt_close = tk.Button(self.root,text='断开',width=5,height=1,state='disable',command=self.close)
		self.bt_get_info = tk.Button(self.root,text='获取',width=5,height=1,state='disable',command=self.get)
		self.data = tk.Label(self.root,text='信息...')
	def main(self):
		self.et_ip.place(x=3,y=5)
		self.et_port.place(x=3,y=35)
		self.ip_label.place(x=150,y=5)
		self.port_label.place(x=150,y=35)
		self.bt_conn.place(x=3,y=100)
		self.bt_close.place(x=83,y=100)
		self.bt_get_info.place(x=163,y=100)
		self.data.place(x=5,y=150)
		self.root.mainloop()
	def conn(self):
		self.ip = self.et_ip.get()
		self.port = int(self.et_port.get())
		self.data['text'] = '连接中...'
		time.sleep(5)
		try:
			self.client.connect((self.ip,self.port))
		except Exception as e:
			self.data['text'] = '连接失败...'
		else:
			self.bt_close['state']='active'
			self.bt_get_info['state']='active'
			self.data['text'] = '连接成功...'
	def get(self):
		self.client.send('cpu'.encode('utf-8'))
		self.data['text']=self.client.recv(1024).decode('utf-8')
	def close(self):
		self.client.close()
		self.bt_close['state']='disable'
		self.bt_get_info['state']='disable'
client = Client()
client.main()