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


def mainloop():
    stop = False
    while stop == False:
        accord = input("Voulez-vous créer un agenda ?\noui/non\n").lower()
        if accord == "non":
            stop = True
        elif accord == "oui":
            nom = input("quel est votre nom ?")
            nom = Agenda(nom)
            ajout = input(
                "voulez-vous ajouter un évènement ?\noui/non\n").lower()
            qst = False
            if ajout == "oui":
                qst = True
            while qst == True:
                title = input("Titre de votre évènement: ")
                day = int(input("Jour de l'évènement: "))
                month = int(input("Mois de l'évènement: "))
                year = int(input("Année de l'évènement: "))
                nom.add_event(title, day, month, year)
                print(nom.get_dates)
                keep_asking = input(
                    "voulez-vous continuer ? (oui/non)").lower()
                if keep_asking == "non":
                    qst = False
            modif = input(
                "Voulez-vous modifier un évènement ?\noui/non\n").lower()
            if modif == "oui":
                qst = True
            while qst == True:
                print(nom.get_dates)
                title = input("Titre de l'évènement à modifier: ")
                ntitle = input("Nom du nouvel évènement: ")
                day = int(input("Jour de l'évènement: "))
                month = int(input("Mois de l'évènement: "))
                year = int(input("Année de l'évènement: "))
                nom.modify_event(title, ntitle, day, month, year)
                print(nom.get_dates)
                keep_asking = input(
                    "voulez-vous continuer de modifier ? (oui/non)\n").lower()
                if keep_asking == "non":
                    qst = False
            delete = input(
                "Voulez-vous supprimer un event ?\noui/non\n").lower()
            if delete == 'oui':
                qst = True
            while qst == True:
                print(nom.get_dates)
                title = input("Titre de l'évènement à supprimer: ")
                nom.delete_event(title)
                print(nom.get_dates)
                keep_asking = input(
                    "voulez-vous supprimer d'autres events ? (oui/non)\n").lower()
                if keep_asking == "non":
                    qst = False

            else:
                print("Merci d'avoir utilisé notre MVP")
                break


if __name__ == '__main__':
    mainloop()
