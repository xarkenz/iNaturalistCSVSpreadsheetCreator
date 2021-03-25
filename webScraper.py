import csv
def decodeCSV(csvFile):
    uniqueCount = {}
    normalName = {}
    f = open(csvFile)
    csv_f = csv.reader(f)
    for row in csv_f:
        print(row)
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
