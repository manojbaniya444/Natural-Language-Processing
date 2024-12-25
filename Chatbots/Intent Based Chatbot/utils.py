import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np
# nltk.download('punkt') # package with pretrained tokenizer

def tokenize(sentence):
    """Tokenize the sentence into token"""
    return nltk.word_tokenize(sentence)

def stem(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    """Return bag of words array: 0 or 1 for each word in the bag that exists in the sentence"""
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1
            
    return bag

if __name__ == "__main__":
    print(tokenize("How long does shipping take?"))
    words = ["Organize", "organizes", "organizing"]
    stems = [stem(word) for word in words]
    bag = bag_of_words(["How", "long", "does", "shipping", "take", "?"], ["How", "long", "does", "shipping", "take", "?"])
    print(stems)
    print(bag)