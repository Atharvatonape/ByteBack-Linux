import get_data
from dotenv import load_dotenv
import os
import re
import csv
import timestamp

load_dotenv()

# Ensure the pattern ends with a slash for consistent comparison
PATTERN = os.path.join(os.getenv("UNIQUE_TEST_FOLDER", ""), '')
csv_path =  os.path.expanduser('~/Desktop')+ '/Analysis.csv'

def add_data_to_csv(data):
    """
    Adds data to a CSV file, creating the file if it doesn't exist.
    """
    file_exists = os.path.isfile(csv_path)
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write header only if the file did not exist
        if not file_exists:
            writer.writerow(['File Name','Folder Name', 'Time', 'File Size (MB)', 'Site URL', 'Tab URL', 'MIME Type'])
        # Write data
        writer.writerow(data)

def check_folder():
    data_list = get_data.get_data()
    for index, data in enumerate(data_list, start=1):
        folder_name, time_stamp, file_size, site_url, tab_url, mime_type = data
        # Normalize folder_name for consistent comparison
        normalized_folder_name = os.path.join(folder_name, '')
        # Check if the normalized folder name starts with the pattern
        if normalized_folder_name.startswith(PATTERN):
            print(f"Match found in folder {folder_name}")
            # Add this data to the CSV file
            file_name = os.path.basename(folder_name)
            real_time = timestamp.timestamp_converter(time_stamp)
            real_bytes = timestamp.bytes_to_mb(file_size)
            add_data_to_csv([file_name,folder_name, real_time, real_bytes, site_url, tab_url, mime_type])
        else:
            pass



def match_folder(folder_name):
    regex = re.compile(PATTERN)
    if regex.match(folder_name):
        return True
    else:
        return False



check_folder()
# match_folder()

