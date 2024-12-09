import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

data = pd.read_csv("movie_metadata.csv")

data = data.loc[:,['director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'genres', 'movie_title']]

# print(data.isna().sum())

data['director_name'] = data['director_name'].replace(np.nan, "unknown")
data['actor_1_name'] = data['actor_1_name'].replace(np.nan, "unknown")
data['actor_2_name'] = data['actor_2_name'].replace(np.nan, "unknown")
data['actor_3_name'] = data['actor_3_name'].replace(np.nan, "unknown")

# print(data.isna().sum())

data["genres"] = data["genres"].str.replace("|", " ")


data['movie_title'] = data['movie_title'].str.lower()


#note in terminal i didnt see any \xa0 but cleaned it anyway
data['movie_title'] = data['movie_title'].apply(lambda x: x[:-1])


data.to_csv("data1.csv", index=False)