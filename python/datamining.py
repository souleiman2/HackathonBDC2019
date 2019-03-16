import requests

max_page_number = 547001
page_number = 1
url = 'https://hackathon-api.bdc.n360.io/website_statistics?page={}'.format(page_number)

response = requests.post(url)

data = response.json()
for item in data["Items"]:
    print(item)
