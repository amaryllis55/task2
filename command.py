import os
import pymongo
import elements


class Connect:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.hotels=[]
        self.rewierers=[]

    def close(self):
        self.client.close()

    def show_statistics(self):
        stats = ["position", "cleanliness", "quality/price", "service", "average vote"]
        chosen = []
        not_selected = False

        while (not_selected == False):
            for item in stats:
                print(item + "\n")
            print("Select an option:\n")
            chosen = input()
            if chosen in stats:
                self.make_statistic(chosen)
                not_selected=True

    def make_statistic(self, chosen):
        db = self.client.test_database
        coll=db.collection
        numPos=db.collection.count({chosen: {"$gt": 7}})
        numNeg=db.collection.count({chosen: {"$gt": 4}})
        numMed= db.collection.count()-(numPos+numNeg)





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
                mongodb.show_statistics()
                mongodb.close()
