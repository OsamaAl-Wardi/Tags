import cv2, os, sys

def split_video(filename, path, skip):
    # create the frames folder if not yet existed
    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except:
            sys.exit()

    # create a VideoCapture object for reading frames
    vidcap = cv2.VideoCapture(filename)

    # read and export every nth frame
    frame_index = 0
    success, image = vidcap.read()
    while success:
        if frame_index % skip == 0:
            print('split_video: %d' % frame_index)
            cv2.imwrite(path + "/%d.jpg" % int(frame_index/skip), image)
        frame_index += 1
        success, image = vidcap.read()

# split_video('../video.mp4', '../frames/', 30)