from google.cloud import vision
from google.cloud.vision import types

class FrameAnnotator:
    client = vision.ImageAnnotatorClient()

    def annotate(content):
        image = types.Image(content=content)

        # detect labels
        response = FrameAnnotator.client.label_detection(image=image, timeout=10)
        labels = response.label_annotations
        
        return [x.description for x in labels] if len(labels) > 0 else []