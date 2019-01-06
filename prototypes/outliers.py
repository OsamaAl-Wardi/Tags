#Saurav Dahal
#dahal.saurav123@gmail.com

def removeOutliers(frame_dict, object_count):
    outliers_list = []
    numberOfFrames = len(frame_dict)
    for objects in object_count:
        if object_count[objects] == numberOfFrames:
            outliers_list.append(objects)

    new_frame_list = []
    i = 0
    for frame in frame_dict:
        new_frame_list.append([])
        for word in frame:
            if word not in outliers_list:
                new_frame_list[i].append(word)
        print(frame, new_frame_list[i])
        i += 1


frame_dict = [['cat', 'bird', 'beak', 'wildlife', 'people'], ['people', 'cat', 'dog'], ['tree', 'football', 'people', 'beak', 'cat'], ['dog', 'cat', 'tree', 'people']]
object_count = {'bird': 1, 'beak': 2, 'wildlife': 1, 'people': 4, 'cat': 4, 'dog': 2, 'tree': 2, 'football':1}
removeOutliers(frame_dict, object_count)