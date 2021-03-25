import gspread

gc = gspread.service_account(filename='client_secret.json')
sh = gc.open("SPREADSHEET NAME")
def updateSheet(speciesCount, parkName):
    count = 6
    countList = []
    parkSheet = parkName

    for i in speciesCount:
        countNameTuple = [speciesCount[i][1], i, speciesCount[i][0]]
        countList.append(countNameTuple)
        count = count +1
    placing = str('A6:C' + str(count))
    parkSheet.update(placing, countList)

def updateTreePurge(speciesCount):
    count = 6
    countList = []
    parkSheet = sh.get_worksheet(2)


    for i in speciesCount:
        if 'tree' in speciesCount[i][0] or 'shrub' in speciesCount[i][0]:
            countNameTuple = [speciesCount[i][2], i, speciesCount[i][1]]
            countList.append(countNameTuple)
        else:
            print(False)
        count = count +1
    placing = str('A6:C' + str(count))
    parkSheet.update(placing, countList)


