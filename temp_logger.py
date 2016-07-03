import os
import glob
import time
import datetime
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
os.system('gpio mode 0 out && gpio mode 1 out')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
	

while True:
    temp = read_temp()
    timestamp=datetime.datetime.now()+datetime.timedelta(hours=2)
    retezec_print =str(timestamp) + ' '+ str(temp)
    retezec='\n' + retezec_print
    log = open('teplota.log','a')
    log.write(retezec)
    log.close()
    print(retezec_print)
    if temp<22:
        os.system('gpio write 1 1 && gpio write 0 0')
    elif temp<25:
        os.system('gpio write 1 0 && gpio write 0 0')
    else:
        os.system('gpio write 1 0 && gpio write 0 1')
    time.sleep(300)
