import os
import time
#from subprocess import Popen, PIPE


while True:
    if os.path.exists('/home/dan/Downloads/kali-linux-2016.2-amd64.iso'):
        time.sleep(5)
        os.system('sudo shutdown -P 20')
        break
    time.sleep(10)
