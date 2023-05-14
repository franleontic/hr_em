import numpy as np
import classla
import stopwordsiso as stopwords

class Model:
    def __init__(self, rating_dict):
        self.rating_dict = rating_dict
        self.lem = classla.Pipeline("hr", processors='tokenize, pos, lemma', tokenize_no_ssplit=True, use_gpu=False)
        self.sw = stopwords.stopwords("hr")

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
        confidence = 0
        text = text.replace(",", " ")
        words = self.lem(text)
        if len(words.sentences) > 0:
            for word in words.sentences[0].words:
                word = word.lemma
                print(f"Word is {word}")
                if word in self.rating_dict:
                    print(f"Found {word}")
                    rating = self.rating_dict[word]
                    text_rating += rating
                    rated_words += 1
        
        if len(words.sentences) > 1:
            print("error")
        
        if rated_words > 0:
            text_rating = text_rating/rated_words
            confidence = rated_words/len(words.sentences[0].words)
        return text_rating, confidence
    
    def tokenize_and_score(self, text):
        text_rating = np.zeros(2)
        rated_words = 0
        total_words = 0
        confidence = 0
        tokens = self.lem(text)
        if len(tokens.sentences) > 0:
            for word in tokens.sentences[0].words:
                if word.upos != "PUNCT" and word.text.lower() not in self.sw:
                    total_words += 1 
                    word = word.lemma.lower()
                    print(f"Word is {word}")
                    if word in self.rating_dict:
                        print(f"Found {word}")
                        rating = self.rating_dict[word]
                        text_rating += rating
                        rated_words += 1
      
        if rated_words > 0:
            text_rating = text_rating/rated_words
            confidence = rated_words/total_words
        return text_rating, confidence
