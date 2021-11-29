import datetime


class Agenda:
    """Class to make agenda objects for people"""

    def __init__(self, name):
        self.name = name
        self.data = []

    def add_event(self, title, day, month, year):
        """add a dictionary in a list (self.data)"""
        new_event = {}
        new_event['title'] = title
        date = datetime.datetime(year, month, day)
        new_event['date'] = date.strftime("%x")
        self.data.append(new_event)

    def delete_event(self, title):
        """delete an item based on his name"""
        flag = False
        for event in self.data:
            if title == event['title']:
                flag = True
                self.data.remove(event)
        if flag == False:
            raise ValueError("L'évenement demandé n'existe pas")

    def modify_event(self, title, ntitle, day, month, year):
        """modify an event based on his name"""
        flag = False
        for event in self.data:
            if title == event['title']:
                flag = True
                self.data.remove(event)
        if flag == False:
            raise ValueError("L'évenement demandé n'existe pas")
        new_event = {}
        new_event['title'] = ntitle
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
    igor = Agenda('Igor')
    igor.add_event('TP7', 30,11,2021)
    igor.modify_event('TP7', 'TP8', 30,11,2021)
    chris.add_event('présentation MVP', 29, 11, 2021)
    chris.add_event('avancement du projet', 30, 11, 2021)
    #chris.delete_event('présentation MVP')
    print(chris)
    print(chris.get_dates)
    print(igor)
    print(igor.get_dates)
