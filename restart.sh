cp -r /home/miniand/minipc/supervisord.conf.minipc1 /etc/supervisor/supervisord.conf 
kill -SIGHUP `cat /var/run/supervisord.pid`
echo "end.....!!!!"
