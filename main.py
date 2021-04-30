import os
import argparse

from Analyzer import filter_woody_plants
from SheetManager import read_csv, export_csv

# Detect missing packages before any action is taken
import csv, requests, bs4

source_path = None
target_path = None
exclude_list = []
cancel = False

# The argparse module is very helpful in this program, and the way it's set up allows source and target to be individually optional, which is different from when I was using sys.argv
# The only reason I wanted to include argparse originally was to add --exclude and to have it feel native, but it changed how source and target are written
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", nargs=1, help="the file path of the source csv") # Only accepts one argument
parser.add_argument("-t", "--target", nargs=1, help="the file path of the target csv") # Only accepts one argument
parser.add_argument("-x", "--exclude", action="extend", nargs="+", type=str, metavar="TAXON", help="taxa to exclude") # Doesn't have a limit on taxon excludes, they will be iterated anyway

args = parser.parse_args() # Parses with sys.argv by default, which is fine

if bool(args.exclude):
    # Excludes are passed
    for taxon in args.exclude:
        # Supports extra arguments, comma separation, or a combination of the two
        # Removes leading and trailing whitespace, which makes comma separation more flexible
        exclude_list += [x.strip() for x in str(taxon).split(",")]
else:
    # No excludes passed, ask user
    raw_exclude = str(input("What, if any, taxa (genus or species) should be excluded from the filtered list? Leave blank if none. (e.g. > Genus1 Species1, Genus2, [...])\n[list] > "))
    if raw_exclude.replace(" ", "") != "":
        # Almost the same as what is done above except with only one str
        exclude_list += [x.strip() for x in raw_exclude.split(",")]

# Remove useless strings created during comma separation (usually not needed)
exclude_list = [x for x in exclude_list if x != ""]

# NOTE: It's not a big deal if a taxon is misspelled, it just won't filter anything; the user will be notified of this at the end.

# We can check whether the argument is passed by converting them to bool; they are a list when passed, so any string inside makes it True
if bool(args.source):
    # Source passed in command line
    source_path = args.source[0]
else:
    # Source not passed, request from user
    source_path = str(input("What is the file path of the source CSV spreadsheet? (If file is not located in the same directory as this program, use the full path.)\n[file path] > "))

if bool(args.target):
    # Target passed in command line
    target_path = args.target[0]
else:
    # Target not passed, request from user
    target_path = str(input("What is the file path of the target CSV spreadsheet? (The CSV output document will be created at the target path; enter filename only to put it in this folder.)\n[file path] > "))

# Check the program inputs before utilizing them
if source_path.replace(" ", "") == "":
    # Source path is empty/whitespace (should only occur when using input())
    raise InputError("Source file path cannot be empty.")
    exit(1)
if target_path.replace(" ", "") == "":
    # Target path is empty/whitespace (same as above)
    raise InputError("Target file path cannot be empty.")
    exit(1)
if not os.path.isfile(source_path):
    # Source path is not a file or doesn't exist (only calls os.path.isfile(), meaning the path to a folder would raise this as well)
    raise FileNotFoundError("The document at the source path could not be found. (This could also mean the path led to a folder.)")
    exit(1)
if os.path.isfile(target_path):
    # Target path points to an existing file, ask user before overwrite (doesn't matter if there is a folder with the same name, though)
    if str(input(f"A file was detected at the target path '{target_path}'. Running this program will overwrite the file at this path. Proceed anyway?\n[y/n] > ")).lower() in ("y", "yes"):
        print("--> Target file will be overwritten after filtering is complete. Pressing Ctrl+C (Windows/Linux) or \u2318+. (Mac) to halt the program during the filtering process can prevent this.")
    else:
        cancel = True
        print("--> Operation skipped.")
        # The other errors should probably exit the program, but this one can just pass without processing the file if this is being run externally

if not cancel:
    #print(f"finish program with source '{source_path}', target '{target_path}' and excluding {exclude_list}")
    print("Gathering data from source file...")
    csv_data_raw = read_csv(source_path) # Read and group the data from source CSV file
    print("Filtering species... (Species will appear below; this may take a while!)")
    csv_data_filtered = filter_woody_plants(csv_data_raw, exclude_list) # Analyze and filter data
    print("Writing to target file...")
    export_csv(target_path, csv_data_filtered) # Save to target CSV file (overwrites file if already present)
    print("Done. If you are concerned about accuracy, be sure to check the output manually for false positives.")
