from flask import Flask, render_template, send_from_directory
from os import system
from picamera import PiCamera
from time import sleep

def timelapse():
  camera = PiCamera()
  camera.resolution = (3280, 2464)
  #camera.resolution = (1024, 768)
  #camera.resolution = (2592, 1944)
  #camera.resolution = (3280, 2464)
  #camera.framerate = 15

  for i in range(10):
    sleep(5)
    camera.capture('/home/pi/Projects/Photos/images/image{0:04d}.jpg'.format(i))

  camera.close()
  #system('convert -delay 10 -loop 0 images/image*.jpg images/animation.gif')
  print('done')

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/photos')
def photos():
  timelapse()
  return render_template('photos.html')

@app.route('/view')
def view():
  return render_template('photos.html')

@app.route('/images/<path:path>')
def images(path):
    return send_from_directory('images', path)

@app.route('/styles/<path:path>')
def styles(path):
    return send_from_directory('styles', path)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
