#This is a program made for interaction between Windows O.S. and User
from pyttsx3 import speak
import os
import time
import calendar

speak('Hello, I am your complete Windows assisstant')

print()
print()
while True:
	print('Specify your requirements: ', end=" ")
	p = input()
	if (('show' in p) or ('what' in p)) and ('date' in p):
	    os.system('date')

	elif(('open' in p) or ('run' in p) or ('launch' in p)) and (('prompt' in p) or ('cmd') or ('command' in p)):
	    os.system('start cmd.exe')
	    
	elif ('make' in p) and (('folder' in p) or ('directory' in p)):
	    path = input('enter the name of new directory: ')
	    os.mkdir(path)

	elif (('invert' in p) or ('change' in p)) and (('color' in p) or ('colour' in p)):
	    os.system('color f0')

	elif ('run' in p) and ('chrome' in p):
	    os.system('chrome')

	elif('run' in p) or ('open' in p) and ('edge' in p):
	    os.system('start microsoft-edge:')

	elif (('run' in p) or ('execute' in p)) and (('notepad' in p) or ('editor' in p)):
	    os.system('notepad')

	elif ('run' in p) and (('player' in p) or ('media' in p)):
	    os.system('wmplayer')

	elif ('create' in p) and ('partition' in p):
	    print('NOTE: \n****Clean must not be disk on the disk containing the current boot****')
	    p = input('It will create a 300 Mb primary parition, if sure, type yes')
	    if p == 'yes':
	        os.system('diskpart /s partition_script.txt')
	    else:
	        break

	elif (('configure' in p) or ('start' in p)) and ('http' in p):
	    os.system('Powershell.exe notepad C:\Apache24\conf\httpd.conf')

	elif (('run' in p) or ('start' in p)) and ('http' in p):
	    os.system('Powershell.exe C:\Apache24\bin\httpd.exe -k install')
	
	elif('open' in p) or ('run' in p) and ('paint' in p):
	    os.system('start mspaint')

	elif(('run' in p) or ('configure' in p) or ('start' in p)) and ('ssh' in p):
	    os.system('Powershell.exe Start-Service sshd')
	    os.system('Powershell.exe Get-NetFirewallRule -Name *ssh*')

	elif (('change' in p) or ('open' in p)) and (('dir' in p) or ('folder' in p) or ('directory' in p)):
	    path = input('Specify the path of file: ')
	    os.system('start cmd.exe /K cd {}'.format(path))

	elif(('run' in p) or ('start' in p)) and ('python' in p):
	    py = 'cmd.exe /K python'
	    os.system('start {}'.format(py))
	    
	elif(('open' in p) or ('start' in p)) and ('calculator' in p):
	    os.system('calc').time.sleep(2)

	elif(('open' in p) or ('start' in p)) and (('computer' in p) or ('explorer' in p)):
	    os.system('start explorer')

	elif(('open' in p) or ('run' in p)) and ('firefox' in p):
	    os.system('start C:\Program Files\Mozilla Firefox\firefox.exe')

	elif(('start' in p) or ('open' in p) or ('run' in p)) and ('settings' in p):
	    os.system('start ms-settings:')

	elif('clear' in p) or ('delete' in p) and ('cache' in p) or ('temp' in p):
	    os.system('start %temp%')

	elif(('search' in p) or ('open' in p)) and ('google' in p):
	    os.system('start /D https://www.google.com/')
	
	elif(('kill' in p) or ('terminate' in p)) and (('process' in p) or ('program' in p)):
	    os.system('tasklist')
	    kill = int(input('enter the PID of process, from above list: '))
	    os.system('taskkill /PID {} /F'.format(kill))
	
	elif(('open' in p) or ('start' in p)) and ('camera' in p):
	    os.system('start microsoft.windows.camera:')

	elif('ip' in p):
	    os.system('ipconfig | find /N "IPv4"')

	elif ('exit' in p) or ('quit' in p):
	    break

	else:
	    speak("Currently don't support")

