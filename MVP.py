import datetime


class Agenda:
    """Class to make agenda objects for people"""

    def __init__(self, name):
        self.name = name
        self.data = []

    def add_event(self, title, day, month, year):
        new_event = {}
        new_event['title'] = title
        date = datetime.datetime(year, month, day)
        new_event['date'] = date.strftime("%x")
        self.data.append(new_event)

    @property
    def get_dates(self):
        return self.data

    def __str__(self):
        return "Voici l'agenda de "+self.name


if __name__ == '__main__':
    chris = Agenda('Chris')
    chris.add_event('présentation MVP', 29, 11, 2021)
    chris.add_event('avancement du projet', 30, 11, 2021)
    print(chris)
    print(chris.get_dates)
