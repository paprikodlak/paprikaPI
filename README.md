# paprikaPI

## git
Download:
```
git clone https://github.com/paprikodlak/paprikaPI
```
Redownload:
```
git reset --hard
git pull
```
## initial_setup.sh
Script to setup RPi, connet to wifi and install usefull programs. Also contains some random knowledge.

## cpustatus
```
watch -n 1 ./cpustatus.sh
```


## blikblikblik
Example for how to blink with LEDs.
```
gpio mode 0 out
gpio write 0 1
gpio write 0 0
```

## Thermometer D18B20
Add line "dtoverlay=w1-gpio" at the end of `nano /boot/config.txt; reboot`

thermometer id: 28-000006dc502a
```
sudo modprobe w1-gpio
sudo modprobe w1-therm
roomtemp=$(cat /sys/bus/w1/devices/28-000006dc502a /w1_slave | grep -E -o ".{0,0}t=.{0,5}" | cut -c 3-)
echo "Temperature: $roomtemp"
```
### temp_logger.py
red led on GPIO17,
white led on GPIO18,
thermometer DS18b20 on GPIO4 (http://arduino-info.wikispaces.com/file/view/DS18B20-Wiring.jpg/543661142/DS18B20-Wiring.jpg)


https://www.domorazek.cz/raspberry-pi-jako-ip-teplomer/

### temp_logger.sh
http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/
To actually use this script, put your Python script where you want and make sure it is executable (e.g. ``chmod +x myservice.py``) and also starts with the line that tells the computer to use the Python interpreter (e.g. ``#!/usr/bin/env python``). Edit the init script accordingly. Copy the init script into ``/etc/init.d`` using e.g. ``sudo cp myservice.sh /etc/init.d``. Make sure the script is executable (chmod again) and make sure that it has UNIX line-endings (dos2unix).

To make the Raspberry Pi use your init script at the right time, one more step is required: running the command ``sudo update-rc.d myservice.sh defaults``. This command adds in symbolic links to the /etc/rc?.d directories so that the init script is run at the default times. you can see these links if you do ``ls -l /etc/rc?.d/*myservice.sh``.

At this point you should be able to start your Python script using the command ``sudo /etc/init.d/myservice.sh start``, check its status with the ``/etc/init.d/myservice.sh`` status argument and stop it with sudo ``/etc/init.d/myservice.sh stop``.

## Displej
pcd8544
(links sorted by relevence)
https://github.com/XavierBerger/pcd8544
http://ikanbilis.com/98.php
https://github.com/rm-hull/pcd8544


## GPIO
RPi GPIO layout rev2: http://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/09/Raspberry-Pi-GPIO-Layout-Revision-2.png

## raspi-wifi-blindscript
(by @shamiao)
A minimalistic script to configure Wi-Fi network on Raspbian system for Raspberry Pi(R) ARM computer. 


## TODO
přepnout teploměr GPIO na pull-up

přidat do scriptů používající GPIO nastavení GPIO na správný mód

skritp, který vygeneruje průběh teploty a uploadne na web/vizualizace naměřené teploty (python? pandas/matplotlib?)

rozchodit displej (vnitřní teplota, vnější teplota z internetu)
