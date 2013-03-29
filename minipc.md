1. sudo su root

2. 拷贝3个jar到minipc，/home/miniand目录下

3. 更新supervisord.conf配置文件

4. cp -r /etc/supervisor/supervisord.conf.minipc /etc/supervisor/supervisord.conf 

5.浏览器 到minipc 9001，然后stop掉 所有任务
/usr/bin/supervisorctl 
进去了reload


