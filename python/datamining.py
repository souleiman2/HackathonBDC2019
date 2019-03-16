import requests
import pickle
import os

filename = 'data.pickle'

def filter(item, segment_name):
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

all_users_items = filter(items, "All Users")
new_users_items = filter(items, "New Users")
ret_users_items = filter(items, "Returning Users")
organic_traffic_items = filter(items, "Organic Traffic")

time_au = list(map(lambda item: item["time_on_page"], all_users_items))
time_nu = list(map(lambda item: item["time_on_page"], new_users_items))
time_eu = list(map(lambda item: item["time_on_page"], ret_users_items))

avegage_time_au = list(map(lambda item: item["avg_time_on_page"], all_users_items))
avegage_time_nu = list(map(lambda item: item["avg_time_on_page"], new_users_items))
avegage_time_eu = list(map(lambda item: item["avg_time_on_page"], ret_users_items))

pageviews_au = list(map(lambda item: item["pageviews"], all_users_items))
pageviews_nu = list(map(lambda item: item["pageviews"], new_users_items))
pageviews_eu = list(map(lambda item: item["pageviews"], ret_users_items))

sessions_nu = list(map(lambda item: item["sessions"], new_users_items))
sessions_au = list(map(lambda item: item["sessions"], all_users_items))
sessions_eu = list(map(lambda item: item["sessions"], ret_users_items))

bounce_nu = list(map(lambda item: item["bounce_rate"], new_users_items))
bounce_au = list(map(lambda item: item["bounce_rate"], all_users_items))
bounce_eu = list(map(lambda item: item["bounce_rate"], ret_users_items))

months = list(map(lambda item: item["date_start"][:-3], all_users_items))
months_ = list(map(lambda item: item["date_start"][:-3], new_users_items))

print("time per page: ")
print(time_au)
print(time_nu)

print("Time average : ")
print(avegage_time_au)
print(avegage_time_nu)

print("Sessions : ")
print(sessions_au)
print(sessions_nu)

print("Bounce : ")
print(bounce_au)
print(bounce_nu)

print("page views  : ")
print(pageviews_au)
print(pageviews_nu)

print("MONTHS:")
print(months)
print(months_)

print(len(items))
