import sqlite3
import shutil
import pprint
from datetime import datetime
import timestamp

PATH = "/Users/A200298519/library/Application Support/Google/Chrome/Profile 4/History"
TEMP_PATH = "/Users/A200298519/Desktop/MVP/cli/"

LOCAL_STATE = "/Users/A200298519/Library/Application Support/Google/Chrome/Local State"

shutil.copy2(PATH, TEMP_PATH)
shutil.copy2(LOCAL_STATE, TEMP_PATH)


conn = sqlite3.connect(TEMP_PATH + "History")
cursor = conn.cursor()

# Get the schema of the downloads table
query = """
PRAGMA table_info(downloads);
"""
cursor.execute(query)
schema_info = cursor.fetchall()

today_date = timestamp.get_today_date()
# Extract the column headers
headers = [column[1] for column in schema_info]

# Define the query to fetch the first row from the downloads table
today_date = timestamp.get_today_date()

query = f"""
SELECT target_path, start_time FROM downloads
where start_time >= {today_date}
ORDER BY id DESC
LIMIT 3;
"""

# Execute the query
cursor.execute(query)

# Fetch the first row
first_row = cursor.fetchall()

# Print the column headers and the first row
print("Column headers of the downloads table:")
print(headers)
print("\nFirst row data:")
print(first_row, "\n")

conn.close()










