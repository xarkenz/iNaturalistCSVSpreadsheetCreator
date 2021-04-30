import csv

def read_csv(read_path:str):
    # Import and group the CSV file
    data = {}
    with open(read_path, "r") as f:
        read_file = csv.reader(f)
        for row in read_file:
            if row[0] == "scientific_name":
                # Ignore the header row, we will add it back in the export step
                continue
            elif row[0] in data:
                # If we already have the species, we can just increment the number
                data[row[0]][0] += 1
            else:
                # Create an entry for the species if it doesn't exist
                data[row[0]] = [1, row[1]]
        return data

def export_csv(write_path:str, csv_data:dict):
    # Export the filtered CSV file
    with open(write_path, "w") as f:
        write_file = csv.writer(f, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL) # Options might not be necessary but it can't hurt
        write_file.writerow(["Common Name", "Scientific Name", "Count"]) # Insert a more descriptive header row since we removed it while grouping
        for species in csv_data.keys():
            write_file.writerow([csv_data[species][1], species, str(csv_data[species][0])]) # Line order: common_name, scientific_name, count
