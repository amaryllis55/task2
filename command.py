import os
import pymongo


class Connect:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')

    def close(self):
        self.client.close()

    def show_statistics(self):
        stats = ["position", "clealiness", "quality/price", "service", "average vote"]
        nations = ["Russia", "Polonia", "Italia", "Firenze", "San Pietroburgo", "Cracovia", "Breslavia"]
        not_selected = True
        chosen = None
        while (not_selected):
            for item in nations:
                print(item + "\n")
            print("Select an option:\n")
            chosen = input()
            if chosen not in options:
                print("The selected option is not valid. Please try again: \n")
            else:
                not_selected = False

        while (not_selected == False):
            for item in stats:
                print(item + "\n")
            print("Select an option:\n")
            chosen = input()
            if chosen in options:
                not_selected = True
        if chosen != None:
            self.make_statistic(chosen)
        # chosen contiene l'attributo rispetto a cui fare statistica

    def make_statistic(self, chosen):
        print("TODO")


class Review:
    def __init__(self, vote, text, year, month):
        self.vote = vote
        self.text = text
        self.year = year
        self.month = month


class Hotel:
    def __init__(self, name, serviceRating, numberReview, cleaninessRating, positionRating, qualityPriceRating,
                 description):
        self.name = name
        self.numberReview = numberReview
        self.cleaninessRating = cleaninessRating
        self.positionRating = positionRating
        self.qualityPriceRating = qualityPriceRating
        self.serviceRating = serviceRating
        self.description = description
        self.rewiews = []

    def computeAverageRating(self, avgB, numB, avgT, numT):
        self.avgRating = (avgB * numB + avgT * numT) / self.numberReview

    def setAverageRating(self, avg):
        self.avgRating = avg

    def addReview(self, vote):
        print("TODO")


if __name__ == '__main__':

    options = ["login", "register", "read analytics", "read statistics"]

    print("Options:\n")
    for item in options:
        print(item + "\n")
    print("Select an option:\n")
    while (True):
        chosen = input()
        if chosen not in options:
            print("The selected option is not valid. Please try again: \n")
        else:
            pid = os.fork()
            if pid == 0:  # child process
                mongodb = Connect()
                if chosen == options[0]:  # login
                    mongodb.close()
                if chosen == options[1]:  # register
                    mongodb.close()
                if chosen == options[2]:  # analitycs
                    mongodb.client.close()
                if chosen == options[3]:  # statistics
                    mongodb.close()
