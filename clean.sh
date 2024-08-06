#!/bin/bash

dir="$HOME/Downloads/Test"

cd "$dir" || exit 1  # Change directory to Downloads or exit if fails

pattern="/Users/A200298519/Downloads/"

for file in "$dir"/*
do
    if [ -f "$file" ]; then  # Check if it's a regular file
            filename="${file##*/}"  # Extract filename from path
            filesize=$(stat -f "%z" "$file")  # Get file size in bytes for macOS
            if [ "$filesize" -gt 1000000 ] ; then
                echo "Removing $filename because it's larger than 1MB"
                rm "$file"
            fi
            echo "$filename $filesize bytes"
    fi
done

