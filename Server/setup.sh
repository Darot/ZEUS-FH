#!/bin/bash
#Autor: Daniel Roth, Domminik Krichbaum
echo -e "\e[01;32mThis script will install the ZEUS-Server systemwide for all users.\e[00m"
echo -e "\e[01;32mYou need to bee an admin or in sudoers group to finish installation\e[00m"
echo -e "\e[01;32mThis will not install the ZEUS-Client you need to run the Client installation manualy\e[00m"
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

# Libraries
sudo apt-get install Python3
sudo apt-get install gcc
sudo apt-get install libpython3.2
sudo apt-get install libpython2.7
sudo apt-get install python-setuptools
sudo apt-get install python-dev
sudo apt-get install libevent-dev
sudo apt-get install libevent-1.4.2
sudo apt-get install libzmq-dev

sudo easy_install pyzmq
sudo easy_install autobahn
sudo easy_install Colorama
sudo easy_install twisted

# Programinstallation
chmod +x WebServer.py
sudo cp -R ../Server /usr/local/bin/Zeus-Server
sudo ln -s /usr/local/bin/Zeus-Server/WebServer.py /usr/local/bin/zeusserver
if [ $? != 0 ]; then
{
    echo -e "\e[00;31mERROR: If zeus is already installed please use update_script!\e[00m"
    exit 1
} fi

if [ $? == 0 ]; then
{
    echo "Done!"
    echo "Usage:"
    echo "zeus-server"
    exit 0
} fi
