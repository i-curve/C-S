import psutil
import time
from socket import *

def get_cpu(t=1):
	# t1 = psutil.cpu_times()
	# time.sleep(t)
	# t2 = psutil.cpu_times()

	# t1_busy = sum(t1)-t1.idle
	# t2_busy = sum(t2)-t2.idle

	# if t2_busy -t1_busy <0:
	# 	return 0.0
	# cpu_busy = t2_busy - t1_busy
	# all_time = sum(t2)-sum(t1)
	# return str(cpu_busy/all_time)
	return str(psutil.cpu_percent(interval=1))
def get_memory():
	pass
func_dict = {'cpu':get_cpu,'memory':get_memory}

c_server = socket(AF_INET,SOCK_STREAM)#IPV4/TCP
c_server.bind(('',4000))
c_server.listen(5)

print('wait for connection...')
while True:
	client,c_addr = c_server.accept()
	print('Connection from: ',c_addr)
	while True:
		data = client.recv(1024).decode('utf-8')
		# if data == 'cpu':
		# 	buf = get_cpu().encode('utf-8')
		# 	client.send(buf)
		if not data:
			print('Connection close: ',c_addr)
			break
		func = func_dict.get(data)
		if func:
			buf = func_dict[data]().encode('utf-8')
			client.send(buf)
		else:
			buf = '无效的信息获取'
			client.send(buf)
	client.close()
c_server.close()
