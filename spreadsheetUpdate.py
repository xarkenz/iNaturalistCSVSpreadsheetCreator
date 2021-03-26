import gspread

gc = gspread.service_account(filename='client_secret.json')
sh = gc.open("SPREADSHEET NAME")
def updateSheet(speciesCount, parkName):
    count = 6
    countList = []
    parkSheet = sh.get_worksheet(parkName)

    for i in speciesCount:
        countNameTuple = [speciesCount[i][1], i, speciesCount[i][0]]
        countList.append(countNameTuple)
        count = count +1
    placing = str('A6:C' + str(count))
    parkSheet.update(placing, countList)


