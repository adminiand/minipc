import os
import time

def do():
	print "do restart....."
	os.system("echo restart : %s"%(time.ctime()))
	os.system('kill -1 `cat /var/run/supervisord.pid`')



def main():
	while(True):
		try:
			time.sleep(86400)
			do()
		except Exception, e:
			print e.message
			 

		 
if __name__ == '__main__':
	main()