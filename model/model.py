import numpy as np
import classla

class Model:
    def __init__(self, rating_dict):
        self.rating_dict = rating_dict
        self.lem = classla.Pipeline("hr", processors='tokenize, pos, lemma', tokenize_no_ssplit=True, use_gpu=False)

    def score(self, text):
        text_rating = np.zeros(2)
        rated_words = 0
        for word in text:
            word = self.lem(word).sentences[0].words[0].lemma

            if word in self.rating_dict:
                rating = self.rating_dict[word]
                text_rating += rating
                rated_words += 1
        
        confidence = rated_words/len(text)
        return text_rating, confidence
    
    def score_all(self, text):
        text_rating = np.zeros(2)
        rated_words = 0
        words = self.lem(text)
        for word in words.sentences[0].words:
            word = word.lemma

            if word in self.rating_dict:
                rating = self.rating_dict[word]
                text_rating += rating
                rated_words += 1
        
        confidence = rated_words/len(text)
        return text_rating, confidence
