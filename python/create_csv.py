import get_data as get_data
import os
import sys
import csv
import timestamp as timestamp
from datetime import datetime
import check_file as check_file


# Ensure the pattern ends with a slash for consistent comparison
PATTERN =  "/Users/A200298519/Downloads/Test/"
csv_path =  os.path.expanduser('~/Desktop')+ '/Analysis.csv'

last_date_processed = None

def check_folder():
    print("Checking folder \n")
    data_list = get_data.get_data()
    data_csv =[]
    date_today = datetime.now().strftime("%Y-%m-%d")
    for index, data in enumerate(data_list, start=1):
        folder_name, time_stamp, file_size, site_url, tab_url, mime_type = data
        print("Folder_name", folder_name)
        normalized_folder_name = os.path.join(folder_name, '')
        if normalized_folder_name.startswith(PATTERN):
            # print(f"Match found in folder {folder_name}")a
            # Add this data to the CSV file
            file_name = os.path.basename(folder_name)
            # print(file_name)
            real_time = timestamp.timestamp_converter(time_stamp)
            real_bytes = timestamp.bytes_to_mb(file_size)
            valid = check_file.file_validate(file_name)
            if valid:
                data_csv.append([file_name, "0" ,real_time, real_bytes, folder_name, tab_url, mime_type])
            else:
                data_csv.append([file_name, "1" ,real_time, real_bytes, folder_name, tab_url, mime_type])

    print(data_csv)
    add_data_to_csv(data_csv, date_today)


def add_data_to_csv(data_csv, date_today):
    print("Adding data to csv \n")
    global last_date_processed
    file_exists = os.path.isfile(csv_path)
    deleted = []
    with open(csv_path, mode='a', newline='') as file:

        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            # Write the header only if it's the first write operation or if it's a new day
        if not file_exists or date_today != last_date_processed:
            writer.writerow(['File Name', 'Deleted', 'Time', 'File Size (MB)', 'Folder Name', 'Tab URL', 'MIME Type'])
        # Check if the date has changed since the last data entry
        if date_today != last_date_processed:
            # This section writes the date row only when the date changes
            writer.writerow([])  # Optionally add a blank row for visual separation
            writer.writerow([date_today])  # Date row
            writer.writerow([])  # Optionally add a blank row for visual separation
            last_date_processed = date_today
        # Write data
        writer.writerow([])  # Optionally add a blank row for visual separation
        writer.writerow(["Downloaded Files"])
        writer.writerow([])
        for data in data_csv:
            if data[1] == "0":
                writer.writerow(data)
            else:
                deleted.append(data)
        writer.writerow([])  # Optionally add a blank row for visual separation
        writer.writerow(["Deleted Files"])
        writer.writerow([])
        for data in deleted:
            writer.writerow(data)
        writer.writerow([])  # Optionally add a blank row for visual separation
        writer.writerow(["--------------------------------------------------------"])




# match_folder()
check_folder()

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_folder":
            check_folder()
        else:
            print("Unknown command")
    else:
        print("No command provided")

if __name__ == "__main__":
    main()
