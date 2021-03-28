import csv
from bs4 import BeautifulSoup
import requests
def decodeCSV(csvFile):
    uniqueCount = {}
    normalName = {}
    f = open(csvFile)
    csv_f = csv.reader(f)
    for row in csv_f:
        normalName[row[0]] = row[1]
        if row[0] in uniqueCount:
            #uniqueCount[row[0]] = uniqueCount[row[0]][0] + 1
            tuple1 = uniqueCount[row[0]]
            x = tuple1[0]
            y = tuple1[1]
            x = x+1
            a = (x,y)
            uniqueCount[row[0]] = a
        else:
            uniqueCount[row[0]] = (1, row[1])
    return uniqueCount, normalName

def crossReference(uniqueCount):
    updatedDict = {}
    count = 1
    length = len(uniqueCount)
    for i in uniqueCount:
        nameList = i.split()
        underscored = i.replace(" ", "_")
        print(underscored)
        print(str(count)+'/'+str(length))
        single = nameList[0]
        print(single)
        count = count + 1
        wikiLink = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&titles='+underscored+'&redirects='
        r = requests.get(wikiLink)
        soup = BeautifulSoup(r.content, 'html.parser')
        x = str(soup.get_text)
        x = x.lower()
        if 'shrub' in x or 'tree' in x or ' liana' in x or 'shrub' in x or 'tree' in x or 'liana ' in x or 'woody' in x or 'vine' in x or 'bush' in x:
            updatedDict[i] = uniqueCount[i]
        else:
            link2 = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&titles=' + single + '&redirects='
            r2 = requests.get(link2)
            soup2 = BeautifulSoup(r2.content, 'html.parser')
            y = str(soup2.get_text)
            y = y.lower()
            if 'shrub' in y or 'tree' in y or ' liana' in y or 'shrub' in y or 'tree' in y or 'liana ' in y or 'woody' in y or 'vine' in y or 'bush' in y:
                updatedDict[i] = uniqueCount[i]
                print(True)


    return updatedDict
