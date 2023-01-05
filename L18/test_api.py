import requests
spoiler = requests.get('https://api.kanye.rest')
kanye_west = spoiler.text
print(kanye_west[(kanye_west.find(":",0)+1):-1])
