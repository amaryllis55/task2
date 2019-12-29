

class Review:
    def __init__(self, vote, text, year, month):
        self.vote = vote
        self.text = text
        self.year = year
        self.month = month


class Hotel:
    def __init__(self, name, numberReview, serviceRating, cleaninessRating, positionRating, qualityPriceRating,
                 description):
        self.name = name
        self.numberReview = numberReview
        self.cleaninessRating = cleaninessRating
        self.positionRating = positionRating
        self.qualityPriceRating = qualityPriceRating
        self.serviceRating = serviceRating
        self.description = description

    def computeAverageRating(self, avgB, numB, avgT, numT):
        self.avgRating = (avgB * numB + avgT * numT) / self.numberReview

    def setAverageRating(self, avg):
        self.avgRating = avg

    def addReview(self, vote):
        print("TODO")

