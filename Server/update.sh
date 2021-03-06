#!/bin/bash
#Autor: Daniel Roth, Domminik Krichbaum
echo -e "\e[01;32mThis script will update ZEUS-Server to this version A1.3\e[00m"
echo -e "\e[01;32mYou need to bee an admin or in sudoers group to update\e[00m"
echo -e "\e[01;32mThis will not update the ZEUS-Client you need to run the Client update manualy\e[00m"
echo -e "\e[01;32mOnly run this script if an older version of ZEUS is installed\e[00m"
echo "Do you want to go on? y/n"

function ask {
    echo $1        # add this line
    read -n 1 -r
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
            return 1;
    else
            exit
            echo "Abort.."
    fi
}

ask 

#Check for ZEUS installation:
if [ ! -d "/usr/local/bin/Zeus-Server" ]; then
{
  echo -e "\e[00;31mUPDATE-ERROR: Zeus-Server is not installed!\e[00m"
  echo -e "\e[00;31mPlease use installation script.\e[00m"
  exit 1
} fi

# Programupdate

#remove old links an files:
sudo rm -R /usr/local/bin/Zeus-Server	
sudo rm /usr/local/bin/zeusserver

chmod +x WebServer.py
sudo cp -R ../Server /usr/local/bin/Zeus-Server
sudo ln -s /usr/local/bin/Zeus-Server/WebServer.py /usr/local/bin/zeusserver

if [ $? == 0 ]; then
{
    echo "Done!"
    exit 0
} fi
