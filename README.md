# iNaturalistCSVSpreadsheetCreator
This program takes a CSV generated from iNaturalist and formats it to a spreadsheet. Read README for instructions.

Instructions:

Exporting the CSV File:

To export the iNaturalist Data, go to https://www.inaturalist.org/observations/export.
Open another tab and pull up the Observation page for your park. I did Guerrero Park, so the URL looks like this: https://www.inaturalist.org/observations?place_id=144488&quality_grade=research&verifiable=any&view=species&iconic_taxa=Plantae
Notice the "place_id=" parameter in the URL string. Copy that parameter into the search bar of the export page. For me, I would copy "place_id=144488".
Next, under quality grade, select "Research". For Captive / Cultivated, select "No". Leave everything else in the filter section the same. 
Under "Show only" select the plant leaf. It should be the 9th one. This will restrict the data to plants, which is what you want. 
If you scroll down to "Preview", the number should match the number of observations of plants in your park. For me, the number is "1-30 of 1541" and there are 1541 observations in my park
Now scroll down to Columns, and deselect everything in Basic and Geo. Under Taxon, the only two things that should be selected are "scientific_name" and "common_name". Nothing else needs to be selected. 
Hit "Create Export" and wait a minute or two as it creates your data. When it finishes, there should be a button to download it at the bottom of the page under "Recent Exports"
Download the zip folder and extract it. Inside, there should be a csv file. rename the file to something simple. I renamed mine to roy.csv, because my park is Roy G. Guerrero. 
Place that csv file in the same folder with the code and the json file. 


Getting the Google Sheets API Key

First you will have to create a Google Sheets API key. To do that you will have to create a new project at this link here: https://console.cloud.google.com/apis/api/drive.googleapis.com
In the top left, click "New Project" and call it whatever you want.
Next, hit "Enable APIs and Services"
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
Put that json file in the same folder with the rest of the code.
Next, open up the json file with Notepad and look for the line, "client_email". Make sure to share the Google Sheets that you will be using to store your data with that email. 
Now, navigate to spreadsheetUpdate.py and change SPREADSHEET NAME to what ever your spreadsheet is called in Google Drive. If your spreadsheet is named "Plearth Data" the line should look like this: sh = gc.open("Plearth Data")


