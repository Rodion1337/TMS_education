import requests
spoiler = requests.get('https://api.kanye.rest')
kanye_west = spoiler.json()
print(kanye_west['quote'])
