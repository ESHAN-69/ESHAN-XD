import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':os.system('chmod 777 eshan_64;./eshan_64')
elif bit == '32bit':os.system('chmod 777 eshan_32;./eshan_32)
