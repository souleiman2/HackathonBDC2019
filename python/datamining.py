import requests
import pickle
import os

filename = 'data.pickle'

def filter(segment_name):
    res = []
    for item in items:
        if item["segment_name"] == segment_name:
            res.append(item)
    return res

if not os.path.isfile('data.pickle'):
    max_page_number = 1164
    items = []
    for page_number in range(max_page_number):
        print('{}% done'.format(round(100 * (page_number + 1)/max_page_number, 2)))
        url = 'https://hackathon-api.bdc.n360.io/website_statistics?page={}'.format(page_number)

        response = requests.post(url)

        data = response.json()
        items += data["Items"]
    with open(filename, 'wb') as f:
        pickle.dump(items, f)
else:
    with open(filename, 'rb') as f:
        items = pickle.load(f)

print(items[0].keys())

temp = []
for item in items:
    web_id = item["website_id"]
    if web_id == 9:
        temp.append(item)
        
items = temp

all_users_items = filter("All Users")
new_users_items = filter("New Users")
ret_users_items = filter("Returning Users")
organic_traffic_items = filter("Organic Traffic")



pageviews = list(map(lambda item: item["pageviews"], all_users_items))
months = list(map(lambda item: item["date_start"][:-3], all_users_items))
print(pageviews)
print(months)

print(len(items))
