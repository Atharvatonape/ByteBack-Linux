import sqlite3
import shutil
import pprint
from datetime import datetime
import timestamp
from dotenv import load_dotenv 
import os

load_dotenv()

PATH = os.getenv("CHROME_HISTORY_PATH")
TEMP_PATH = os.getenv("TEMP_PATH")

# PATH = "/Users/A200298519/library/Application Support/Google/Chrome/Profile 4/History"
# TEMP_PATH = "/Users/A200298519/Desktop/MVP/cli/"

def get_data():
    shutil.copy2(PATH, TEMP_PATH)
    conn = sqlite3.connect(TEMP_PATH + "History")
    cursor = conn.cursor()
    # display_table_headers(conn, 'downloads')
    result = get_downloads_today(cursor)
    data = result
    conn.close()
    os.remove(TEMP_PATH + "History")
    # for i in data:
    #     print(i[0])
    # print(data[0][0])
    return data

def get_downloads_today(cursor):
    today_date = timestamp.get_today_date()
    query = f"""
    SELECT current_path, start_time , total_bytes, site_url, tab_url, mime_type FROM downloads
    where start_time >= {today_date}
    ORDER BY id DESC
    """
    cursor.execute(query)
    downloads = cursor.fetchall()
    # print(downloads)
    return downloads

def display_table_headers(conn, table_name):
    """
    Displays the column headers for a specified table in the SQLite database.

    Parameters:
    - conn: SQLite database connection object.
    - table_name: Name of the table for which to display headers.
    """
    cursor = conn.cursor()
    try:
        cursor.execute(f"PRAGMA table_info({table_name});")
        headers = cursor.fetchall()
        if headers:
            print(f"Column headers for the table '{table_name}':")
            for header in headers:
                print(header[1])  # Column names are in the second element
        else:
            print(f"No headers found. Does the table '{table_name}' exist?")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

get_data()









