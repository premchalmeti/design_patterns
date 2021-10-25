from . import Subject


class Editor:
    FILE_OPEN_EVENT = 'open'
    FILE_WRITE_EVENT = 'write'
    FILE_CLOSE_EVENT = 'close'

    def __init__(self):
        self.events = Subject()

    def openFile(self, path, mode):
        self.file = open(path, mode)
        self.events.notify(self.FILE_OPEN_EVENT, {'file': self.file.name})

    def writeToFile(self, data):
        self.file.write(data)
        self.events.notify(self.FILE_WRITE_EVENT, {'file': self.file.name})

    def closeFile(self):
        self.file.close()
        self.events.notify(self.FILE_CLOSE_EVENT, {'file': self.file.name})
