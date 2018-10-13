#  -*- coding:utf-8 -*-
"""
HC-SR04
echo = 40
tri = 30

L298N
ena = 3
enb = 5
in1 = 11,
in2 = 8,
in3 = 10,
in4 =12
"""
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
class L298N_2(object):
    def __init__(self,ena,enb,in1,in2,in3,in4):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        gpio.setup(in1, gpio.OUT,initial=gpio.LOW)
        gpio.setup(in2, gpio.OUT,initial=gpio.LOW)
        gpio.setup(in3, gpio.OUT,initial=gpio.LOW)
        gpio.setup(in4, gpio.OUT,initial=gpio.LOW)
        gpio.setup(ena, gpio.OUT,initial=gpio.LOW)
        gpio.setup(enb, gpio.OUT,initial=gpio.LOW)
        self.pwm_ena=gpio.PWM(ena,50)
        self.pwm_enb=gpio.PWM(enb,50)
        self.speedleft = 50
        self.speedright = 50    
    def pwmstart(self):
        self.pwm_ena.start(self.speedleft)
        self.pwm_enb.start(self.speedright)
    def do_changespeed(self):
        self.pwm_ena.ChangeDutyCycle(self.speedleft)
        self.pwm_enb.ChangeDutyCycle(self.speedright)
    def changespeed(self, speedleft, speedright):
        self.pwm_ena.ChangeDutyCycle(speedleft)
        self.pwm_enb.ChangeDutyCycle(speedright)   
    def goforward(self):
        gpio.output(self.in1, gpio.HIGH)
        gpio.output(self.in2, gpio.LOW)
        gpio.output(self.in3, gpio.LOW)
        gpio.output(self.in4, gpio.HIGH)
    def goback(self):
        gpio.output(self.in1, gpio.LOW)
        gpio.output(self.in2, gpio.HIGH)
        gpio.output(self.in3, gpio.HIGH)
        gpio.output(self.in4, gpio.LOW)
    def stop(self):
        gpio.output(self.in1, gpio.LOW)
        gpio.output(self.in2, gpio.LOW)
        gpio.output(self.in3, gpio.LOW)
        gpio.output(self.in4, gpio.LOW)
    def leftpowerup(self, pu=5):
        if self.speedleft < 100:
            self.speedleft = self.speedleft + pu
            self.do_changespeed()
    def rightpowerup(self, pu=5):
        if self.speedright < 100:
            self.speedright = self.speedright + pu
            self.do_changespeed()    
    def leftpowerdown(self, pu=5):
        if self.speedleft > 0:
            self.speedleft = self.speedleft - pu
            self.do_changespeed()
    def rightpowerdown(self, pu=5):
        if self.speedleft > 0:
            self.speedright = self.speedright - pu
            self.do_changespeed()

class L298N_4(object):
    def __init__(self,ena,enb,enc,end,in1,in2,in3,in4,in5,in6,in7,in8):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.in5 = in5
        self.in6 = in6
        self.in7 = in7
        self.in8 = in8
        gpio.setup(in1, gpio.OUT,initial=gpio.LOW)
        gpio.setup(in2, gpio.OUT,initial=gpio.LOW)
        gpio.setup(in3, gpio.OUT,initial=gpio.LOW)
        gpio.setup(in4, gpio.OUT,initial=gpio.LOW)
        gpio.setup(in5, gpio.OUT,initial=gpio.LOW)
        gpio.setup(in6, gpio.OUT,initial=gpio.LOW)
        gpio.setup(in7, gpio.OUT,initial=gpio.LOW)
        gpio.setup(in8, gpio.OUT,initial=gpio.LOW)
        gpio.setup(ena, gpio.OUT,initial=gpio.LOW)
        gpio.setup(enb, gpio.OUT,initial=gpio.LOW)
        gpio.setup(enc, gpio.OUT,initial=gpio.LOW)
        gpio.setup(end, gpio.OUT,initial=gpio.LOW)
        self.pwm_ena=gpio.PWM(ena,50)
        self.pwm_enb=gpio.PWM(enb,50)
        self.pwm_enc=gpio.PWM(enc,50)
        self.pwm_end=gpio.PWM(end,50)
        self.speedforwardleft = 50
        self.speedbackleft = 50
        self.speedforwardright = 50
        self.speedbackright = 50
    def pwmstart(self):
        self.pwm_ena.start(self.speedforwardleft)
        self.pwm_enb.start(self.speedbackleft)
        self.pwm_enc.start(self.speedforwardright)
        self.pwm_end.start(self.speedbackright)
    def do_changespeed(self):
        self.pwm_ena.ChangeDutyCycle(self.speedforwardleft)
        self.pwm_enb.ChangeDutyCycle(self.speedbackleft)
        self.pwm_enc.ChangeDutyCycle(self.speedforwardright)
        self.pwm_end.ChangeDutyCycle(self.speedbackright)
    def changespeed(self, speedforwardleft, speedbackleft, speedforwardright, speedbackright):
        self.pwm_ena.ChangeDutyCycle(speedforwardleft)
        self.pwm_enb.ChangeDutyCycle(speedbackleft)
        self.pwm_enc.ChangeDutyCycle(speedforwardright)
        self.pwm_end.ChangeDutyCycle(speedbackright) 
    def goforward(self):
        gpio.output(self.in1, gpio.HIGH)
        gpio.output(self.in2, gpio.LOW)
        gpio.output(self.in3, gpio.LOW)
        gpio.output(self.in4, gpio.HIGH)
        gpio.output(self.in5, gpio.HIGH)
        gpio.output(self.in6, gpio.LOW)
        gpio.output(self.in7, gpio.LOW)
        gpio.output(self.in8, gpio.HIGH)
    def goback(self):
        gpio.output(self.in1, gpio.LOW)
        gpio.output(self.in2, gpio.HIGH)
        gpio.output(self.in3, gpio.HIGH)
        gpio.output(self.in4, gpio.LOW)
        gpio.output(self.in5, gpio.LOW)
        gpio.output(self.in6, gpio.HIGH)
        gpio.output(self.in7, gpio.HIGH)
        gpio.output(self.in8, gpio.LOW)
    def turnleft(self):
        gpio.output(self.in1, gpio.HIGH)
        gpio.output(self.in2, gpio.LOW)
        gpio.output(self.in3, gpio.LOW)
        gpio.output(self.in4, gpio.HIGH)
        gpio.output(self.in5, gpio.LOW)
        gpio.output(self.in6, gpio.HIGH)
        gpio.output(self.in7, gpio.HIGH)
        gpio.output(self.in8, gpio.LOW)
    def turnright(self):
        gpio.output(self.in1, gpio.LOW)
        gpio.output(self.in2, gpio.HIGH)
        gpio.output(self.in3, gpio.HIGH)
        gpio.output(self.in4, gpio.LOW)
        gpio.output(self.in5, gpio.HIGH)
        gpio.output(self.in6, gpio.LOW)
        gpio.output(self.in7, gpio.LOW)
        gpio.output(self.in8, gpio.HIGH)        
    def stop(self):
        gpio.output(self.in1, gpio.LOW)
        gpio.output(self.in2, gpio.LOW)
        gpio.output(self.in3, gpio.LOW)
        gpio.output(self.in4, gpio.LOW)
        gpio.output(self.in5, gpio.LOW)
        gpio.output(self.in6, gpio.LOW)
        gpio.output(self.in7, gpio.LOW)
        gpio.output(self.in8, gpio.LOW)
    def showspeed(self):
    #    print ("{0}  {1}  {2}  {3} \n").format(self.speedforwardleft,self.speedbackleft,self.speedforwardright,self.speedbackright)
    return self.speedforwardleft,self.speedbackleft,self.speedforwardright,self.speedbackright
    def leftforwardpowerup(self, pu=5):
        if self.speedforwardleft < 100:
            self.speedforwardleft = self.speedforwardleft + pu
            if self.speedforwardleft > 100.0:
                self.speedforwardleft=100.0
            self.do_changespeed()
        self.showspeed()
    def leftbackpowerup(self, pu=5):
        if self.speedbackleft < 100:
            self.speedbackleft = self.speedbackleft + pu
            if self.speedbackleft > 100.0:
                self.speedbackleft=100.0
            self.do_changespeed()
            self.showspeed()
    def rightforwardpowerup(self, pu=5):
        if self.speedforwardright < 100:
            self.speedforwardright = self.speedforwardright + pu
            if self.speedforwardright > 100.0:
                self.speedforwardright=100.0
            self.do_changespeed()
            self.showspeed()
    def rightbackpowerup(self, pu=5):
        if self.speedbackright < 100:
            self.speedbackright = self.speedbackright + pu
            if self.speedbackright > 100.0:
                self.speedbackright=100.0
            self.do_changespeed()
            self.showspeed()
    def leftforwardpowerdown(self, pu=5):
        if self.speedforwardleft > 0:
            self.speedforwardleft = self.speedforwardleft - pu
            if self.speedforwardleft < 0:
                self.speedforwardleft=0
            self.do_changespeed()
            self.showspeed()
    def leftbackpowerdown(self, pu=5):
        if self.speedbackleft > 0:
            self.speedbackleft = self.speedbackleft - pu
            if self.speedbackleft < 0:
                self.speedbackleft=0
            self.do_changespeed()
            self.showspeed()
    def rightforwardpowerdown(self, pu=5):
        if self.speedforwardleft > 0:
            self.speedforwardright = self.speedforwardright - pu
            if self.speedforwardright < 0:
                self.speedforwardright=0
            self.do_changespeed()
            self.showspeed()
    def rightbackpowerdown(self, pu=5):
        if self.speedbackleft > 0:
            self.speedbackright = self.speedbackright - pu
            if self.speedbackright < 0:
                self.speedbackright=0
            self.do_changespeed()
            self.showspeed()

class HC_SR04(object):
    def __init__(self, tri, echo):
        self.tri = tri
        self.echo = echo
        self.start = 0.0
        gpio.setup(tri, gpio.OUT, initial = gpio.LOW)
        gpio.setup(echo, gpio.IN)
    def getdistance(self):
        gpio.output(self.tri,gpio.HIGH)
        time.sleep(0.055)
        gpio.output(self.tri,gpio.LOW)
        while gpio.input(self.echo) == 0:
            pass
        self.start = time.time()
        while gpio.input(self.echo) == 1:
            pass
        return (time.time() - self.start) * 170

