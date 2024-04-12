#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "One argument expected (the chapter number, like 1, 02, etc.)" >&2
    echo "Usage: $0 <chapter>"
    exit 2
fi

# Padding with leading zeros (1 -> 01)
chapter_no_zeros=$(echo $1 | sed 's/^0*//')
chapter=$(printf "%02d" "$chapter_no_zeros")

# Find .md files with "OP-<chapter>-<title>*.md" in their name
pattern="OP-$chapter-*.md"
files=$(find . -type f -name "$pattern")

# Count the number of files found
file_count=$(echo "$files" | wc -l)

# If multiple files are found, print an error message
if [ "$file_count" -gt 1 ]; then
    echo "Error: Multiple files match the pattern $pattern:"
    
    # Save IFS
    OLDIFS=$IFS

    while IFS= read -r file; do
        echo "$file"
    done <<< "$files"

    # restore it
    IFS=$OLDIFS

    exit 2
fi

filename=$files

echo "Changing publicDir in vite.config.ts ..."
bash change_public_dir.sh $chapter_no_zeros

echo "Running slidev ..."
pnpm slidev $filename