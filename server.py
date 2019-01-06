import os, sys, shutil
from bottle import route, run, template, request
import urllib.request

from app.scene import SceneAnnotator
from app.tags import annotate

# adjust the skip amount per frames
skip = 10
if len(sys.argv) > 1:
    skip = int(sys.argv[-1])

extensions = ['.webm', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.mpg','.mpeg','.m2v','.3gp','mp4']

@route('/', method='GET')
def get():
    return template('templates/home.html')

@route('/', method='POST')
def post():
    # get url of video link
    url = request.forms.get('link')

    # check whether the link refers to a valid video file
    extension = url.split('/')[-1].split('.')[-1]
    if extension not in extensions:
        return "Invalid file format"

    # download and save the video
    filename = "videos/video." + extension
    urllib.request.urlretrieve(url, filename)

    # annotate video
    path = 'frames/'      # relative to the 'app' directory
    scenes = annotate(path, filename, skip)

    # remove 'videos/video...' after reading it
    os.remove(filename)

    # remove 'frames' folder after using it
    shutil.rmtree('frames')
    
    return template('templates/output.html', data=SceneAnnotator.to_dict(scenes), link=url)

run(host='localhost', port=8080)