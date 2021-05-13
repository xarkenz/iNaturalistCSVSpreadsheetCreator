# iNaturalistWoodyPlantFilter-separator

This program is a branch of iNaturalistWoodyPlantFilter, and aims to split a pre-filtered input CSV spreadsheet into trees, shrubs, and vines. Read `README.md` (this document) for instructions, and use at your own risk. Do note that some of the steps may be confusing. If you find something confusing, feel free to contact me (info below) with any questions you have so I can help and/or clarify.

The structure and usage of this program is very similar to iNaturalistWoodyPlantFilter, with a few differences that can be seen through the **Program Instructions**.

**PLEASE NOTE THAT THIS PROGRAM IS NOT 100% ACCURATE AND MAY CONTAIN SOME FALSE POSITIVES.** However, most of the unknown plants will go into a separate CSV to be sorted by hand.

If you encounter any problems or have any suggestions or questions, I respond to emails at seanedwardsclarke@gmail.com and am also active on Discord at `xarkenz#6200`; feel free to reach out.

## Program Instructions

**Usage**
It is recommended that quotation marks be used around each argument after the identifier. (e.g. `-s "file.csv"`)
```
usage: main.py [-h] [-s SOURCE] [-t TARGET]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        the file path of the source csv
  -t TARGET, --target TARGET
                        the file path of the target folder
```

The modules needed for this are exactly the same as those needed in iNaturalistWoodyPlantFilter. You will need BeautifulSoup (`bs4`), `argparse`, `csv`, `requests`, and `os`. Some of these are already part of the native Python environment. You should be able to use repl.it for this tool if desired, simply keeping all relevant files in the working folder.

A CSV file (`source`) should be obtained from iNaturalistWoodyPlantFilter or from a spreadsheet filtered by hand; make sure the filename is easy to type. Just in case, make sure to keep a copy of that file handy. While you can put the file anywhere if you use the full file path, it is most convenient to add the file to the program folder so the filename can be used alone (e.g. `some_park.csv`). __The `target` argument is going to be the path of a destination folder rather than a destination file (which is how it is in iNaturalistWoodyPlantFilter).__ The name of the target folder can be set to any name, but it is recommended that it be unique from any existing folder. If you input a filename only, the target folder will be created in the program directory, but a full file path can be used if the destination is located elsewhere. *Warning: If a folder already exists at the target path, the output of this program will be merged with the existing folder, possibly overwriting files! (The program will provide a warning if this is the case.)*

**NOTE:** The folder created by the program (`target`) will contain 4 CSV files: `trees.csv`, `shrubs.csv`, `vines.csv`, and `unknown.csv`.

The next step after the source file and target folder are prepared and the required modules are installed is to execute the program. First, open up the command line (Windows: `cmd.exe`; Mac/Linux: `terminal`) and use the `cd` command to [navigate to this folder](https://ss64.com/nt/cd.html). In some operating systems, you can alternatively secondary-click on this folder in a file manager and open it in the command line from that menu. For repl.it users, you will already be inside the main folder, so this is not a concern.

When you are inside this folder, shown by the folder path to the left of the cursor, you can then enter the command according to the **Usage** syntax above. The `--help` option shows the help for the program. The other two options, `--source` and `--target`, are optional, but if they are not present, the program will request manual entry.

**NOTE:** The program can be manually stopped at any time without making any changes via a keyboard interrupt (Windows/Linux: `Ctrl`+`C`; Mac: &#8984;+`.`).

After the program reports that it is done and exits, you should be able to find the folder with 4 named CSVs at the target path, as noted above. These are the output CSVs, each of which holds one type of plant. Each CSV has 2 or 3 columns (depending on how many are in `source`) and one row for each unique species. The first row is a header which describes the data below. If needed, the CSV can be converted to a spreadsheet format or imported into Google Sheets, for example. You are now done with this process, but remember: it's a good idea to manually sort the species that are found in `unknown.csv`, as they could either be one of the types desired or not a woody plant at all.
