import os
import pymongo


class Connect:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')

    def close(self):
        self.client.close()
    def show_statistics(self):
        stats = ["position", "clealiness", "quality/price", "service", "average vote"]
        not_selected=True
        while(not_selected):
            for item in options:
                print(item + "\n")
            print("Select an option:\n")
            chosen = input()
            if chosen not in options:
                print("The selected option is not valid. Please try again: \n")
            else:
                not_selected=False
        # chosen contiene l'attributo rispetto a cui fare statistica
    def make_statistic(self, chosen):
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

                if chosen == options[0]:  # login
                    mongodb = Connect()
                    mongodb.close()
                if chosen == options[1]:  # register
                    mongodb = Connect()
                    mongodb.close()
                if chosen == options[2]: #analitycs
                    mongodb = Connect()
                    mongodb.client.close()
                if chosen == options[3]:  # statistics
                    mongodb = Connect()
                    mongodb.close()



