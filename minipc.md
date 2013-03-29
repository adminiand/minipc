1. sudo su root

2. 拷贝3个jar到minipc，/home/miniand目录下

3. 更新supervisord.conf配置文件

4. cp -r /etc/supervisor/supervisord.conf.minipc /etc/supervisor/supervisord.conf 

5.浏览器 到minipc 9001，然后stop掉 所有任务
/usr/bin/supervisorctl 
进去了reload



####github 用户名 adminiand 密码 shang123
https://github.com/adminiand/minipc.git

安装 git
apt-get install git
minipc中 

`sudo su root`

`cd /home/miniand`

`git clone https://github.com/adminiand/minipc.git`

`cd minipc`

`cp post-merge .git/hooks/post-merge`

`chmod a+x .git/hooks/post-merge`

增加crontab
`*/10 * * * * root /home/miniand/minipc/git pull`


