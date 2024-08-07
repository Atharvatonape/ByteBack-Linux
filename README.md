# ByteBack-Linux CLI Tool

`ByteBack` is an enhanced command-line interface (CLI) tool that automates the logs of downloaded files in a particular folder and also automatic deletion of files after a specified period. This Linux-Python based tool is designed to operate using native libraries, eliminating the need for external dependencies.

## Motivation 

ByteBack was developed to address the common challenges of managing large volumes of downloadable content, particularly in environments where efficient data handling is crucial, like research labs and tech companies. It simplifies the process of tracking and managing files, automates data clean-up based on predefined rules, and enhances productivity by keeping digital workspaces organized. This tool is invaluable for anyone needing a systematic approach to handle their digital downloads effectively.

## Features

- **No external Libraries**: After setting up the project you dont need to download any extra libraries making a very Powerful Robust and Scalable tool.
- **Log File Size**: Automatically logs the size of downloaded files.
- **Log Download Date**: Captures the date and time of the download.
- **Log Download URL**: Records the URL from which files are downloaded.
- **Log Storage Location**: Notes the local storage path of the downloaded files.
- **Periodic Deletion**: Automatically deletes downloaded files after a specified duration.

## Prerequisites

Ensure you have Python installed on your machine (Python 3.x recommended).

## Installation and Configuration

### Step 1: Download the Code

Download the ByteBack script from the provided repository or source.

### Step 2: Configure the Environment File

Modify the `.env` file in your download with the following details:

- **History Path**: Path to your Google Chrome download database. Typically found at:
  - Linux/macOS: `~/.config/google-chrome/Default/History`
- **Path**: Directory where you want to automate the tracking and management of downloads.
- **Temp_Path**: Path for storing a temporary copy of the Chrome database, which is cleared each cycle.

## Setting Up Automation with Cron Jobs

Automate ByteBack by setting up cron jobs on macOS and Linux, or using Task Scheduler on Windows.

### macOS and Linux

1. **Open your terminal.**
2. **Edit your crontab**:
   ```bash
   crontab -e

## Usage

Navigate to the directory containing the script and execute it with the following syntax:

```bash
./clean.sh
