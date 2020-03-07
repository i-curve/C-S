获取服务器信息

架构：

cpu信息：pip install psutil

​	User_time: 用户进程时间百分比

​	System_time: 系统进程时间百分比

​	Wait IO: IO等待时间

​	idle: cpu空闲时间百分比

​	psutil.cpu_time()

​	psutil.cpu_percent()

内存信息

​	psutil.virtual_memory()

磁盘信息

​	psutil.disk_usage('/')

网络信息

进程信息