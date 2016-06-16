import os
import sched, time
import subprocess
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    t = subprocess.check_output("python ./thermometer_log.py", shell=True)
    if t<22:
        os.system('gpio -g write 17 1 && gpio -g write 18 0')
    elif t<25:
        os.system('gpio -g write 17 0 && gpio -g write 18 0')
    else:
        os.system('gpio -g write 17 0 && gpio -g write 18 1')
    print "%s \n" % t
    sc.enter(60, 1, do_something, (sc,))


s.enter(60, 1, do_something, (s,))
s.run()

