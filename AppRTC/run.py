
import subprocess


server = '.\\Google_Cloud\\google-cloud-sdk\\bin\\dev_appserver.py'

appEngine = './app_engine'

#Use ip adress if you want to access the signalling server 
#from another pc connected to the same network
#You will need to change the `roomServer` variable inside AppRTC/js/appwindow.js 
#to have the value of the ip address eg.: `var roomServer = 'http://192.168.1.1:8080'`
#Example for the ipAddress variable - ipAddress = '' or ipAddress = '192.168.1.1'
ipAddress = ''

if ipAddress is not '':
  ipAddress = '--host='+ipAddress
  command = [server, appEngine, ipAddress]
else:
  command = [server, appEngine]
print(command)

subprocess.call(command, shell=True)
