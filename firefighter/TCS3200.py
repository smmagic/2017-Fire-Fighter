from nanpy import ArduinoApi, SerialManager


#Brandon Waller
#GW Robotics
#Python code for TCS3200 Color Sensor

class ColorSensor(object):
    a = ArduinoApi()
    def __init__(self, s0, s1, s2, s3, sensorOut):
        self.s0 = s0
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.sensorOut = sensorOut
        a.pinMode(s0, a.OUTPUT)
        a.pinMode(s1, a.OUTPUT)
        a.pinMode(s2, a.OUTPUT)
        a.pinMode(s3, a.OUTPUT)
        a.pinMode(sensorOut, a.INPUT)
        a.digitalWrite(s0, a.HIGH)
        a.digitalWrite(s1, a.LOW)

    def get_red():
        #Return 0- ~255 red value
        a.digitalWrite(s2, a.HIGH)
        a.digitalWrite(s3, a.LOW)

        return a.pulseIn(sensorOut, a.LOW)
    
    def get_green():
        #return 0- ~255 green value
        a.digitalWrite(s2, a.HIGH)
        a.digitalWrite(s3, a.HIGH)
        
        return a.pulseIn(sensorOut, a.LOW)

    def get_blue():
        #return 0- ~255 blue value 
        a.digitalWrite(s2, a.LOW)
        a.digitalWrite(s3, a.HIGH)
        
        return a.pulseIn(sensorOut, a.LOW)

