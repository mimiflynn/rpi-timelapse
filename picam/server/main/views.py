from flask import render_template, send_from_directory, Blueprint

from utils.camera import singlephoto, timelapse, create_gif
from utils.utils import make_tree


main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/')
def index():
    singlephoto()
    return render_template('index.html')


@main_blueprint.route('/timelapse')
def photos():
    timelapse()
    create_gif()
    path = '/home/pi/Projects/Photos/static/gifs'
    return render_template('animations.html', tree=make_tree(path))


@main_blueprint.route('/view')
def view():
    path = '/home/pi/Projects/Photos/static/images'
    return render_template('photos.html', tree=make_tree(path))


@main_blueprint.route('/archive')
def archive():
    path = '/home/pi/Projects/Photos/static/archive'
    return render_template('archive.html', tree=make_tree(path))


@main_blueprint.route('/gif')
def gif():
    create_gif()
    path = '/home/pi/Projects/Photos/static/gifs'
    return render_template('animations.html', tree=make_tree(path))


@main_blueprint.route('/animations')
def animations():
    path = '/home/pi/Projects/Photos/static/gifs'
    return render_template('animations.html', tree=make_tree(path))
