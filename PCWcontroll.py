#  -*- coding:utf-8 -*-
from pigo import *
import Tkinter
import threading
car = L298N_4(15,16,18,22,40,38,37,36,35,33,32,31)
car.pwmstart()
#hc = HC_SR04(38,40)
def keyboardcontroll(event):
    key_press = event.keysym.lower()
    if key_press == 'w':
        car.goforward()
    elif key_press == 's':
        car.goback()
    elif key_press == 'q':
        car.leftforwardpowerup()
    elif key_press == 'e':
        car.rightforwardpowerup()
    elif key_press == 'a':
        car.leftbackpowerup()
    elif key_press == 'd':
        car.rightbackpowerup()
    elif key_press == 'r':
        car.leftforwardpowerdown()
    elif key_press == 't':
        car.rightforwardpowerdown()
    elif key_press == 'f':
        car.leftbackpowerdown()
    elif key_press == 'g':
        car.rightbackpowerdown()
    elif key_press == 'p':
        car.turn()
    elif key_press == 'space':
        car.stop()
    else:
        pass

#def distancecontroll():
#    while 1:
#        distance = hc.getdistance()
        #TODO
#        dis.set("distance between car an obstacle is %0.2f m" % distance)
tk = Tkinter.Tk()
tk.bind_all('<Key>',keyboardcontroll)
frame=Tkinter.Frame(tk)
frame.grid()
Tkinter.Label(frame,text='hello').pack()
#dis = Tkinter.StringVar()
#t = threading.Thread(target=distancecontroll)
#t.start()
#Create new thread to change distance controll mode
#Tkinter.Label(frame,textvariable=dis).pack()
tk.mainloop()

gpio.cleanup()

