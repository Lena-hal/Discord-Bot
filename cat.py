import requests
import json


def get_random_cat():
    cat_request = requests.get("https://api.thecatapi.com/v1/images/search")
    cat_data = json.loads(cat_request.content)

    return cat_data[0]["url"]

def get_breed_list():
    cat_request = requests.get("https://api.thecatapi.com/v1/breeds")
    print(cat_request)
    cat_breeds = json.loads(cat_request.content)
    string = ""
    for i in range(len(cat_breeds)):
        string+=f"{cat_breeds[i]['name']}: {cat_breeds[i]['id']}\n"
    return string

def get_specific_cat_breed(id: str):
    cat_request = requests.get(f"https://api.thecatapi.com/v1/images/search?breed_ids={id}")
    cat_data = json.loads(cat_request.content)
    if len(cat_data) == 0:
        return "Invalidní kočičk ID"
    return cat_data[0]["url"]


print(get_random_cat())