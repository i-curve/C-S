import psutil
import time
from socket import *

def get_cpu(t=1):
	s = 'cpu使用率为:\n'+str(psutil.cpu_percent(interval=0.5))+'%\n'
	return s
def get_memory():
	mem = psutil.virtual_memory()
	s = '内存使用情况为:\n'+\
		'剩余内存为: '+str(mem.free/1024)+\
		'M\n总共内存为:'+str(mem.total/1024)+'M\n'
	return s
	
def get_disk():
	disk = psutil.disk_usage('/')
	return str(disk.free)+'/'+str(disk.total)
def get_all():
	s = get_cpu()+get_memory()
	return s
func_dict = {'cpu':get_cpu,'memory':get_memory,'disk':get_disk,'all':get_all}

c_server = socket(AF_INET,SOCK_STREAM)#IPV4/TCP
c_server.bind(('',4000))
c_server.listen(5)

print('wait for connection...')
while True:
	client,c_addr = c_server.accept()
	print('Connection from: ',c_addr)
	while True:
		data = client.recv(1024).decode('utf-8')
		if not data:
			print('Connection close: ',c_addr)
			break
		func = func_dict.get(data)
		if func:
			buf = func_dict[data]().encode('utf-8')
			client.send(buf)
		else:
			buf = '无效的信息获取'.encode('utf-8')
			client.send(buf)
	client.close()
c_server.close()
