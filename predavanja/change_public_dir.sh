#!/bin/bash

# Check if argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <new_public_dir>"
    exit 1
fi

# Define the new public directory
# Pad it with leading zeros (1 -> 01)
new_public_dir=$(printf "%02d" "$1")

# Set the path to your TypeScript file
config_file="vite.config.ts"

# Use sed to replace the publicDir value
sed -i "s/publicDir: '\.\/assets\/[0-9]\{2\}'/publicDir: '\.\/assets\/${new_public_dir}'/" "$config_file"

echo "publicDir updated to './assets/$new_public_dir'"
