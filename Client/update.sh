#!/bin/bash
echo -e "\e[01;32mThis script will update ZEUS to this version A1.3\e[00m"
echo -e "\e[01;32mYou need to bee an admin or in sudoers group to update\e[00m"
echo -e "\e[01;32mThis will not update the ZEUS-Server you need to run the server update manualy\e[00m"
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
if [ ! -d "/usr/local/bin/Zeus" ]; then
{
  echo -e "\e[00;31mUPDATE-ERROR: Zeus is not installed!\e[00m"
  echo -e "\e[00;31mPlease use installation script.\e[00m"
  exit 1
} fi


# Programupdate

#remove old links an files:
sudo rm -R /usr/local/bin/Zeus
sudo rm /usr/local/bin/zeus

chmod +x cli.py
sudo cp -R ../Client /usr/local/bin/Zeus
sudo ln -s /usr/local/bin/Zeus/cli.py /usr/local/bin/zeus
sudo gcc ../Client/filemaker/filemaker.c -o ../Client/filemaker/filemaker

if [ $? == 0 ]; then
{
    echo "Done!"
    exit 0
} fi
