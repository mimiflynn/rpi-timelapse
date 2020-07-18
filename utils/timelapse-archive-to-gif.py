#!/usr/bin/python3

import os
import re
import sys

archive_name = sys.argv[1]


def gifify(archive):
    output_images_dir = re.sub('.tar.gz', '', archive)
    output_gif = re.sub('tar.gz', 'gif', archive)
    print('Unpacking timelapse archive {} to {} and outputting gif'.format(
        archive, output_images_dir))
    os.system('mkdir {}'.format(output_images_dir))
    os.system('tar -zxvf {} -C {}'.format(archive, output_images_dir))
    print('Creating gif {}/{}'.format(output_gif, output_gif))
    os.system(
        'convert -delay 10 -loop 0 {}/picam/client/static/timelapse/image*.jpg {}/{}'.format(output_images_dir, output_images_dir, output_gif))


gifify(archive_name)
