import os
import datetime
from picamera import PiCamera
from time import sleep


def singlephoto():
    print('start taking single photo at {:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now()))
    camera = PiCamera()
    camera.resolution = (3280, 2464)
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Projects/Photos/picam/client/static/images/single.jpg')
    camera.stop_preview()
    camera.close()
    print('done taking single photo at {:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now()))
    os.system('cp picam/client/static/images/single.jpg picam/client/static/images/single-{:%Y-%m-%d_%H-%M-%S}.jpg'.format(datetime.datetime.now()))


def timelapse():
    print('start taking timelapse at {:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now()))
    camera = PiCamera()
    # camera.resolution = (3280, 2464)
    camera.resolution = (1024, 768)
    # camera.resolution = (2592, 1944)
    # camera.resolution = (3280, 2464)
    # camera.framerate = 15

    for i in range(50):
        sleep(5)
        camera.capture('/home/pi/Projects/Photos/picam/client/static/timelapse/image{0:04d}.jpg'.format(i))

    camera.close()
    os.system('tar -zcvf archive/{:%Y-%m-%d_%H-%M-%S}.tar.gz timelapse/'.format(datetime.datetime.now()))
    print('done taking timelapse at {:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now()))


def create_gif():
    print('create gif of timelapse at {:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now()))
    os.system('convert -delay 10 -loop 0 picam/client/static/timelapse/image*.jpg picam/client/static/gifs/animation-{:%Y-%m-%d_%H-%M-%S}.gif'.format(datetime.datetime.now()))
    print('done creating gif of timelapse at {:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now()))
