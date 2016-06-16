# paprikaPI

byobu
sudo apt-get install byobu, byobu-enable
kill window: ctr+a, k

nano
jump to EoF: ctrl + w + v

cpustatus
watch -n 1 ./cpustatus.sh

blikblikblik:
gpio mode 0 out
gpio write 0 1
gpio write 0 0
for (( ; ; )); do gpio -g write 17 1; gpio -g write 17 0;gpio -g write 18 1; gpio -g write 18 0; done


Těploměr:
přidat "dtoverlay=w1-gpio" na konec sudo nano /boot/config.txt, reboot

teploměr id: 28-000006dc502a

sudo modprobe w1-gpio
sudo modprobe w1-therm
roomtemp=$(cat /sys/bus/w1/devices/28-000006dc502a /w1_slave | grep -E -o ".{0,0}t=.{0,5}" | cut -c 3-)
echo "Temperature: $roomtemp"

Temp logging
sudo apt-get install bc



https://www.domorazek.cz/raspberry-pi-jako-ip-teplomer/
