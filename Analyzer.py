import requests
from bs4 import BeautifulSoup

# NOTE: Wikipedia is not the most reliable resource for data, but it is reliable and comprehensive enough and has an API we can use.

# These keywords are searched for in the Wikipedia page for each species/genus
keywords = ["shrub", "tree", "liana", "wood", "vine", "bush", "lumber"]

# Filters a dictionary from an iNaturalist CSV to return a dictionary without the non-woody plants
def filter_woody_plants(raw_data:dict, excludes:list=[]):
    
    final_data = {} # The output will be stored here
    num_species = len(raw_data) # May save time with longer data sets
    excludes_uses = [0] * len(excludes)
    try:
        for i, name in enumerate(raw_data.keys()):
            print(f"----------------\nSpecies {i}/{num_species}: {name} ({raw_data[name][0]})")
            # Test against excludes (case sensitive to differentiate species/genus)
            use = True
            for i, exclude in enumerate(excludes):
                if exclude in name:
                    use = False
                    excludes_uses[i] += 1
            if use:
                # Filter the species
                name_format = name.replace(" ", "_")
                genus = name.split(" ")[0]
                # Wikipedia article for specific species is tested first
                print(f"Searching Wikipedia for '{name}'...")
                # Get the content of the Wikipedia page for the species
                name_wiki_raw = requests.get(f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&titles={name_format}&redirects=")
                name_wiki = str(BeautifulSoup(name_wiki_raw.content, 'html.parser').get_text).lower()
                # Test each keyword against the content
                for word in keywords:
                    if word in name_wiki:
                        final_data[name] = raw_data[name]
                        print("Verdict: WOODY")
                        break # Further testing not necessary
                else:
                    # If the entry is just the genus, it only needs to be tested once; this means using species code for a genus but they are the same, thankfully
                    if genus != name:
                        # No keywords were detected in the species article, meaning they either weren't present or the article for the particular species doesn't exist
                        # If this is the case, test the article for the genus
                        print(f"Searching Wikipedia for '{genus}'...")
                        # Get the content of the Wikipedia page for the genus
                        genus_wiki_raw = requests.get(f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&titles={genus}&redirects=")
                        genus_wiki = str(BeautifulSoup(genus_wiki_raw.content, 'html.parser').get_text).lower()
                        # Test each keyword against the content
                        for word in keywords:
                            if word in genus_wiki:
                                final_data[name] = raw_data[name]
                                print("Verdict: WOODY")
                                break # Further testing not necessary
                        else:
                            # Most likely not woody (could rarely miss some woody plants)
                            print("Verdict: NON-WOODY")
                    else:
                        # Tested once; genus only
                        print("Verdict: NON-WOODY")
            else:
                print("Verdict: EXCLUDE")
        
        if len(excludes) != 0:
            # Give some feedback on what was excluded
            print("================\nExclusion terms used (0 uses could indicate a typo or lack of necessity):\n  " + "\n  ".join([f"'{excludes[i]}': {excludes_uses[i]}" for i in range(len(excludes))]))
        else:
            print("================")

        return final_data
    except KeyboardInterrupt:
        print("================\nProgram halted manually. Exiting.")
        exit()
