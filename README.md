# iNaturalistWoodyPlantFilter

This program is a fork of Panzerschwein's iNaturalistCSVSpreadsheetCreator, and aims to filter through a CSV of plants documented in iNaturalist to remove the plants that are not considered woody. Read `README.md` (this document) for instructions, and use at your own risk. Do note that some of the steps may be confusing. If you find something confusing, feel free to contact me (info below) with any questions you have, so I can help and/or clarify.

There is one major difference between the original project and this fork; this fork generates a CSV output file whereas the original outputs directly onto a Google Sheet. I would recommend using the one that is more convenient for your purposes. The code is also reworked in most areas to look/run smoother, but a lot of the credit for the original code goes to Panzerschwein.

**PLEASE NOTE THAT THIS PROGRAM IS NOT 100% ACCURATE AND OFTEN CONTAINS SOME FALSE POSITIVES.** While you may still have to manually sort through the result CSV if it is a concern, this program can greatly reduce the amount of non-woody plants in the CSV file.

I have also not tested this program using [repl.it](https://replit.com/), although I would imagine it is possible. Please let me know whether you are able to get it working so I can add it to the instructions here.

If you encounter any problems or have any suggestions, I respond to emails at seanedwardsclarke@gmail.com and am also active on Discord at `xarkenz#6200`; feel free to reach out.

## Exporting the CSV File From iNaturalist

These instructions are for gathering data from a park with boundaries included in iNaturalist. These steps are the same as in iNaturalistCSVSpreadsheetCreator. **If you already have a CSV file, proceed to the Program Instructions.**

1. Find the Observation page in iNaturalist for the park you chose.
2. Copy the part of the URL of this page that looks like `place_id=123456`. For example, in the URL `https://www.inaturalist.org/observations?place_id=123456&quality_grade=research&verifiable=any&view=species&iconic_taxa=Plantae`, `place_id=123456` would be the text to copy.
3. Go to https://www.inaturalist.org/observations/export.
4. Under "Create a Query", there should be an input bar that is meant for query parameters. Paste the text you copied into this input bar.
5. Next to Quality Grade (middle of "Filter" area), select "Research". This returns only results that classify as research-grade.
6. Next to Captive / Cultivated (right side of "Filter" area), select "No". This returns only results that are considered wild.
7. In the "Show only" area, select the leaf for plants, which should be between insects and fungi. This returns only results that are plants.
8. Leave all parameters not mentioned at their default values. Below the "Create a Query" section is the "Preview" section. You can check your filter work here to make sure that you will get results and that they the type of results you want.
9. In the "Choose columns" section, a large amount of the boxes are actually checked. To get the right data, make sure to deselect *every* checkbox (the "All | None" control should help) in **all** column sections **except** `scientific_name` and `common_name` in the Taxon section. These are the only two columns that should be enabled.
10. After following all above steps as closely as possible, press the "Create Export" button in the next section. The amount of time it takes to load the data may vary, but it usually does not take very long with reasonably sized parks.
11. After it finishes creating the export, go to the very bottom of the page and find the "Recent Exports" section. The data from your park should be located in this section. Once you find it, press the "Download" button and save the ZIP file somewhere; the filename can remain the same. If you need to pick from multiple recent exports, the timestamps near the left side should help identify the correct export to download.
12. Extract the ZIP file you downloaded and rename the CSV file contained within to some name that is descriptive and easy to type, such as the abbreviated park name. For example, a CSV for the park Roy G. Guerrero could be named `roy.csv`. Keeping `.csv` on the end of the filename is highly recommended. (I also recommend retaining the original ZIP file in case something goes wrong.)
13. Add the file to the folder containing the `main.py` program. After that, the program is ready to run. Refer to the section **Program Instructions** for details on how to proceed.

## Program Instructions

**Usage**
It is recommended that quotation marks be used around each argument after the identifier. (e.g. `-s "file.csv"`)
```
usage: main.py [-h] [-s SOURCE] [-t TARGET] [-x TAXON [TAXON ...]]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        the file path of the source csv
  -t TARGET, --target TARGET
                        the file path of the target csv
  -x TAXON [TAXON ...], --exclude TAXON [TAXON ...]
                        species/genera to exclude
```

This fork does not use the Google API. The modules that needs to be present for this fork to function properly are BeautifulSoup (`bs4`), `argparse`, `csv`, `requests`, and `os`. Some of these are already part of the native Python environment.

A CSV file (`source`) should be obtained from the the section **Exporting the CSV File From iNaturalist**; the filename should be easy to type, as mentioned. Just in case, make sure to keep a copy of that file handy. While you can put the file anywhere if you use the full file path, it is most convenient to add the file to this folder so the filename can be used alone. The `target` file, on the other hand, is the destination where the output file will go from this program. The name of the target file can be set to any name, but it is recommended not to use an existing filename. If you input a filename only, the output will be created in this folder, but a full file path can be used if the destination is located elsewhere. *Warning: If a file already exists at the target path, this file will be overwritten with the output data! (The program will provide this warning if this is the case.)*

The next step after the source and target files are prepared and BeautifulSoup is installed is to execute the program. First, open up the command line (Windows: `cmd.exe`; Mac/Linux: `terminal`) and use the `cd` command to [navigate to this folder](https://ss64.com/nt/cd.html). In some operating systems, you can alternatively second-click on this folder in a file manager and open it in the command line.

When you are inside this folder, shown by the folder path to the left of the cursor, you can then enter the command according to the **Usage** syntax above. The `--help` option shows help for the program. The other three options, `--source`, `--target`, and `--exclude`, are optional, but if they are not present, the program will request manual entry. `--exclude` is not a required argument and can be skipped in the program.

To exclude one or more species, the optional argument `--exclude` can be used. To use this argument, enter a comma-separated list surrounded by quotation marks (spacing should not matter) where each item of the list is a scientific name/species (`Genus species`) or a genus (`Genus`). (e.g. `-x "Opuntia engelmannii, Quercus, Toxicodendron radicans"`) The items from this list will override the filter for these particular taxon so they are not included in the output. Higher-level taxa cannot be used to exclude species.

**NOTE:** The program can be manually stopped at any time without making any changes via a keyboard interrupt (Windows/Linux: `Ctrl`+`C`; Mac: &#8984;+`.`).

After the program says it is done and exits, you should be able to find a new CSV file at the target path. This is the output CSV, which is organized and filtered. It has 3 columns and one row for each species. The first row is a header which describes the data below. If needed, the CSV can be converted to a spreadsheet format or imported into Google Sheets, for example. You are now done with this process, but remember: there likely exist false positives in the data output of this program, so if that is an issue, you may need to manually skim through the data yourself. However, individuals of the same species are grouped together, and along with the filtering of the data, the number of species to check is vastly reduced.
