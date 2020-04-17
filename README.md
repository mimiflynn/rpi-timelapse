# Raspberry Pi Zero Timelapse

![timelapse](https://github.com/mimiflynn/rpi-timelapse/blob/master/result.gif)

## Tech Stack

- Python 3.4
- Flask
- ImageMagick
- Raspberry Pi 3
- Raspberry Pi Camera

## Startup

For GIF making magic install ImageMagick with `sudo apt install imagemagick`.

`python3 manage.py`

## Objective

Trigger timelapse capture from my phone via password protected website.

## Deploy

### Create directories

```buildoutcfg
mkdir picam/client/static/{archive,gifs,images,timelapse}
```

### systemd

`/etc/systemd/system/photos.service`

```buildoutcfg
[Unit]
Description=Gunicorn instance to take timelapses
After=network.target

[Service]
User=pi
Group=www-data
WorkingDirectory=/home/pi/Projects/Photos
ExecStart=/usr/local/bin/gunicorn --workers 3 --timeout 999 -k gevent --threads 12 --bind unix:photos.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

```buildoutcfg
sudo systemctl status photos.service

sudo systemctl start photos.service

sudo systemctl stop photos.service
```


### nginx

`/etc/nginx/sites-available/default`

```buildoutcfg
upstream flask_server {
        # swap the commented lines below to switch between socket and port
        server unix:/home/pi/Projects/Photos/photos.sock fail_timeout=0;
        # server 127.0.0.1:5000 fail_timeout=0;
}
server {
	listen 2002;
	server_name domain-name-of-yours.com;

	# Set up proxy for app
	location / {
	    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_redirect off;

	    include proxy_params;
	    proxy_pass http://flask_server;
	}
	
	# Configure NGINX to deliver static content from the specified folder
    location /static {
       alias /home/pi/Projects/Photos/picam/client/static;
    }
}
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
