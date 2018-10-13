from . import pigo
from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as gpio

car = pigo.L298N_4(15,16,18,22,40,38,37,36,35,33,32,31)

def index(request):
	car.pwmstart()
	return HttpResponse("<h1>Picar Interface</h1>")

def goforward(request):
	car.goforward()
	return HttpResponse("<h1>goforward</h1>")

def goback(request):
	car.goback()
	return HttpResponse("<h1>goback</h1>")

def turnleft(request):
	car.turnleft()
	return HttpResponse("<h1>Picar Interface</h1>")

def turnright(request):
	car.turnright()
	return HttpResponse("<h1>Picar Interface</h1>")

def leftforwardpowerup(request):
	car.leftforwardpowerup()
	return HttpResponse("<h1>Picar Interface</h1>")

def leftforwardpowerdown(request):
	car.leftforwardpowerdown()
	return HttpResponse("<h1>Picar Interface</h1>")

def rightforwardpowerup(request):
	car.rightforwardpowerup()
	return HttpResponse("<h1>Picar Interface</h1>")

def rightforwardpowerdown(request):
	car.rightforwardpowerdown()
	return HttpResponse("<h1>Picar Interface</h1>")

def rightbackpowerup(request):
	car.rightbackpowerup()
	return HttpResponse("<h1>Picar Interface</h1>")

def	rightbackpowerdown(request):
	car.rightbackpowerdown()
	return HttpResponse("<h1>Picar Interface</h1>")

def leftbackpowerup(request):
	car.leftbackpowerup()
	return HttpResponse("<h1>Picar Interface</h1>")

def leftbackpowerdown(request):
	car.leftbackpowerdown()
	return HttpResponse("<h1>Picar Interface</h1>")

def stop(request):
	car.stop()
	return HttpResponse("<h1>Picar stop</h1>")

def poweroff(request):
	gpio.cleanup()
	return HttpResponse("<h1>Picar poweroff</h1>")

def getspeed(request):
	return HttpResponse("<h3>now speed is:"+car.showspeed()+"</h3>")
