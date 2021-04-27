# iNaturalistWoodyPlantFilter
This program is based on Panzerschwein's iNaturalistCSVSpreadsheetCreator, and filters a CSV file of iNaturalist plants to reduce the number of non-woody plants present. Read README for instructions, and use at your own risk.

IF ACCURACY IS NEEDED, THIS PROGRAM DOES NOT PROVIDE PERFECT ACCURACY AND MAY CONTAIN FALSE POSITIVES. While you will still have to manually sort through the result CSV, this program can greatly reduce the amount of non-woody plants in the CSV file.

There is one major difference between the original project and this fork; this fork generates a CSV output file whereas the original outputs directly onto a Google Sheet. I would recommend using the one that is more convenient for your purposes.

I have also not tested this program using repl.it, although I would imagine it is possible. Please let me know if you are able to get it working so I can add it to the instructions here.

If you enounter any problems, I respond to emails at seanedwardsclarke@gmail.com and am also active on Discord at xarkenz#6200; feel free to reach out.

**PROGRAM INSTRUCTIONS**

You do not need to use the Google API for this fork.

Usage (may be different depending on OS): `main.py` | `main.py <source> <target>`

The only module that should need to be installed for this fork is BeautifulSoup (`bs4`). `csv` and `requests` are also needed but they should already be built into the Python environment.

To filter the CSV file obtained through the step **Exporting the CSV File From iNaturalist**, I suggest keeping a copy elsewhere in case something goes wrong. Then, I would recommend putting one of the copies into the folder that contains `main.py`. This will be your source file. Your target file does not need to exist yet, as the program will create it, and it will also overwrite any file that already exists at the target path. The program can now be executed, preferably through a command line or a similar environment to show errors and output, using the syntax above. *Note: Both the source path and target path are required, so the program will let you enter them manually if they are not provided as command line arguments.*

If necessary, you can then take this resulting CSV file and import it to Google Sheets. Keep in mind that the first line is the header line.

**EXPORTING THE CSV FILE FROM INATURALIST**

Source CSV files are used in the same way from the original project to this fork, so the same instructions can be followed:

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
