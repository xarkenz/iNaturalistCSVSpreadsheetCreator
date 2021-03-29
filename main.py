import gspread
from bs4 import BeautifulSoup
import requests
from webScraper import decodeCSV, crossReference
from spreadsheetUpdate import updateSheet
specificWorksheet = int(input("""What is the index of the worksheet that you want to write the data to?
(0 if its the first sheet on the spreadsheet, 1 if its the second and so on) Put 0 if you haven't created any more worksheets in your Google Sheet
> """))
csvFile = input("""What is the name of the csv file that you want to read? (ex. bob.csv)
> """)
count = decodeCSV(csvFile)
enable = input("""Would you like to enable Sorting Mode? (y/n) Sorting mode will automatically eliminate plants that are not woody plants, and leave you with a smaller dataset to go through.
> """)
if enable.lower() == 'y' or enable.lower() == 'yes':
    count = crossReference(count)

updateSheet(count, specificWorksheet)
