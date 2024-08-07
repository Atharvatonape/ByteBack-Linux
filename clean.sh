#!/bin/bash

dir="$HOME/Downloads/Test"
start_dir=$(pwd)  # Save current directory

cd "$dir" || exit 1  # Change directory to Downloads or exit if fails

pattern="/Users/A200298519/Downloads/"

cronnn="true"
which python3

if [ $cronnn = "true" ]; then
    echo "Calling Python script for checking folder"
    python3 "/Users/A200298519/Desktop/MVP/cli/python/create_csv.py"
fi

for file in "$dir"/*
do
    if [ -f "$file" ]; then  # Check if it's a regular file
            filename="${file##*/}"  # Extract filename from path
            filesize=$(stat -f "%z" "$file")  # Get file size in bytes for macOS
            if [ "$filesize" -gt 100 ] ; then
                echo "Removing $filename because it's larger than 1MB"
                rm "$file"
            fi
            echo "$filename $filesize bytes"
    fi
done

