import os
import pymongo


class Connect:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')

    def close(self):
        self.client.close()


if __name__ == '__main__':

    options = ["login", "register", "read analytics", "read statistics"]
    stats=["position", "clealiness", "quality/price",  "service", "average vote" ]
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
                    mongodb.client.close()

                if chosen == options[1]:  # register
                    mongodb = Connect()
                    mongodb.client.close()
                if chosen == options[2]: #analitycs
                    mongodb = Connect()
                    mongodb.client.close()
                if chosen == options[3]:  # analitycs
                    mongodb = Connect()
                    mongodb.client.close()


