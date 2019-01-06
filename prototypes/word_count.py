import io
import os

from collections import Counter
from google.cloud import vision
from google.cloud.vision import types

def get_file_number(filename):
    return int(filename.split('.')[0])

def annotate_frames(path):
    client = vision.ImageAnnotatorClient()
    frames = []

    # sort files in an ascending order
    files = [f for f in os.listdir(path) if not f.startswith('.')]
    files.sort(key=get_file_number)

    for file in files:
        print('annotate_frames: %s' % file)

        # get the image
        file_name = os.path.join(os.path.dirname(path), file)
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)

        # detect labels
        response = client.label_detection(image=image, timeout=10)
        labels = response.label_annotations

        if len(labels) == 0:
            frames.append(['none'])
            continue

        # put each frame's labels into a list in frames
        frames.append([x.description for x in labels])

    return frames

# for frame in annotate_frames('../frames/'):
#     print(frame)