#!/bin/sh

OUTPUT_FILE="context.txt"

# Clear the output file if it already exists
> "$OUTPUT_FILE"

echo "Gathering files into $OUTPUT_FILE..."

# Find all HTML files and append them
find . -type f -name "*.html" | while read -r file; do
    echo "Adding $file"
    echo "==== BEGIN FILE: $file ====" >> "$OUTPUT_FILE"
    cat "$file" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
done

# Check for and append style.css
if [ -f "style.css" ]; then
    echo "Adding style.css"
    echo "==== BEGIN FILE: style.css ====" >> "$OUTPUT_FILE"
    cat "style.css" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
else
    echo "style.css not found in the current directory."
fi

echo "Done. Your code is ready in $OUTPUT_FILE."