from observer_pattern.observers.base_observer import Observer


class EmailManager(Observer):
    receipients = []

    def send_email(self, email, subject, body):
        print(f'Email: {email}\nTitle: {subject}\nBody: {body}\n')
        print(f'Sent mock email to {email}')
    
    def send_all(self, subject, body):
        list(
            map(lambda email: self.send_email(email, subject, body), self.receipients)
        )

    def update(self, eventType, data, subject):
        from observer_pattern.subjects.editor import Editor

        if eventType == Editor.FILE_WRITE_EVENT:
            file = data.get('file')
            subject = f'Critical update'
            body = f'Critical {file} updated on production'

            self.send_all(subject, body)
