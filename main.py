import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# import data
data = pd.read_csv('kdrama.csv')
# print(data)

# create a set of stop words to remove from the synopsis
stop_words = set(stopwords.words('english'))

def suggest_shows(genre, cast):
    shows = data[["Name",
                 # "Aired Date",
                 # "Year of release",
                 # "Original Network",
                 # "Aired On",
                 # "Number of Episodes",
                 # "Duration",
                 # "Content Rating",
                 # "Rating",
                 "Synopsis",
                 "Genre",
                 # "Tags",
                 # "Director",
                 # "Screenwriter",
                 "Cast",
                # "Production companies",
                # "Rank"
                ]]
    show_arr = np.array(shows)
    
    # extract keywords from the synopses of previous shows
    keywords = set()
    for show in show_arr:
        if show[2] != genre and all(actor not in show[3] for actor in cast):
            synopsis = show[1].lower()
            tokens = word_tokenize(synopsis)
            keywords.update([token for token in tokens if token not in stop_words])

#     # The resulting list of suggestions is converted to a set to remove duplicates and returned.
#     suggest = []
#     for show in show_arr:
#         if show[1] == genre:
#             suggest.append(show[0])

#         for actor in cast:
#             if actor in show[2]:
#                 suggest.append(show[0])
#     return list(set(suggest))

     # suggest new shows based on the extracted keywords
    suggest = []
    for show in show_arr:
        if show[2] == genre or any(actor in show[3] for actor in cast):
            synopsis = show[1].lower()
            tokens = word_tokenize(synopsis)
            if any(token in keywords for token in tokens):
                suggest.append(show[0])

    # remove duplicates and return the list of suggestions
    return list(set(suggest))



# Example usage
suggestions = suggest_shows('Horror', 'Lee Je Hoon')
print("Show suggestions:", suggestions)
