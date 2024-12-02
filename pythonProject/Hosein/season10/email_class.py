import pprint

class Email:
    emails: list['Email'] = []
    def __init__(self, client: str, server: str, title: str, subTitle: str):
        self.client = client
        self.server = server
        self.title = title
        self.subTitle = subTitle
        Email.emails.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.client!r}, {self.server!r}, {self.title!r}, {self.subTitle!r})"
    

emaul1 = Email("ME", "YOU", "Kos sher", "kossssssssssssssssssssssss")

pprint.pprint(Email.emails)