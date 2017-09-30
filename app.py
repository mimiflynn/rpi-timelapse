from flask import Flask, render_template, send_from_directory

from utils.camera import singlephoto, timelapse, create_gif
from utils.utils import make_tree


app = Flask(__name__)


@app.route('/')
def index():
    singlephoto()
    return render_template('index.html')


@app.route('/timelapse')
def photos():
    timelapse()
    create_gif()
    path = '/home/pi/Projects/Photos/gifs'
    return render_template('animations.html', tree=make_tree(path))


@app.route('/view')
def view():
    path = '/home/pi/Projects/Photos/images'
    return render_template('photos.html', tree=make_tree(path))


@app.route('/archive')
def archive():
    path = '/home/pi/Projects/Photos/archive'
    return render_template('archive.html', tree=make_tree(path))


@app.route('/gif')
def gif():
    create_gif()
    path = '/home/pi/Projects/Photos/gifs'
    return render_template('animations.html', tree=make_tree(path))


@app.route('/animations')
def animations():
    path = '/home/pi/Projects/Photos/gifs'
    return render_template('animations.html', tree=make_tree(path))


@app.route('/images/<path:path>')
def images(path):
    return send_from_directory('images', path)


@app.route('/gifs/<path:path>')
def gifs(path):
    return send_from_directory('gifs', path)


@app.route('/archive/<path:path>')
def archives(path):
    return send_from_directory('archive', path)


@app.route('/styles/<path:path>')
def styles(path):
    return send_from_directory('styles', path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
