#
#
#
#

sudo raspi-config

echo -n
echo -n "WiFi setup:"
sudo chmod +x raspi-wifi-shellscript.sh
sudo ./raspi-wifi-shellscript.sh

#byobu hotkeys:
#kill window: ctr+a, k
echo -n
echo -n "Installing byobu"
sudo apt-get -y install byobu
sudo byobu-enable



#knowledge base:
#
#Nano:
#jump to end of file:  ctrl + w + v
