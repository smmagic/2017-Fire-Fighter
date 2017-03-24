from subsystems import Drivetrain
#from subsystems import SensorStick    # SEAS Innovation Challenge subsystems
from time import sleep

import multiprocessing

def worker():
    print "Robot in running"
    return

p = multiprocessing.Process(target=worker)
p.start()
p.join()

# H-drive drivetrain
drivetrain = Drivetrain()
# sensor_stick = SensorStick()
#status_light = StatusLight()

#testsystem = Test()

while (True):
    #status_light.check_flame()
    #sensor_stick.check_actuation()
    drivetrain.arcade_drive(1.0, 0.0, 0.0)
#    testsystem.move()
    sleep(.1)
