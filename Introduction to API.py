# Introduction to API

import pandas as pd
import matplotlib.pyplot as plt

#create a dictionary
dict_={'a':[11,21,31],'b':[12,22,32]}

# The data in the dictionary is passed along to the pandas API. Then used the dataframe to communicate with the API.
df=pd.DataFrame(dict_)
type(df)

# Call the method `head` the dataframe communicates with the API displaying the first few rows of the dataframe.
df.head()

# Call the method `mean`, the API will calculate the mean and return the value.
df.mean()



## REST APIs
from nba_api.stats.static import teams
import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

#The method .get_teams() returns a list of dictionaries.
nba_teams = teams.get_teams()

#The dictionary key id has a unique identifier for each team as a value. Let's look at the first three elements of the list:
nba_teams[0:3]

# convert the dictionary to a table
dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()

df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors

id_warriors=df_warriors[['id']].values[0][0]
# we now have an integer that can be used to request the Warriors information 

# Download the dataframe from the API call for Golden State and run the rest like a video.
import requests

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(filename, "Golden_State.pkl")

file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()

# Create two dataframes, one for the games that the Warriors faced the raptors at home, and the second for away games.
games_home=games[games['MATCHUP']=='GSW vs. TOR']
games_away=games[games['MATCHUP']=='GSW @ TOR']

# calculate the mean for the column PLUS_MINUS for the dataframes games_home and games_away:
games_home['PLUS_MINUS'].mean()
games_away['PLUS_MINUS'].mean()

# We can plot out the PLUS MINUS column for the dataframes games_home and games_away.
fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()






