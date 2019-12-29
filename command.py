import os
import pymongo
import elements


class Connect:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.cities = ["Firenze"]
        self.nations = ["Russia"]

    def close(self):
        self.client.close()

    def show_statistics(self, place, type):
        stats = ["position", "cleanliness", "quality/price", "service", "average vote"]
        not_selected = False

        while (not_selected == False):
            for item in stats:
                print(item + "\n")
            print("Select an attribute:\n")
            chosen = input()
            if chosen in stats:
                self.make_statistic(chosen, place, type)
                not_selected = True

    def make_statistic(self, chosen, place, type):
        db = self.client.test_database
        coll = db.hotels
        numPos = db.hotels.count({"$and": [{chosen: {"$gt": 6}}, {type: place}]})
        numNeg = db.hotels.count({"$and": [{chosen: {"$lt": 5}}, {type: place}]})
        numMed = db.hotels.count({type: place}) - (numPos + numNeg)


if __name__ == '__main__':

    options = ["login", "register", "read analytics", "read statistics"]

    print("Options:\n")
    for item in options:
        print(item + "\n")
    print("Select an option:\n")
    while (True):
        chosen = input()

        pid = os.fork()
        if pid == 0:  # child process

            if chosen == options[0]:  # login
                mongodb = Connect()
                mongodb.close()
            if chosen == options[1]:  # register
                mongodb = Connect()
                mongodb.close()
            if chosen == options[2]:  # analitycs
                mongodb = Connect()
                mongodb.client.close()
            if chosen == options[3]:  # statistics
                mongodb = Connect()
                print("Options:\n")
                opt = ["city", "nation"]
                for item in opt:
                    print(item + "\n")
                print("Select an option:")
                type = input()
                if type == "city":
                    for item in mongodb.cities:
                        print(item + "\n")
                    print("Select an option:")
                    place = input()
                    mongodb.show_statistics(type, place)

                elif type == "nation":
                    for item in mongodb.cities:
                        print(item + "\n")
                    print("Select an option:")
                    place = input()
                    mongodb.show_statistics(type, place)
                mongodb.close()
