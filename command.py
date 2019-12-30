import os
import pymongo
import datetime
import elements


class Connect:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.cities = [["Firenze", 4343]]
        self.nations = [["Russia", 9090]]
        self.dates = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9,
                      "oct": 10, "nov": 11, "dec": 12}
        self.dictionary = {}  # contiene i codici corrispondenti a città e nazione

        for item in self.cities:
            if item[0] not in self.dictionary.keys():
                self.dictionary[item[0]] = item[1]
        for item in self.nations:
            if item[0] not in self.dictionary.keys():
                self.dictionary[item[0]] = item[1]

    def updateDict(self, name, code):
        if name not in self.dictionary.keys():
            self.dictionary[name] = code

    def close(self):
        self.client.close()

    def manageAnalytics(self):
        opt = ["averageRating", "serviceRating", "cleanlinessRating", "positionRating"]
        for item in opt:
            print(item)
        chosen = input("Select evaluation attribute:\n")
        if chosen in opt:
            plt = input("Select city or nation:\n")
            if plt == "city":
                for item in self.cities:
                    print(item[0])
                city = input("Select city:\n")
                if city in self.dictionary.keys():
                    self.computeAnalysis(self.dictionary[city], "CityID")
            elif plt == "nation":
                for item in self.nations:
                    print(item[0])
                nation = input("Select nation:\n")
                if nation in self.dictionary.keys():
                    self.computeAnalysis(self.dictionary[nation], "NationID")

    def computeAnalysis(self, place, type):
        now = datetime.datetime.now()  # current date and time
        day = now.strftime("%d")
        month = now.strftime("%m")
        year = now.strftime("%Y")

        # suppongo di voler prendere da dicembre 2018 a dicembre 2019

        db = self.client.test_databahse
        hotel_list = db.hotels.find({type: place})
        # hotel_list contiene tutti gli hotel nel posto place
        averall_avgs = []
        for hotel in hotel_list:
            averages = []
            for i in range(12):
                averages.append([])
            for id in hotel["reviewList"]:
                rew = db.findOne({"_id": id})
                result = self.isAntecedent(rew["Day"], rew["Month"], rew[
                    "Year"])
                if result:
                    print("TODO")

    def isAntecedent(self, day, month, year):
        current_year = datetime.datetime.now().strftime("%Y")
        if int(current_year) - int(year) <= 1 and self.dates[day]>=datetime.datetime.now().strftime("%d"):
            return True
        return False

    def manageStatistics(self):
        opt = ["averageRating", "serviceRating", "cleanlinessRating", "positionRating"]
        for item in opt:
            print(item)
        chosen = input("Select evaluation attribute:\n")
        if chosen in opt:
            plt = input("Select city or nation:\n")
            if plt == "city":
                for item in self.cities:
                    print(item[0])
                city = input("Select city:\n")
                if city in self.dictionary.keys():
                    self.computeAvg(chosen, self.dictionary[city], "CityID")
            elif plt == "nation":
                for item in self.nations:
                    print(item[0])
                nation = input("Select city:\n")
                if nation in self.dictionary.keys():
                    self.computeAvg(chosen, self.dictionary[nation], "NationID")

    def computeAvg(self, chosen, place, type):
        db = self.client.test_database
        numPos = db.hotels.count_documents({"$and": [{chosen: {"$gt": 6}}, {type: place}]})
        numNeg = db.hotels.count_documents({"$and": [{chosen: {"$lt": 5}}, {type: place}]})
        numMed = db.hotels.count_documents({type: place}) - (numPos + numNeg)
        print(numPos, numNeg, numMed)
        # plot?


if __name__ == '__main__':

    options = ["login", "register", "read analytics", "read statistics"]

    print("Options:\n")
    for item in options:
        print(item + "\n")
    print("Select an option:\n")

    while (True):
        chosen = input()
        # pid = os.fork()
        # if pid == 0:  # child process
        if chosen == options[0]:  # login
            mongodb = Connect()
            mongodb.close()
        if chosen == options[1]:  # register
            mongodb = Connect()
            mongodb.close()
        if chosen == options[2]:  # analitycs
            mongodb = Connect()
            mongodb.manageAnalytics()
            mongodb.close()
        if chosen == options[3]:  # statistics
            mongodb = Connect()
            mongodb.manageStatistics()
            mongodb.close()
        print("Select an option:\n")
