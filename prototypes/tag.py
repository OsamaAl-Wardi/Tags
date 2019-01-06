##### old

# from scenes_separator import annotate_scenes, print_scene
# from word_count import annotate_frames

# import cv2, os, sys

# def annotate(path, filename, skip):
#     # check whether the frames folder existed, if not, create
#     if not os.path.isdir(path):
#         try:
#             os.makedirs(path)
#         except:
#             sys.exit()

#     # create a VideoCapture object for reading frames 
#     # and retrieve its intrinsic parameters
#     video = cv2.VideoCapture(filename)
#     fps = video.get(cv2.cv.CV_CAP_PROP_FPS)

#     # read and export every nth frame from the video
#     frame_index = 0
#     success, image = video.read()
#     while success:
#         if frame_index % skip == 0:
#             print('split_video: %d' % frame_index)
#             cv2.imwrite(path + "/%d.jpg" % int(frame_index/skip), image)
#         frame_index += 1
#         success, image = video.read()

#     # find all words in each frame
#     frames = annotate_frames(path)

#     # check for groups of scenes
#     scenes = annotate_scenes(frames)

#     for scene in scenes:
#         print_scene(scene)

# path = '../frames/'
# filename = '../videos/dessert.mp4'
# skip = 10
# annotate(path, filename, skip)