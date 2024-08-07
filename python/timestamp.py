from datetime import datetime, timedelta, date


def timestamp_converter(timestamp):
    # Convert microseconds to seconds
    timestamp_in_seconds = timestamp / 1000000

    # Define the start of the Windows epoch
    windows_epoch_start = datetime(1601, 1, 1)

    # Add the timestamp (in seconds) to the Windows epoch start
    date = windows_epoch_start + timedelta(seconds=timestamp_in_seconds)

    # Format the date
    formatted_date = date.strftime("%Y-%m-%d,  %H:%M:%S")
    return formatted_date

def get_today_date():
    # Get today's date as a datetime object
    today_midnight = datetime.combine(date.today(), datetime.min.time())
    # Format today's date to match the required format
    today_date_str = today_midnight.strftime("%Y-%m-%d, %H:%M:%S")

    # Convert the formatted string back to a timestamp (in microseconds)
    today_date_timestamp = date_to_timestamp(today_date_str)

    return today_date_timestamp

def date_to_timestamp(date_str):
    # Parse the date string into a datetime object
    given_date = datetime.strptime(date_str, "%Y-%m-%d, %H:%M:%S")

    # Define the start of the Windows epoch
    windows_epoch_start = datetime(1601, 1, 1)

    # Calculate the difference in seconds
    difference = given_date - windows_epoch_start
    timestamp_in_seconds = difference.total_seconds()

    # Convert seconds to microseconds
    timestamp_in_microseconds = int(timestamp_in_seconds * 1000000)

    return timestamp_in_microseconds

def bytes_to_mb(bytes):
    return bytes / 1024 / 1024