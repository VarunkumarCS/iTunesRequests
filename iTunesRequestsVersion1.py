import requests
import json 

#requesting api in this program
url = "https://itunes.apple.com/gb/rss/customerreviews/id=1500780518/sortBy=mostRecent/json"
r = requests.get(url)
data = r.json()

#calling the keys and values and printing it
def enteries():
    y = data['feed']['author']
    print("The enteries for [feed][author] are: ", y)
print()



enteries1= data['feed']['updated']
print(enteries1)
print()

enteries2= data['feed']['rights']
print(enteries2)
print()

enteries3= data['feed']['title']
print(enteries3)
print()

enteries4= data['feed']['icon']
print(enteries4)
print()

"""""""""


for entry in data:
    a = data["author_uri"].append(entry["author"]["uri"]["label"])
    print(a)


for entry in enteries:
    for key,val in entry.items():
        for subkey, subval in val.items:
            if not isinstance(subval, dict):
                data[f"{key}_{subkey}"].append(subval)

            else:
                for att_key, att_val in subval.items():
                    data[f"{key}_{subkey}_{att_key}"].append(att_val)

print(data)

"""""""""