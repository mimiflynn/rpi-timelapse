import os
import datetime

from flask import Flask, render_template, send_from_directory
from picamera import PiCamera
from time import sleep

def singlephoto():
  camera = PiCamera()
  camera.resolution = (3280, 2464)
  camera.start_preview()
  sleep(2)
  camera.capture('/home/pi/Projects/Photos/images/single.jpg')
  camera.stop_preview()
  camera.close()
  print('done taking single photo')
  os.system('cp images/single.jpg images/single-{:%Y-%m-%d %H:%M:%S}.jpg'.format(datetime.datetime.now()))


def timelapse():
  camera = PiCamera()
  #camera.resolution = (3280, 2464)
  camera.resolution = (1024, 768)
  #camera.resolution = (2592, 1944)
  #camera.resolution = (3280, 2464)
  #camera.framerate = 15

  for i in range(50):
    sleep(5)
    camera.capture('/home/pi/Projects/Photos/images/image{0:04d}.jpg'.format(i))

  camera.close()
  os.system('tar -zcvf {:%Y-%m-%d %H:%M:%S}.tar.gz images/'.format(datetime.datetime.now()))
  #os.system('convert -delay 10 -loop 0 images/image*.jpg images/animation.gif')
  print('done taking timelapse')

def make_tree(path):
  tree = dict(name=os.path.basename(path), children=[])
  try: lst = os.listdir(path)
  except OSError:
    pass #ignore errors
  else:
    for name in lst:
      fn = os.path.join(path, name)
      if os.path.isdir(fn):
        tree['children'].append(make_tree(fn))
      else:
        tree['children'].append(dict(name=name))
  return tree

app = Flask(__name__)

@app.route('/')
def index():
  singlephoto()
  return render_template('index.html')

@app.route('/timelapse')
def photos():
  timelapse()
  path = '/home/pi/Projects/Photos/images'
  return render_template('photos.html', tree=make_tree(path))

@app.route('/view')
def view():
  path = '/home/pi/Projects/Photos/images'
  return render_template('photos.html', tree=make_tree(path))

@app.route('/images/<path:path>')
def images(path):
    return send_from_directory('images', path)

@app.route('/styles/<path:path>')
def styles(path):
    return send_from_directory('styles', path)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
