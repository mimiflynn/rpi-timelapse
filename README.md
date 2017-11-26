# Raspberry Pi Zero Timelapse

![timelapse](https://github.com/mimiflynn/rpi-timelapse/blob/master/result.gif)

## Tech Stack

- Python 3.4
- Flask
- ImageMagick
- Raspberry Pi 3
- Raspberry Pi Camera

[Blog Post Describing Setup](https://trailingwhitespace.com/articles/rpi-camera-flask/)

## Startup

For GIF making magic install ImageMagick with `sudo apt install imagemagick`.

`python3 app.py`

## Objective

Trigger timelapse capture from my phone via password protected website.

## Deploy

```buildoutcfg
sudo systemctl status photos.service

sudo systemctl start photos.service

sudo systemctl stop photos.service
```

## End Points

`/` - takes a photo and displays it

`/view` - view all single photos

`/timelapse` - takes 50 photos with a 5 second delay

`/gif` - create gif from last timelapse

`/animations` - view all timelaps gifs

`/archive` - contains list of zipped up timelapse images

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

to make a gif from the timelapse images: `convert -delay 20 -loop 0 image*.jpg result.gif`
