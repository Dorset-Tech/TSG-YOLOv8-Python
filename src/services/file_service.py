import os


class FileService:
    def __init__(self, directory="yolo_service/videos/"):
        self.directory = directory

    def save_file(self, file):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        file_path = os.path.join(self.directory, file.filename)
        file.save(file_path)
        return file_path
