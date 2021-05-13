import csv
from os import mkdir

def read_csv(read_path: str):
    # Import and group the CSV file
    data = {}
    common_names = {}
    with open(read_path, "r") as f:
        read_file = csv.reader(f)
        for row in read_file:
            if len(row) == 2:
                if row[0].lower() in ["scientific_name", "scientific name"]:
                    if row[1].lower() != "count":
                        raise ValueError("CSV columns are improperly formatted. See README.md for instructions.")
                    # Ignore the header row, we will add it back in the export step
                    continue
                elif row[0] in data:
                    # If we already have the species, we can just combine
                    data[row[0]] += int(row[1])
                else:
                    # Create an entry for the species if it doesn't exist
                    data[row[0]] = int(row[1])
            elif len(row) == 3:
                if row[1] in ["scientific_name", "Scientific Name"]:
                    if row[2].lower() != "count" or row[0].lower() not in ["common_name", "common name"]:
                        raise ValueError("CSV columns are improperly formatted. See README.md for instructions.")
                    # Ignore the header row, we will add it back in the export step
                    continue
                elif row[1] in data:
                    # If we already have the species, we can just combine
                    data[row[1]] += int(row[2])
                else:
                    # Create an entry for the species if it doesn't exist
                    data[row[1]] = int(row[2])
                    common_names[row[1]] = row[0]
        return (data, common_names)

def export_csv(write_path: str, csv_data: list, common_names: dict = {}):
    # Export the filtered CSV files
    if write_path.endswith("/"):
        write_path = write_path[:-1]
    
    try:
        mkdir(write_path)
    except FileExistsError:
        # User would have already been warned of this fact
        pass
    
    filenames = ["trees.csv", "shrubs.csv", "vines.csv", "unknown.csv"]
    for i in range(len(filenames)):
        with open(write_path + "/" + filenames[i], "w") as f:
            write_file = csv.writer(f, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
            if len(common_names) > 0:
                write_file.writerow(["Common Name", "Scientific Name", "Count"])
                for species in csv_data[i].keys():
                    write_file.writerow([common_names[species], species, str(csv_data[i][species])])  # Line order: common_name, scientific_name, count
            else:
                write_file.writerow(["Scientific Name", "Count"])
                for species in csv_data[i].keys():
                    write_file.writerow([species, str(csv_data[i][species])])  # Line order: scientific_name, count
