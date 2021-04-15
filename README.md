# iNaturalistCSVSpreadsheetCreator
This program takes a CSV generated from iNaturalist and formats it to a spreadsheet. Read README for instructions, and use at your own risk.

IT DOES NOT DO ALL THE WORK FOR YOU. YOU WILL STILL HAVE TO GO THROUGH MANUALLY AND DELETE THE NON-WOODY PLANTS THAT ARE MARKED AS FALSE POSITIVES

If you enounter any problems, you can email me at otter.kokinda@gmail.com, but the best way to reach me is through Discord at Panzerschwein#1162. If you message me there, I will probably resond within minutes. 

INSTRUCTIONS:

First of all, if you are comfortable using Python 3 and installing pip modules, do it that way. The three libraries you will have to install are "gspread", "bs4" and "csv". If you are not comfortable with Python, or never used Python before, I recommend using Repl.it. here is a link to the repl: https://replit.com/@Panzerschwein/iNaturalistSpreadSheetFormatter#main.py
There should be a blue button that says "fork" on the page when you go to the link. click it. (You may have to login in or create an account if you haven't already). 
If you have already finished with the rest of the steps in this README, click the 3 dots on the files tab, and choose "Upload files". Choose "client_secret.json" and your csv file that you extracted.
Lastly, select main.py, and hit Run at the top of the page. input the data when prompted in the termanil on the right side of the screen, and once the code finishes, your spreadsheet should be updated!


EXPORTING THE CSV FILE

To export the iNaturalist Data, go to https://www.inaturalist.org/observations/export.
Open another tab and pull up the Observation page for your park. I did Guerrero Park, so the URL looks like this: https://www.inaturalist.org/observations?place_id=144488&quality_grade=research&verifiable=any&view=species&iconic_taxa=Plantae
Notice the "place_id=" parameter in the URL string. Copy that parameter into the search bar(the one under "Create a Query" not the one that says "search" next to it) of the export page. For me, I would copy "place_id=144488".
Next, under quality grade, select "Research". For Captive / Cultivated, select "No". Leave everything else in the filter section the same. 
Under "Show only" select the plant leaf. It should be the 9th one. This will restrict the data to plants, which is what you want. 
If you scroll down to "Preview", the number should match the number of observations of plants in your park. For me, the number is "1-30 of 1541" and there are 1541 observations in my park
Now scroll down to Columns, and deselect everything in Basic and Geo. Under Taxon, the only two things that should be selected are "scientific_name" and "common_name". Nothing else needs to be selected. 
Hit "Create Export" and wait a minute or two as it creates your data. When it finishes, there should be a button to download it at the bottom of the page under "Recent Exports"
Download the zip folder and extract it. Inside, there should be a csv file. rename the file to something simple. I renamed mine to roy.csv, because my park is Roy G. Guerrero. 
Place that csv file in the same folder with the code and the json file (or just keep it in your download folder if you are using repl).


GETTING THE GOOGLE SHEETS API KEY

**Make sure you use a personal gmail for this section, as AustinISD restricts the Google Cloud Platform Service for student accounts**

This section has been having a lot of problems for some reason, I think Google has changed the way they manage their Cloud Dashboard, so if for some reason you are unable to complete this section, please message on Discord at Panzerschwein#1162 and I can give you a hand.

First you will have to create a Google Sheets API key. To do that you will have to create a new project at this link here: 
https://console.cloud.google.com/apis/dashboard
In the top left, click "New Project" and call it whatever you want.
Next, hit "Enable APIs and Services"
Search for Google Drive API, click it, then hit "Enable"
Go back to the dashboard (an easy way is to just repastw this link: https://console.cloud.google.com/apis/dashboard)
Then hit "Enable APIs and Services"
Search for Google Sheets API, click it, then hit "Enable"
Then, navigate to the "Credentials" tab on the sidebar and click "Create Credentials", and select "Help me choose"
Answer the following questions with the same answers as below:

**Which API are you using?**
Select "Google Sheets API"

**Where will you be calling the API from?**
Select "Web Server"

**What data will you be accessing?**
Select "Application Data"

**Are you planning to use this API with App Engine or Compute Engine?**
Select "No"

After answering those questions, click "What credentials do i need?" and fill out the the boxes.
For Service account name, I usually just put the name of my project, but you can call it whatever you want. 
Under "Role", click "Select a Role", then click "Project" then select "Editor"
The service account ID generates automatically based on the service account name, so you dont have to do anything for that. 
For Key Type, make sure JSON is selected. 
Hit "Continue"
It should then prompt you to download a json file, download it, and change the file name to "client_secret.json"
Put that json file in the same folder with the rest of the code (or keep it in your download folder if you are using repl).
Next, open up the json file with Notepad and look for the line, "client_email". Make sure to share the Google Sheets that you will be using to store your data with that email. 

FINAL STEPS:

Now, navigate to spreadsheetUpdate.py and change SPREADSHEET NAME to what ever your Google Spreadsheet is called in Google Drive. If your Google Spreadsheet is named "Plearth Data" the line should look like this: sh = gc.open("Plearth Data")


