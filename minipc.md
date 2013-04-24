####github
* 用户名 adminiand 
* 密码 *shang123*
* 地址 https://github.com/adminiand/minipc.git

#######minipc中安装 git： `apt-get install git`
  

`sudo su root`

`cd /home/miniand`

`git clone https://github.com/adminiand/minipc.git`

`cd minipc`
`chmod a+x gitpull.sh`


`cp post-merge .git/hooks/post-merge`

`chmod a+x .git/hooks/post-merge`

第一次最后运行下：

`chmod restart.sh`

`./restart.sh`

#####因lubuntu cron有问题，更新任务已经靠cron.py 循环启动gitpull！

~~增加crontab -e
`*/10 * * * * root /home/miniand/minipc/gitpull.sh`~~

###目前现有minipc
安装git，
sudo su root后，在/home/miniand 下 

`git clone https://github.com/adminiand/minipc.git`

`cd minipc`

`cp post-merge .git/hooks/post-merge`

`chmod a+x .git/hooks/post-merge`

`chmod a+x gitpull.sh`

`chmod a+x restart.sh`

`./restart.sh`

#####因lubuntu cron有问题，更新任务已经靠cron.py 循环启动gitpull！

~~增加crontab -e
`*/10 * * * * root /home/miniand/minipc/gitpull.sh`~~


####restart.sh  
1. 更新supervisord.conf配置文件

 cp -r /etc/supervisor/supervisord.conf.minipc /etc/supervisor/supervisord.conf 

2. kill -1 `cat /var/run/supervisord.pid`

~~crontab -e
*/10 * * * * root /home/miniand/minipc/gitpull.sh~~


###git项目有问题的：
`ssh miniand@minipcIp` ssh到minipc
`sudo su root ` 切换到root
`rm -rf minipc` 删除minipc目录

然后重一次以下内容：

`git clone https://github.com/adminiand/minipc.git`

`cd minipc`

`cp post-merge .git/hooks/post-merge`

`chmod a+x .git/hooks/post-merge`

`chmod a+x gitpull.sh`

`chmod a+x restart.sh`

`./restart.sh`

最后登陆http://minipcIp:9001 查看


