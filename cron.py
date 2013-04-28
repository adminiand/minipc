import os
import time

def do():
	print "do....."
	os.system("echo %s"%(time.ctime()))
	os.system('sh /home/miniand/minipc/gitpull.sh')


def main():
	while(True):
		try:
			do()
		except Exception, e:
			print e.message
		finally:
			time.sleep(600)

		 
if __name__ == '__main__':
	main()