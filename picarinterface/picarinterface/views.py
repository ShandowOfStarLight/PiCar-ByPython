from pigo import *
from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as gpio
def index(request):
	car = L298N_4(15,16,18,22,40,38,37,36,35,33,32,31)
	car.pwmstart()
	return HttpResponse("<h1>Picar Interface</h1>")

def goforward():
	car.goforward()

def goback():
	car.goback()

def turnleft():
	car.turnleft()

def turnright():
	car.turnright()

def leftforwardpowerup():
	car.leftforwardpowerup()

def leftforwardpowerdown():
	car.leftforwardpowerdown()

def rightforwardpowerup():
	car.rightforwardpowerup()

def rightforwardpowerdown():
	car.rightforwardpowerdown()

def rightbackpowerup():
	car.rightbackpowerup()

def	rightbackpowerdown():
	car.rightbackpowerdown()

def leftbackpowerup():
	car.leftbackpowerup()

def leftbackpowerdown():
	car.leftbackpowerdown()

def stop():
	car.stop()

def poweroff():
	gpio.cleanup()

def getspeed():
	lf, lb, rf, rb = car.showspeed()
	return HttpResponse("<h3>now speed is: {0},{1},{2},{3}</h3>".format(lf,lb,rf,rb))