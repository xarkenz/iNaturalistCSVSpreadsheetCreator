import gspread
from webScraper import decodeCSV
from spreadsheetUpdate import updateSheet
specificWorksheet = int(input("""What is the index of the worksheet that you want to write the data to?
(0 if its the first sheet on the spreadsheet, 1 if its the second and so on)
> """))
csvFile = input("""What is the name of the csv file that you want to read? (ex. bob.csv)
> """)
count, names = decodeCSV(csvFile)
updateSheet(count, specificWorksheet)
