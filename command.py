import os
import pymongo
import elements


class Connect:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.cities = [["Firenze", 4343]]
        self.nations = [["Russia", 9090]]
        self.dictionary={}#contiene i codici corrispondenti a città e nazione

        for item in self.cities:
            if item[0] not in self.dictionary.keys():
                self.dictionary[item[0]]=item[1]
        for item in self.nations:
            if item[0] not in self.dictionary.keys():
                self.dictionary[item[0]]=item[1]

    def updateDict(self, name, code):
        if name not in self.dictionary.keys():
            self.dictionary[name]=code

    def close(self):
        self.client.close()

    def manageAnalytics(self):
        opt = ["averageRating", "serviceRating", "cleanlinessRating", "positionRating"]
        for item in opt:
            print(item)
        chosen = input("Select evaluation attribute:\n")


    def manageStatistics(self):
        opt=["averageRating", "serviceRating","cleanlinessRating", "positionRating"]
        for item in opt:
            print(item)
        chosen=input("Select evaluation attribute:\n")
        if chosen in opt:
            plt = input("Select city or nation:\n")
            if plt == "city":
                for item in self.cities:
                    print(item[0] )
                city = input("Select city:\n")
                if city in self.dictionary.keys():
                    self.computeAvg(chosen, self.dictionary[city], "CityID")
            elif plt=="nation":
                for item in self.nations:
                    print(item[0])
                nation = input("Select city:\n")
                if nation in self.dictionary.keys():
                    self.computeAvg(chosen, self.dictionary[nation], "NationID")




    def computeAvg(self, chosen, place, type):
        db = self.client.test_database
        coll = db.hotels
        numPos = db.hotels.count_documents({"$and": [{chosen: {"$gt": 6}}, {type: place}]})
        numNeg = db.hotels.count_documents({"$and": [{chosen: {"$lt": 5}}, {type: place}]})
        numMed = db.hotels.count_documents({type: place}) - (numPos + numNeg)
        print(numPos, numNeg, numMed)
        #plot?


if __name__ == '__main__':

    options = ["login", "register", "read analytics", "read statistics"]

    print("Options:\n")
    for item in options:
        print(item + "\n")
    print("Select an option:\n")

    while (True):
        chosen=input()
        #pid = os.fork()
        #if pid == 0:  # child process
        if chosen == options[0]:  # login
            mongodb = Connect()
            mongodb.close()
        if chosen == options[1]:  # register
            mongodb = Connect()
            mongodb.close()
        if chosen == options[2]:  # analitycs
            mongodb = Connect()
            mongodb.close()
        if chosen == options[3]:  # statistics
            mongodb = Connect()
            mongodb.manageStatistics()
            mongodb.close()
        print("Select an option:\n")


