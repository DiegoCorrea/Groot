from functools import partial
import multiprocessing
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
# nltk.download('wordnet') # first-time use only


def LemTokens(tokens):
    lemmer = nltk.stem.WordNetLemmatizer()
    return [lemmer.lemmatize(token) for token in tokens]


def LemNormalize(text):
    remove_punct_dict = dict(
        (ord(punct), None)
        for punct in string.punctuation
    )
    return LemTokens(
        nltk.word_tokenize(
            text.lower().translate(remove_punct_dict)
        )
    )


def CosineSimilarity(song_set, feature):
    textlist = song_set[feature].tolist()
    TfidfVec = TfidfVectorizer(
        tokenizer=LemNormalize,
        stop_words={'english'},
        analyzer='word'
    )
    tfidf = TfidfVec.fit_transform(textlist)
    return (tfidf * tfidf.T).toarray()


def get_song_distance(song_set, song_features, classifier_important, DEBUG=True):
    pool = multiprocessing.Pool()
    all_feature_distance = pool.map(partial(CosineSimilarity, song_set), song_features)
    pool.close()
    pool.join()
    distance_matrix = np.zeros(song_set['song_id'].count())
    for (matrix, feature_weight) in zip(all_feature_distance, classifier_important):
        distance_matrix = np.add(distance_matrix, matrix*feature_weight)
    return distance_matrix
