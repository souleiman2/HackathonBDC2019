import requests

max_page_number = 1164
page_number = 1
url = 'https://hackathon-api.bdc.n360.io/website_statistics?page={}'.format(page_number)

response = requests.post(url)

data = response.json()
items = data["Items"]

print(items[0]["new_users"])

