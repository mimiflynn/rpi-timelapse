from picamera import PiCamera
from time import sleep
from os import system

camera = PiCamera()

camera.resolution = (3280, 2464)
#camera.resolution = (1024, 768)
#camera.resolution = (2592, 1944)
#camera.resolution = (3280, 2464)
#camera.framerate = 15

def timelapse():
  for i in range(10):
    sleep(5)
    camera.capture('/home/pi/Projects/Photos/images/image{0:04d}.jpg'.format(i))

  #system('convert -delay 10 -loop 0 images/image*.jpg images/animation.gif')
  print('done')
