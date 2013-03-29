import os
import time

def do():
	print "do...."
	os.system('./home/miniand/minipc/gitpull.sh')

def main():
	while(True):
		try:
			do()
		except Exception, e:
			print e.message
		finally:
			time.sleep(10)

		 
 

if __name__ == '__main__':
	main()