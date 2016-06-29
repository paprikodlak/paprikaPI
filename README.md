# paprikaPI

##git(?)
```
git clone https://github.com/paprikodlak/paprikaPI

git reset --hard
git pull
```
##initial_setup.sh
Script to setup RPi, connet to wifi and install usefull programs. Also contains some random knowledge.

##cpustatus
```
watch -n 1 ./cpustatus.sh
```


##blikblikblik
Example for how to blink with LEDs.
```
gpio mode 0 out
gpio write 0 1
gpio write 0 0

for (( ; ; )); do gpio -g write 17 1; gpio -g write 17 0;gpio -g write 18 1; gpio -g write 18 0; done
```

##Thermometer D18B20
Add line "dtoverlay=w1-gpio" at the end of `nano /boot/config.txt; reboot`

thermometer id: 28-000006dc502a
```
sudo modprobe w1-gpio
sudo modprobe w1-therm
roomtemp=$(cat /sys/bus/w1/devices/28-000006dc502a /w1_slave | grep -E -o ".{0,0}t=.{0,5}" | cut -c 3-)
echo "Temperature: $roomtemp"
```
###temp_logger.py
red led on GPIO17,
white led on GPIO18,
thermometer DS18b20 on GPIO4 (http://arduino-info.wikispaces.com/file/view/DS18B20-Wiring.jpg/543661142/DS18B20-Wiring.jpg)


https://www.domorazek.cz/raspberry-pi-jako-ip-teplomer/

##Displej
pcd8544
(links sorted by relevence)
https://github.com/XavierBerger/pcd8544
http://ikanbilis.com/98.php
https://github.com/rm-hull/pcd8544


##GPIO
RPi GPIO layout rev2: http://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/09/Raspberry-Pi-GPIO-Layout-Revision-2.png

##raspi-wifi-blindscript
(by @shamiao)
A minimalistic script to configure Wi-Fi network on Raspbian system for Raspberry Pi(R) ARM computer. 


##TODO
přepnout teploměr GPIO na pull-up

přidat do scriptů používající GPIO nastavení GPIO na správný mód

vizualizace naměřené teploty (python? pandas/matplotlib?)

rozchodit displej (vnitřní teplota, vnější teplota z internetu)
