import os
import time

def do():
	os.system('./home/miniand/gitpull.sh')

def main():
	while(True):
		do()
		time.sleep(10)

if __name__ == '__main__':
	main()