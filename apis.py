import requests
import json

import time
class Nutrition:
    # def __init__(self,foodid,label,nutrients,category,categoryLabel,image):
    #     self.foodid = foodid
    #     self.label = label
    #     self.nutrients = nutrients
    #     self.category = category
    #     self.categoryLabel = categoryLabel
    #     self.image = image
    def toclas(self):
        returns = []
        for attribute, value in self.__dict__.items():
            data = attribute, '=', value
            returns.append(data)
        return returns
    def next(self, url):
        fetch = requests.get(url)
        if fetch.status_code != 200:
            return False
        fetch = fetch.json()
        return fetch

    def data(self, ingr=None):
        url = "https://api.edamam.com/api/food-database/v2/parser"
        api_id = "4e346f4a"
        api_key = "e5525db9d1cb672290bb3d9a142e15c4"
        ingr = ingr
        params = {
            'ingr' : ingr,
            'app_id': api_id,
            'app_key': api_key,
        }
        fetch = requests.get(url, params=params)
        code = fetch.status_code
        fetch = fetch.json()
        all_data = []
        urls = []
        i = 0
        if code == 200:
            if len(fetch['parsed']) > 0:
                first_object = fetch['parsed'][0]['food']
                first_object['foodid'] = first_object.pop('foodId')
                all_data.append(first_object)


            if len(fetch['hints']) > 0:
                for i in range(0, len(fetch['hints'])):
                    hint = fetch['hints'][i]['food']
                    hint['foodid'] = hint.pop('foodId')
                    all_data.append(hint)


            if '_links' in fetch :
                next_url = fetch['_links']['next']['href']
                urls.append(next_url)


            if len(urls) > 0:

                while True:
                    fetch = Nutrition().next(urls[-1])
                    if not fetch:
                        break

                    if fetch['hints'] :
                        for i in range(1, len(fetch['hints'])):
                            if i != 0 :
                                objects = fetch['hints'][i]['food']
                                objects['foodid'] = objects.pop('foodId')
                                all_data.append(objects)

                        next_url = fetch['_links']['next']['href']
                        urls.append(next_url)
                        i += 1
                        if i % 9 == 0:
                            time.sleep(65)
                        elif i == 20:
                            break
                    else:
                        break

            return all_data
        else:
            return 'empty'



# url = "https://api.edamam.com/api/food-database/v2/parser"
# api_id = "4e346f4a"
# api_key = "e5525db9d1cb672290bb3d9a142e15c4"
# ingr = "cake"
# params = {
#             'ingr' : ingr,
#             'app_id': api_id,
#             'app_key': api_key,
#         }
# fetch = requests.get(url, params=params)

# print(fetch.json())