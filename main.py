import sys
import os
from Analyzer import filter_woody_plants
from SheetManager import read_csv, export_csv

source_path = None
target_path = None
cancel = False

if len(sys.argv) == 1: # No additional arguments passed, request manual entry
    # Not necessary to catch type conflicts as input() should always return str (I hope)
    source_path = str(input("What is the file path of the source CSV spreadsheet? (If file is not located in the same directory as this program, use the full path.)\n[file path] > "))
    target_path = str(input("What is the file path of the target CSV spreadsheet? (The CSV output document will be created at the target path; full path recommended.)\n[file path] > "))
elif len(sys.argv) == 3: # Two arguments passed, they are checked later
    source_path, target_path = sys.argv[1], sys.argv[2] # sys.argv contains all relevant args from the python3 command, including called file name at 0
else: # Number of arguments passed in is not 0 or 2
    raise TypeError("Incorrect quantity of arguments provided. Usage: main.py | main.py <source> <target>")
    exit(1)

# Check the program inputs before utilizing them
if source_path.replace(" ", "") == "": # Source path is empty
    raise InputError("Source file path cannot be empty.")
    exit(1)
if target_path.replace(" ", "") == "": # Target path is empty
    raise InputError("Source file path cannot be empty.")
    exit(1)
if not os.path.isfile(source_path): # Source path is not a file or doesn't exist
    raise FileNotFoundError("The document at the source path could not be found. (This could also mean the path led to a folder.)")
    exit(1)
if os.path.isfile(target_path): # Target path points to an existing file
    if str(input(f"A file was detected at the target path '{target_path}'. Running this program will overwrite the file at this path. Proceed anyway?\n[y/n] > ")).lower() in ("y", "yes"):
        print("--> Target file will be overwritten after filtering is complete. Pressing Ctrl+C (Windows/Linux) or \u2318+. (Mac) to halt the program during the filtering process can prevent this.")
    else:
        cancel = True
        print("--> Operation cancelled.")

if not cancel:
    print("Gathering data from source file...")
    csv_data_raw = read_csv(source_path) # Read and group the data from source CSV file
    print("Filtering species... (Species will appear below; this may take a while!)")
    csv_data_filtered = filter_woody_plants(csv_data_raw) # Analyze and filter data
    print("Writing to target file...")
    export_csv(target_path, csv_data_filtered) # Save to target CSV file (overwrites file if already present)
    print("Done. If you are concerned about accuracy, be sure to check the output manually for false positives.")
