from observer_pattern.observers.event_logger import LoggingListener 
from observer_pattern.observers.email_broadcast import EmailManager
from observer_pattern.subjects.editor import Editor


def run():
    textEditor = Editor()
    logger = LoggingListener()
    emgr = EmailManager()
    emgr.receipients.append('premkumarchalmeti@gmail.com')

    textEditor.events.subscribe(textEditor.FILE_OPEN_EVENT, logger)
    textEditor.events.subscribe(textEditor.FILE_WRITE_EVENT, emgr)

    textEditor.openFile('temp.txt', 'w')
    textEditor.writeToFile('Yoo')
    textEditor.closeFile()


if __name__ == '__main__':
    run()
