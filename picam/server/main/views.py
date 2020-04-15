from flask import render_template, request, Blueprint

from utils import singlephoto, timelapse, create_gif
from utils import make_tree


main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/')
def index():
    singlephoto()
    return render_template('index.html')


# /timelapse?frames=50&freq=5
@main_blueprint.route('/timelapse')
def run_timelapse():
    # frames = request.args.get('frames', 50, type=int)
    # freq = request.args.get('freq', 5, type=int)
    timelapse()
    create_gif()
    path = '/home/pi/Projects/Photos/picam/client/static/gifs'
    return render_template('animations.html', tree=make_tree(path))


@main_blueprint.route('/view')
def view():
    path = '/home/pi/Projects/Photos/picam/client/static/images'
    return render_template('photos.html', tree=make_tree(path))


@main_blueprint.route('/archive')
def archive():
    path = '/home/pi/Projects/Photos/picam/client/static/archive'
    return render_template('archive.html', tree=make_tree(path))


@main_blueprint.route('/gif')
def gif():
    create_gif()
    path = '/home/pi/Projects/Photos/picam/client/static/gifs'
    return render_template('animations.html', tree=make_tree(path))


@main_blueprint.route('/animations')
def animations():
    path = '/home/pi/Projects/Photos/picam/client/static/gifs'
    return render_template('animations.html', tree=make_tree(path))
