# API Examples
# Random User and Fruityvice API Examples

from randomuser import RandomUser
import pandas as pd

separation_line = '-----------------------'

# create a random user object, r.
r = RandomUser()

# get a list of random 10 users.
some_list = r.generate_users(10)

# get full name, we call `get_full_name()` function.
name = r.get_full_name()

# we only need 10 users with full names and their email addresses. We  write a "for-loop" to print these 10 users
for user in some_list:
    print (user.get_full_name()," ",user.get_email())

print(separation_line)


def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

get_users()

df1 = pd.DataFrame(get_users())  

print(separation_line)

## Example 2: Fruityvice API
import requests
import json

# We will obtain the [fruityvice](https://www.fruityvice.com) API data using `requests.get("url")` function. The data is in a json format.
data = requests.get("https://fruityvice.com/api/fruit/all")

# We will retrieve results using `json.loads()` function.
results = json.loads(data.text)

results = json.loads(data.text)

# We will convert our json data into *pandas* data frame. 
pd.DataFrame(results)

df2 = pd.json_normalize(results)

# we can extract some information from this dataframe
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

# Official Joke API 
# This API returns random jokes from a database. The following URL can be used to retrieve 10 random jokes.
data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")

# Retrieve results using `json.loads()` function.
results2 = json.loads(data2.text)

#Convert json data into *pandas* data frame. Drop the type and id columns.
df3 = pd.DataFrame(results2)
df3.drop(columns=["type","id"],inplace=True)
print(df3)




