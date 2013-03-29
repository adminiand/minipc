cp -r /home/miniand/minipc/supervisord.conf.minipc1 /etc/supervisor/supervisord.conf 
sleep 2
kill -1 `cat /var/run/supervisord.pid`
echo "end.....!!!!"
