import os
import pymongo
import logging


class MongoConnection:
    def __init__(self, name):
        self._isEmpty = True
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.dbName = name
        self.db = self.client[name]

    def checkConnection(self):
        if self._isEmpty == False:
            return False
        else:
            if self.dbName in self.db.list_database_names():
                return True


if __name__ == '__main__':

    options = ["login", "register", "read statistics and analytics"]
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

                if chosen == options[0]:  # login
                    mongodb = MongoConnection()

                if chosen == options[1]:  # register
                    mongodb = MongoConnection()
                if chosen == options[2]:
                    mongodb = MongoConnection()
