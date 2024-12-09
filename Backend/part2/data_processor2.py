import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

credits = pd.read_csv('credits.csv')

# print(credits.head())

meta = pd.read_csv("movies_metadata.csv")

# print(meta.head())

meta['release_date'] = pd.to_datetime(meta['release_date'], errors='coerce')

meta['year'] = meta['release_date'].dt.year

#selected data from 2017 because in part 1 we only had till 2016(including)
new_meta = meta.loc[meta['year'] == 2017, ['genres', 'id', 'title', 'year']]

#changed its type from object to int because we will work with it later on as integer
new_meta['id'] = new_meta['id'].astype(int)

data = pd.merge(new_meta, credits, on='id')

import ast

#turned string into python list/dictionary etc. for being able to work on it
data['genres'] = data['genres'].map(lambda x: ast.literal_eval(x))
data['cast'] = data['cast'].map(lambda x : ast.literal_eval(x))
data['crew'] = data['crew'].map(lambda x : ast.literal_eval(x))

# print(data.head())

def make_genresList(data):
    genres = []
    for object in data:
        if object.get('name') == 'Science Fiction':
            genres.append('Sci-Fi')
        else:
            genres.append(object.get('name'))
    if genres == []:
        return np.nan
    else:
        return " ".join(genres)
  
data['genres_list'] = data['genres'].map(lambda x : make_genresList(x))  
  
def get_actor1(data):
    actors = []
    for object in data:
        actors.append(object.get('name'))
    if actors == []:
        return np.nan
    else:
        return actors[0] #we want first actor, thats why index is 0

print(data.describe())













