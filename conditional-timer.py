import os
import time
#from subprocess import Popen, PIPE

filename = input('Enter the exact file that is downloading')

while True:
    if os.path.exists('/home/$WHOAMI/Downloads/%s' % filename):
        time.sleep(5)
        os.system('sudo shutdown -P 20')
        break
    time.sleep(5)
time.sleep(5)
