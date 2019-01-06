import os, shutil

from app.scene import SceneAnnotator
from app.tags import annotate

# remove 'frames' folder before using it
if os.path.isdir('frames'):
    shutil.rmtree('frames')

# hard-coded this thing!!
filename = "videos/desert.mp4"
path = 'frames/'
skip = 20

# annotate the video
scenes = annotate(path, filename, skip)

# show
for scene in scenes:
    SceneAnnotator.show(scene)