#!/bin/bash

SCRIPT_DIR="$(dirname "$(realpath "$0")")"

cd "$SCRIPT_DIR/../../" || exit

TARGET_DIR="$SCRIPT_DIR/input"
OUTPUT_DIR="$SCRIPT_DIR/output"
# Python script to run
PYTHON_SCRIPT="clustering_coefficients_complete.py"

for entry in "$TARGET_DIR"/*; do
  # Run the Python script with the entry as an argument
  cat $entry | python3 "$PYTHON_SCRIPT" -> $OUTPUT_DIR/$(basename "$entry")
done
