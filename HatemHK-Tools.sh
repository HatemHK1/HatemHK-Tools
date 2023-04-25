clear
green='\e[1;31m'
green='\e[1;32m'
blue='\e[1;34m'
purple='\e[1;35m'
cyan='\e[1;36m'
white='\e[1;37m'
yellow='\e[1;33m'

figlet "HatemHK"
echo ''
echo -e $yellow '~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "1-Metasploit"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "2-Sqlmap"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "3-Ipgolocation"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "4-Nikto"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "5-Virus-Hatem"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "6-Social Enginnering ToolKit"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "7-CamPhish"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "8-SMSFlooder"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "9-zphisher"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "10-Hydra"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "11-Nmap"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "12-Osint"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "13-XeroSploit"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "14-FakeCall"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'
echo -e $yellow "15-Aircrack-ng"
echo ' ~_~_~_~_~_~_~_~_~_~_~_~_~_~'

read -p " Enter Your Name : " user
echo "Wellcome To My Tool "$user
#-------------------------------------
read -p "What Do You Install : " tool
if [ $tool == 1 ];then
	echo "[✔]Download Metasploit..........."
git clone https://github.com/rapid7/metasploit-framework.git
else
	echo "Error "$user
fi
#----------------------------------------------------------------
if [ $tool == 2 ];then
echo "[✔]Download Sqlmap..........."
git clone https://github.com/sqlmapproject/sqlmap.git
else
        echo "Error "$user
exit
fi
#--------------------------------------------------------
if [ $tool == 3 ];then
echo "[✔]Download Ipgolocation............"
git clone https://github.com/maldevel/IPGeoLocation
else
        echo "Error "$user
exit
fi
#---------------------------------------------------------
if [ $tool == 4 ];then
echo "[✔]Download Nikto............"
git clone https://github.com/sullo/nikto
cd nikto/program
git checkout nikto-2.5.0
echo "./nikto.pl -h http://www.example.com"
echo "perl nikto.pl -h http://www.example.com"
else
        echo "Error "$user
fi
#---------------------------------------------------------
if [ $tool == 5 ];then
echo "[✔]Download Virus-Hatem.............."
git clone https://github.com/HatemHK1/Virus-Hatem
else
        echo "Error "$user
fi
#---------------------------------------------------------
if [ $tool == 6 ];then
echo "[✔]Download Social Enginnering ToolKit.............."
git clone https://github.com/trustedsec/social-engineer-toolkit.git
cd setoolkit
pip3 install -r requirements.txt
python3 setup.py
else
        echo "Error "$user
fi
#---------------------------------------------------------
if [ $tool == 7 ];then
echo "[✔]Download camphish.............."
git clone https://github.com/techchipnet/CamPhish
else
        echo "Error "$user
fi
#---------------------------------------------------------
if [ $tool == 8 ];then
echo "[✔]Download sms flooder.............."
git clone https://github.com/youhacker55/SMSFlooder
else
        echo "Error "$user
fi
#---------------------------------------------------------
if [ $tool == 9 ];then
echo "[✔]Download zphisher.............."
git clone --depth=1 https://github.com/htr-tech/zphisher.git
else
        echo "Error "$user
fi
#---------------------------------------------------------
if [ $tool == 10 ];then
echo "[✔]Download HYDRA.............."
git clone https://github.com/vanhauser-thc/thc-hydra.git
./configure
make
make install
else
        echo "Error "$user
fi
#---------------------------------------------------------
if [ $tool == 11 ];then
echo "[✔]Download NMAP.............."
git clone https://github.com/nmap/nmap.git
else
        echo "Error "$user
fi
#---------------------------------------------------------
if [ $tool == 12 ];then
echo "[✔]Download OSINT.............."
git clone https://github.com/alpkeskin/mosint.git
else
        echo "Error "$user
fi
#---------------------------------------------------------
if [ $tool == 13 ];then
echo "[✔]Download XEROSPLOIT.............."
git clone https://github.com/LionSec/xerosploit
else
        echo "Error "$user
fi
#---------------------------------------------------------
if [ $tool == 14 ];then
echo "[✔]Download FAKECALL.............."
git clone https://github.com/siputra12/fakecall.git
else
        echo "Error "$user
fi
#------------------------------------------------------
if [ $tool == 15 ];then
echo "[✔]Download Aircrack-Ng.............."
sudo apt-get install build-essential autoconf automake libtool pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev ethtool shtool rfkill zlib pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev ethtool shtool rfkill zlib1g-dev libpcap-dev libsqlite3-dev libpcre2-dev libhwloc-dev libcmocka-dev hostapd wpasupplicant tcpdump screen iw usbutils expect
else
        echo "Error "$user
fi
#------------------------------------------------------
