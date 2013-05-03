import os
import time

def do():
	print "do restart....."
	os.system("echo restart : %s"%(time.ctime()))
	os.system('kill -1 `cat /var/run/supervisord.pid`')



def main():
	while(True):
		try:
			do()
		except Exception, e:
			print e.message
		finally:
			time.sleep(86400)

		 
if __name__ == '__main__':
	main()