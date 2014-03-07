#!/bin/bash
#Autor: Daniel Roth, Domminik Krichbaum
echo -e "\e[01;32mThis script will install the ZEUS-CLI systemwide for all users.\e[00m"
echo -e "\e[01;32mYou need to bee an admin or in sudoers group to finish installation\e[00m"
echo -e "\e[01;32mThis will not install the ZEUS-Server you need to run the server installation manualy\e[00m"
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
chmod +x cli.py
sudo cp -R ../Client /usr/local/bin/Zeus
sudo ln -s /usr/local/bin/Zeus/cli.py /usr/local/bin/zeus
sudo gcc ../Client/filemaker/filemaker.c -o ../Client/filemaker/filemaker
if [ $? != 0 ]; then
{
    echo -e "\e[00;31mERROR: If zeus is already installed please use update_script!\e[00m"
    exit 1
} fi

if [ $? == 0 ]; then
{
    echo "Done!"
    echo "Configurations will be saved in you home-directory"
    echo "Usage:"
    echo "zeus [arg1] [arg2] [arg3] ..."
    exit 0
} fi
