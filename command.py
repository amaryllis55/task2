import os
import pymongo
import elements


class Connect:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')

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
                not_selected = True
                self.make_statistic(chosen)

    def make_statistic(self, chosen):
        print("TODO: " + chosen)


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
