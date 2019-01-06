#calls function that returns a list of scene objects 
#Outputs dictonary of scenes mapped to containing words
import scene_separator

#get list returns dict
def convert(scenes):
    output = {}
    counter = 1
    for scene in scenes:
        output['Scene ' + str(counter)] = list(scene.words.keys())
        counter += 1
    return output

#Calls function that returns list of scene object from video file
def trial2():
    scenes = scene_separator.trial()
    a = convert(scenes)
    return a
