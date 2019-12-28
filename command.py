import os
import pymongo


class Connect:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')


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
                    mongodb = Connect()

                if chosen == options[1]:  # register
                    mongodb = Connect()
                if chosen == options[2]: #analitycs
                    mongodb = Connect()
