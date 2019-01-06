class SceneAnnotator:
    # OBJECT
    def __init__(self, start, words):
        self.start = start
        self.end = None
        self.words = {word: 1 for word in words}

    def get_interval(self):
        return (start, end)

    def get_dominant_words(self, size):
        if size > len(self.words):
            return self.words
        else:
            return {word: self.words[word] for word in self.words[:size-1]}

    def has(self, words):
        return word in self.words

    def count(self, word):
        if self.has(word):
            return 0
        else:
            return self.words[word]

    def show(self):
        print("From frame {} to frame {}, there are".format(self.start, self.end))
        for word, count in self.words.items():
            print(word, count)
        print()

    # CLASS
    def group(frames, error):
        # intialize the first group of frames
        scenes = [SceneAnnotator(0, frames[0])]

        # go through all frames and check whether it belongs to the current group
        for fi in range(1, len(frames)):
            # show process
            print('grouping similar frames: {:.3%}'.format(float(fi/len(frames))), end='\r')

            # turn lists into set in order to use set operations
            scene = set(scenes[-1].words) 
            frame = set(frames[fi])

            # get the groups of words: shared and exclusive
            shared_words = scene.intersection(frame)
            exclusive_words = frame.difference(scene)

            # absolute change: change scene (significant change)
            if len(shared_words) < len(exclusive_words)*error:
                scenes[-1].end = fi-1
                scenes[-1].words = dict(sorted(scenes[-1].words.items(), key=lambda kv: kv[1], reverse=True))
                scenes.append(SceneAnnotator(fi, frames[fi]))

            # relative change: stay in the same scene
            else:
                # increment each shared word
                for word in shared_words:
                    scenes[-1].words[word] += 1
                # add new words
                for word in exclusive_words:
                    scenes[-1].words[word] = 1
        print()

        # set the last scene's end frame to be the last frame
        # since it is not set anywhere else
        scenes[-1].end = fi

        # at this point, a scene is only a camera angle
        return scenes

    def to_dict(scenes):
        dictionary = {}
        count = 1
        for scene in scenes:
            dictionary['Scene '+str(count)] = list(scene.words.keys())
            count += 1
        return dictionary