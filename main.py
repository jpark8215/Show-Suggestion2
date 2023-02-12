import numpy as np
import pandas as pd

# import data
data = pd.read_csv('kdrama.csv')
# print(data)


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
                 # "Synopsis",
                 "Genre",
                 # "Tags",
                 # "Director",
                 # "Screenwriter",
                 "Cast",
                # "Production companies",
                # "Rank"
                ]]
    show_arr = np.array(shows)

    # The resulting list of suggestions is converted to a set to remove duplicates and returned.
    suggest = []
    for show in show_arr:
        if show[1] == genre:
            suggest.append(show[0])

        for actor in cast:
            if actor in show[2]:
                suggest.append(show[0])
    return list(set(suggest))


# Example usage
suggestions = suggest_shows('Horror', 'Lee Je Hoon')
print("Show suggestions:", suggestions)
