# Raspberry Pi Zero Timelapse

## Startup

`python3 app.py`

## Objective

Trigger timelapse capture from my phone via password protected website.

### Tech Stack

Python 3.4
Flask

## Features

`/` - takes a photo and displays it

`/view` - view last timelapse images

`/timelapse` - takes 50 photos with a 5 second delay

`/archive` - shows contents of archive directory that contains zipped up timelapse images

## References

### Documentation

http://picamera.readthedocs.io/en/release-1.11/fov.html

http://flask.pocoo.org/docs/0.11/

### Tutorials

https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/

https://www.raspberrypi.org/learning/timelapse-setup/worksheet/

https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/

http://stackoverflow.com/questions/10961378/how-to-generate-an-html-directory-list-using-python/10961991#10961991

## Notes

to make a gif from the timelapse images: `convert -delay 20 -loop 0 *.jpg result.gif`