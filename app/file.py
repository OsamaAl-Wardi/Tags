import io
import os

class File:
    def get_name(filename):
        return filename.split('.')[0]

    def get_named(filename):
        return int(filename.split('.')[0])

    def get_extension(filename):
        return filename.split('.')[1]

    def get_content(path, filename):
        abspath = os.path.join(os.path.dirname(path), filename)
        with io.open(abspath, 'rb') as f:
            content = f.read()
        return content

    def get_files(path, extension=None, sorting=None):
        # extension
        if extension == None:
            files = [f for f in os.listdir(path) if not f.startswith('.')]
        else:
            files = [f for f in os.listdir(path) if not f.startswith('.') and f.endswith(extension)]

        # sorting
        if sorting != None:
            files.sort(key=sorting)
            
        return files