import os
import argparse

from Analyzer import filter_apart
from SheetManager import read_csv, export_csv

# Detect missing packages before any action is taken
import csv, requests, bs4

source_path = None
target_path = None
cancel = False

# Target folder will have trees.csv, shrubs.csv, vines.csv, and unknown.csv included
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", nargs=1, help="the file path of the source csv")  # Only accepts one argument (i.e. filename.csv)
parser.add_argument("-t", "--target", nargs=1, help="the file path of the target folder")  # Only accepts one argument (i.e. foldername)

args = parser.parse_args() # Parses with sys.argv by default, which is fine

# We can check whether the argument is passed by converting them to bool; they are a list when passed, so any string inside makes it True
if bool(args.source):
    # Source passed in command line
    source_path = args.source[0]
else:
    # Source not passed, request from user
    source_path = str(input("What is the file path of the source CSV spreadsheet? If file is not located in the same directory as this program, use the full path.\n[file path] > "))

if bool(args.target):
    # Target passed in command line
    target_path = args.target[0]
else:
    # Target not passed, request from user
    target_path = str(input("What is the file path of the target folder of CSV spreadsheets? A folder containing 4 resulting CSV documents will be created at the target path; enter folder name only to put it in this folder.\n[folder path] > "))

# Check the program inputs before utilizing them
if source_path.replace(" ", "") == "":
    # Source path is empty/whitespace (should only occur when using input())
    raise ValueError("Source file path cannot be empty.")
if target_path.replace(" ", "") == "":
    # Target path is empty/whitespace (same as above)
    raise ValueError("Target file path cannot be empty.")
if not os.path.isfile(source_path):
    # Source path is not a file or doesn't exist (only calls os.path.isfile(), meaning the path to a folder would raise this as well)
    raise FileNotFoundError("The document at the source path could not be found. (This could also mean the path led to a folder.)")
if os.path.isdir(target_path):
    # Target path points to an existing file, ask user before overwrite
    if str(input(f"A folder was detected at the target path '{target_path}'. Running this program will cause the output CSVs to be merged into the folder, which will overwrite files with the following names:\n- trees.csv\n- shrubs.csv\n- vines.csv\n- unknown.csv\nProceed anyway?\n[y/n] > ")).lower() in ("y", "yes"):
        print("--> Files will be added to target folder after filtering is complete. Pressing Ctrl+C (Windows/Linux) or \u2318+. (Mac) will halt the program during the filtering process, which prevents this.")
    else:
        cancel = True
        print("--> Operation skipped.")
        # The other errors should probably exit the program, but this one can just pass without processing the file if this is being run externally

if not cancel:
    print("Gathering data from source file...")
    csv_data_raw, common_names = read_csv(source_path) # Read and group the data from source CSV file
    print("Filtering species... (Species will appear below; this may take a while!)")
    csv_data_filtered = filter_apart(csv_data_raw) # Analyze and filter data
    print("Writing to target files...")
    export_csv(target_path, csv_data_filtered, common_names) # Save to target CSV files (overwrites files if already present)
    print("Done. The file 'unknown.csv' contains species whose type could not be determined automatically. Be sure to also double-check the accuracy of this program.")
