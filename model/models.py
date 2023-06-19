import numpy as np
from collections import Counter

class DimensionalModel:
    def __init__(self, rating_dict):
        self.rating_dict = rating_dict
        self.counter = Counter({key: 0 for key in rating_dict.keys()})
    
    def score(self, text):
        text_rating = np.zeros(3)
        rated_words = 0
        confidence = 0
        words = text.split(",")
        for word in words:
            word = word.rstrip()
            if word in self.rating_dict:
                rating = self.rating_dict[word]
                self.counter[word] += 1
                text_rating += rating
                rated_words += 1
        if rated_words > 0:
            text_rating = text_rating/rated_words
            confidence = rated_words/len(words)
        return text_rating, confidence
    
    def score_all(self, text):
        words = text.split(",")
        text_rating = np.zeros(3)
        ratings = np.zeros((len(words), 3))
        rated_words = 0
        confidence = 0
        for index, word in enumerate(words):
            word = word.rstrip()
            if word in self.rating_dict:
                rating = self.rating_dict[word]
                self.counter[word] += 1
                text_rating += rating
                ratings[index] = rating 
                rated_words += 1
        if rated_words > 0:
            text_rating = text_rating/rated_words
            confidence = rated_words/len(words)
        return ratings, text_rating, confidence
    

class DiscreteModel:
    def __init__(self, rating_dict):
        self.rating_dict = rating_dict
        self.counter = Counter({key: 0 for key in rating_dict.keys()})
    
    def score(self, text):
        text_rating = np.zeros(8)
        rated_words = 0
        confidence = 0
        words = text.split(",")
        for word in words:
            word = word.rstrip()
            if word in self.rating_dict:
                rating = self.rating_dict[word]
                self.counter[word] += 1
                text_rating += rating
                rated_words += 1
        if rated_words > 0:
            text_rating = text_rating/rated_words
            confidence = rated_words/len(words)
        return text_rating, confidence
    
    def score_all(self, text):
        words = text.split(",")
        text_rating = np.zeros(8)
        ratings = np.zeros((len(words), 8))
        rated_words = 0
        confidence = 0
        for index, word in enumerate(words):
            word = word.rstrip()
            if word in self.rating_dict:
                rating = self.rating_dict[word]
                self.counter[word] += 1
                text_rating += rating
                ratings[index] = rating 
                rated_words += 1
        if rated_words > 0:
            text_rating = text_rating/rated_words
            confidence = rated_words/len(words)
        return ratings, text_rating, confidence