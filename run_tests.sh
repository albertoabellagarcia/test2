#!/bin/bash

# Define the JSON file to validate
JSON_FILE="schema.json"  # The file you want to validate

# Check if the file exists
if [[ ! -f "$JSON_FILE" ]]; then
  echo "Error: File $JSON_FILE does not exist in the PR."
  exit 1
fi

# Validate the JSON file
if jq empty "$JSON_FILE" > /dev/null 2>&1; then
  echo "JSON file $JSON_FILE is valid."
  exit 0
else
  echo "Error: JSON file $JSON_FILE is invalid."
  exit 1
fi
