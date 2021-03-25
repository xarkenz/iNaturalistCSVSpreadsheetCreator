import gspread
from webScraper import decodeCSV, decodeDescription
from spreadsheetUpdate import updateSheet, updateTreePurge
specificWorksheet = input("""What is the index of the worksheet that you want to write the data to?
(0 if its the first sheet on the spreadsheet, 1 if its the second and so on)
> """)
csvFile = input("""What is the name of the csv file that you want to read? (ex. bob.csv)
> """)
count, names = decodeCSV(csvFile)
updateSheet(count, specificWorksheet)
x = decodeDescription('roy_description.csv')
updateTreePurge(x)