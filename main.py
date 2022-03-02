import requests

super_heroes_list = ['Hulk', 'Captain America', 'Thanos']


def find_intel(shl):
    intel_dict = {}
    for i in range(len(shl)):
        url = f'https://superheroapi.com/api/2619421814940190/search/{shl[i]}'
        resp = requests.get(url)
        for item in resp.json()['results']:
            intel_dict[item['name']] = item['powerstats'].get('intelligence')
    max_intel = max(intel_dict.items(), key=lambda x: x[0])
    print(max_intel)


find_intel(super_heroes_list)