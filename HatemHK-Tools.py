import os
import sys
import time
os.system('clear')
print ('''
       ,--,                                                       ,--,       ,--.
      ,--.'|               ___                       ____        ,--.'|   ,--/  /|
   ,--,  | :             ,--.'|_                   ,'  , `.   ,--,  | :,---,': / '
,---.'|  : '             |  | :,'               ,-+-,.' _ |,---.'|  : ':   : '/ /
|   | : _' |             :  : ' :            ,-+-. ;   , |||   | : _' ||   '   ,
:   : |.'  |  ,--.--.  .;__,'  /     ,---.  ,--.'|'   |  ||:   : |.'  |'   |  /
|   ' '  ; : /       \ |  |   |     /     \|   |  ,', |  |,|   ' '  ; :|   ;  ;
'   |  .'. |.--.  .-. |:__,'| :    /    /  |   | /  | |--' '   |  .'. |:   '   ;
|   | :  | ' \__\/: . .  '  : |__ .    ' / |   : |  | ,    |   | :  | '|   |    ;
'   : |  : ; ," .--.; |  |  | '.'|'   ;   /|   : |  |/     '   : |  : ;'   : |.  ;
|   | '  ,/ /  /  ,.  |  ;  :    ;'   |  / |   | |`-'      |   | '  ,/ |   | '_\.'
;   : ;--' ;  :   .'   \ |  ,   / |   :    |   ;/          ;   : ;--'  '   : |
|   ,/     |  ,     .-./  ---`-'   \   \  /'---'           |   ,/      ;   |,'
'---'       `--`---'                `----'                 '---'       '---'
''')

time.sleep(1.0)
print ('\033[0;34m1-Metasploit')
print ("2-Sqlmap")
print ("3-Ipgolocation")
print ("4-Nikto")
print ("5-Virus-Hatem")
print ("6-Social Enginnering ToolKit")
print ("7-CamPhish")
print ("8-SMSFlooder")
print ("9-zphisher")
print ("10-Hydra")
print ("11-Nmap")
print ("12-Osint")
print ("13-XeroSploit")
print ("14-FakeCall")
print ("15-Aircrack-ng")
print ("16-Maltego")
#------------------------------------------------------------------------------------------------
metasploit = input ("What Do You Wanna Install : ")
if metasploit == '1' :
 print ("Download Metasploit...........")
 os.system ('git clone https://github.com/rapid7/metasploit-framework.git')
 os.system ('exit')
#------------------------------------------------------------
sqlmap = input ("What Do You Wanna Install : ")
if sqlmap == '2' :
	print ("Download SQLMAP..............")
time.sleep(1.0)
os.system('git clone git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev')
os.system('python sqlmap.py -h')
os.system('python sqlmap.py -hh')
print ("ERROR install the tool")
os.system('exit')
#----------------------------------------------------------
ipgeolocation = input ("What Do You Wanna install : ")
if ipgeolocation == '3' :
	print ("Download IPGEOLOCATION.............")
time.sleep(1.0)
os.system('git clone https://github.com/maldevel/IPGeoLocation')
os.system('pip3 install -r requirements.txt --user')
os.system('apt-get install python3-setuptools')
os.system('easy_install3 pip')
os.system('pip3 install -r requirements.txt')
print ("ERROR install the tool")
os.system('exit')
#-----------------------------------------------------------
nikto = input ("What Do You Wanna Install : ")
if nikto == '4' :
	print ("Download Nikto................")
time.sleep(1.0)
os.system('git clone https://github.com/sullo/nikto')
os.system('cd nikto/program')
os.system('git checkout nikto-2.5.0')
print ("./nikto.pl -h http://www.example.com")
print ("perl nikto.pl -h http://www.example.com")
print ("ERROR install the tool")
os.system('exit')
#-----------------------------------------------------------
virus_hatem = input ("What Do YOU Wanna Install : ")
if virus-hatem == '5' :
	print ("Download VIRUS-HATEM.............")
time.sleep(1.0)
os.system('https://github.com/HatemHK1/Virus-Hatem')
os.system('cd Virus-Hatem')
os.system('chmo +x Virus-Hatem.sh')
os.system('./Virus-Hatem.sh')
print ("ERROR install the tool")
os.system('exit')
#------------------------------------------------------------
social_enginnering_toolKit = input ("What Do You Wanna Intsall : ")
if social_enginnering_toolKit == '6' :
	print ("Download Social Enginnering ToolKit............")
time.sleep(1.0)
os.system('git clone https://github.com/trustedsec/social-engineer-toolkit.git')
os.system('cd setoolkit')
os.system('pip3 install -r requirements.txt')
os.system('python3 setup.py')
print ("ERROR install the tool")
os.system('exit')
#------------------------------------------------------------
camphish = input ("What DO You Wanna Intsall : ")
if camphish == '7' :
	print ("Download camphish............")
time.sleep(1.0)
os.system('git clone https://github.com/techchipnet/CamPhish')
os.system('cd CamPhish')
os.system('bash camphish.sh')
print ("ERROR install the tool")
os.system('exit')
#----------------------------------------------------------
smsflooder = input ("What Do You Wanna Install : ")
if smsflooder == '8' :
	print ("Download sms flooder..........")
time.sleep(1.0)
os.system('git clone https://github.com/youhacker55/SMSFlooder/')
os.system('cd SMSFlooder')
os.system('python3 install.py')
print ("ERROR install the tool")
os.system('exit')
#------------------------------------------------------
zphisher = input ("What Do You Wanna Intsall : ")
if zphisher == '9' :
        print ("Download zphisher............")
time.sleep(1.0)
os.system('git clone --depth=1 https://github.com/htr-tech/zphisher.git')
os.system('cd zphisher')
os.system('bash zphisher.sh')
print ("ERROR install the tool")
os.system('exit')
#--------------------------------------------------
hydra = input ("What Do You Wanna Install : ")
if hydra == '10':
	print ("Download HYDRA...........")
time.sleep(1.0)
os.system('https://github.com/vanhauser-thc/thc-hydra.git')
os.system('./configure')
os.system('make')
os.system('make install')
print ("ERROR install the tool")
os.system('exit')
#--------------------------------------------------
nmap = input ("What Do You Wanna Install : ")
if nmap == '11':
	print ("Download NMAP................")
time.sleep(1.0)
os.system('git clone https://github.com/nmap/nmap.git')
os.system('./configure')
os.system('make')
os.system('make install')
print ("ERROR install the tool")
os.system('exit')
#--------------------------------------------------
osint = input ("What Do You Wanna Intsall : ")
if osint == '12':
	print ("Download OSINT................")
time.sleep(1.0)
os.system('git clone https://github.com/alpkeskin/mosint.git')
print ("ERROR install the tool")
os.system('exit')
#-----------------------------------------------------
xerosploit = input ("What Do You Wanna Install : ")
if xerosploit == '13':
	print ("Download XEROSPLOIT...........")
time.sleep(1.0)
os.system('git clone https://github.com/LionSec/xerosploit')
os.system('cd xerosploit')
os.system('sudo python install.py -y')
os.system('sudo xerosploit')
print ("ERROR install the tool")
os.system('exit')
#---------------------------------------------------------
fakecall = input ("What Do You Wanna Install : ")
if fakecall == '14':
	print ("Download FAKECALL.........")
time.sleep(1.0)
os.system('git clone https://github.com/siputra12/fakecall.git')
print ("ERROR install the tool")
os.system('exit')
#--------------------------------------------------
aircrack_ng = input ("What Do You Wanna install : ")
if aircrack_ng == '15' :
	print ("Download Aircrack-Ng.........")
time.sleep(1.0)
os.system('sudo apt-get install build-essential autoconf automake libtool pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev ethtool shtool rfkill zlib1g-dev libpcap-dev libsqlite3-dev libpcre2-dev libhwloc-dev libcmocka-dev hostapd wpasupplicant tcpdump screen iw usbutils expect')
print ("ERROR install the tool")
os.system('exit')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
maltego = input ("What Do You Wanna install : ")
if Maltego == '16' :
        print ("Download FAKECALL.........")
time.sleep(1.0)
os.system('git clone https://github.com/MaltegoTech/maltego-trx.git')
print ("ERROR install the tool")
os.system('exit')
#---------------------------------------------------------------------------
