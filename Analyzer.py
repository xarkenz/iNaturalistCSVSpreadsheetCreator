import requests
from bs4 import BeautifulSoup

# NOTE: Wikipedia is not the most reliable resource for data, but it is reliable and comprehensive enough and has an API we can use for this

# These keywords are searched for in the Wikipedia page for each species/genus
vine_keywords = ["vine", "liana", "ivy"]
shrub_keywords = ["shrub", "bush"]
tree_keywords = ["tree", "lumber"]

# Filters a dictionary from a woody-filtered iNaturalist CSV into a list of 4 dictionaries: trees, shrubs, vines, unknown
def filter_apart(raw_data: dict):
    
    # Separate data sets for each category, will be converted to CSV later
    trees_data = {}
    shrubs_data = {}
    vines_data = {}
    unknown_data = {}

    try:
        for i, name in enumerate(raw_data.keys()):
            print(f"----------------\nSpecies {i+1}/{len(raw_data)}: {name} ({raw_data[name]})")
            
            name_format = name.replace(" ", "_")
            genus = name.split(" ")[0]

            # Wikipedia article for specific species is tested first
            print(f"Searching Wikipedia for '{name}'...")
            name_wiki_raw = requests.get(f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&titles={name_format}&redirects=")
            name_wiki = str(BeautifulSoup(name_wiki_raw.content, 'html.parser').get_text).lower()

            # Test each keyword against the content
            indexes = []
            for word in vine_keywords:
                if word in name_wiki:
                    indexes.append(name_wiki.find(word))
                    break
            else:
                indexes.append(99999)
            for word in shrub_keywords:
                if word in name_wiki:
                    indexes.append(name_wiki.find(word))
                    break
            else:
                indexes.append(99999)
            for word in tree_keywords:
                if word in name_wiki:
                    indexes.append(name_wiki.find(word))
                    break
            else:
                indexes.append(99999)
            
            # Determine which to add based on which appears first in the article; I couldn't think of a better way to do this
            if indexes[0] != 99999 or indexes[1] != 99999 or indexes[2] != 99999:
                index = indexes.index(min(indexes))
                if index == 0:
                    vines_data[name] = raw_data[name]
                    print("Verdict: VINE")
                elif index == 1:
                    shrubs_data[name] = raw_data[name]
                    print("Verdict: SHRUB")
                elif index == 2:
                    trees_data[name] = raw_data[name]
                    print("Verdict: TREE")
                else:  # Should not happen
                    unknown_data[name] = raw_data[name]
                    print("Verdict: UNKNOWN")
                continue
            
            # If the entry is just the genus, it only needs to be tested once; this means using species code for a genus, but the code works in the same way, at least for now
            if genus == name:
                unknown_data[name] = raw_data[name]
                print("Verdict: UNKNOWN")
                continue

            # No keywords were detected in the species article, meaning they either weren't present or the article for the particular species doesn't exist
            # If this is the case, test the article for the genus instead
            print(f"Searching Wikipedia for '{genus}'...")
            genus_wiki_raw = requests.get(f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&titles={genus}&redirects=")
            genus_wiki = str(BeautifulSoup(genus_wiki_raw.content, 'html.parser').get_text).lower()

            # Test each keyword against the content
            indexes = []
            for word in vine_keywords:
                if word in genus_wiki:
                    indexes.append(genus_wiki.find(word))
                    break
            else:
                indexes.append(99999)
            for word in shrub_keywords:
                if word in genus_wiki:
                    indexes.append(genus_wiki.find(word))
                    break
            else:
                indexes.append(99999)
            for word in tree_keywords:
                if word in genus_wiki:
                    indexes.append(genus_wiki.find(word))
                    break
            else:
                indexes.append(99999)
            
            # Determine which to add based on which appears first in the article
            if indexes[0] != 99999 or indexes[1] != 99999 or indexes[2] != 99999:
                index = indexes.index(min(indexes))
                if index == 0:
                    vines_data[name] = raw_data[name]
                    print("Verdict: VINE")
                elif index == 1:
                    shrubs_data[name] = raw_data[name]
                    print("Verdict: SHRUB")
                elif index == 2:
                    trees_data[name] = raw_data[name]
                    print("Verdict: TREE")
                else:  # Should not happen
                    unknown_data[name] = raw_data[name]
                    print("Verdict: UNKNOWN")
                continue
            else:
                unknown_data[name] = raw_data[name]
                print("Verdict: UNKNOWN")
        
        print("================")

        return [trees_data, shrubs_data, vines_data, unknown_data]
    except KeyboardInterrupt:
        print("================\nProgram halted manually. Exiting.")
        exit()
