import pymongo

if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db=client["newDB"]

    pipeline = [
        {
            "$match": {"year":2019}
         },
        {
            "$group":
                {"_id": "$month",
                 "average": {"$avg": "$Vote"}}}
    ]
    #result=db.hotel.aggregate(pipeline)

