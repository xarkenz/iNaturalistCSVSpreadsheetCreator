import csv
import requests
from bs4 import BeautifulSoup

keywords = ["shrub", "tree", " liana", "liana ", "wood", "vine", "bush", "lumber"]

def filter_woody_plants(raw_data):
    final_data = {}
    for i, name in enumerate(raw_data.keys()):
        name_format = name.replace(" ", "_")
        genus = name.split(" ")[0]
        print(f"--------\nSpecies {i}/{len(raw_data)} ({name}):")
        print(f"Searching Wikipedia for '{name}'...")
        name_wiki_raw = requests.get(f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&titles={name_format}&redirects=")
        name_wiki = str(BeautifulSoup(name_wiki_raw.content, 'html.parser').get_text).lower()
        for word in keywords:
            if word in name_wiki:
                final_data[name] = raw_data[name]
                print("Possibly woody.")
                break
        else:
            print(f"Searching Wikipedia for '{genus}'...")
            genus_wiki_raw = requests.get(f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&titles={genus}&redirects=")
            genus_wiki = str(BeautifulSoup(genus_wiki_raw.content, 'html.parser').get_text).lower()
            for word in keywords:
                if word in genus_wiki:
                    final_data[name] = raw_data[name]
                    print("Possibly woody.")
                    break
            else:
                print("No match found.")

    return final_data
