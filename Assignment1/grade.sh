#!/bin/bash

# Initialize variables
total_grade=0
num_tests=0

for script in tests/test*/test*.py; do
    test_output=$(python3 "$script")

    echo -e "$test_output"
    echo 
    grade=$(echo "$test_output" | grep "You have received the following grade" | awk -F ':' '{print $2}')

    grade=$(echo "$grade" | sed 's/\x1b\[[0-9;]*m//g')

    total_grade=$(echo "$total_grade + $grade" | bc)

    num_tests=$((num_tests + 1))
done

# Calculate the average if there are any tests
if [ "$num_tests" -gt 0 ]; then
    average=$(echo "scale=2; $total_grade / $num_tests" | bc)
    echo "Total Grade: $average"
else
    echo "No tests found."
fi
