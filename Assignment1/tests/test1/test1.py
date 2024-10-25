import sys
import glob

# If you want to run this test, run it from inside Assignment1
sys.path.insert(1, ".")

from page_rank_complete import page_rank, import_graph

input_files = glob.glob(f'{"./tests/test1/input"}/*')
output_files = glob.glob(f'{"./tests/test1/output"}/*')


def compare_dicts_within_threshold(dict1, dict2, threshold=0.005):
    """
    Compare two dictionaries to see if their values are within a given threshold.

    Parameters:
    - dict1, dict2: The two dictionaries to compare
    - threshold: The maximum allowed difference between values (default 0.005)

    Returns:
    - bool: True if all corresponding values are within the threshold, False otherwise
    """
    # Check if both dictionaries have the same keys
    if dict1.keys() != dict2.keys():
        return False

    # Compare values for each key
    for key in dict1:
        if abs(dict1[key] - dict2[key]) > threshold:
            return False

    return True


def text_file_to_dict(file_path):
    dict = {}
    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("PageRank of the graph:") or not line.strip():
            continue

        parts = line.strip().split(":")
        if len(parts) == 2:
            node = int(parts[0].split()[1])
            rank = float(parts[1])
            dict[node] = rank

    return dict


results = []
for input, output in zip(input_files, output_files):

    with open(input, "r") as file:
        data = file.read()

    G = import_graph(data)

    students_dict = page_rank(G)

    pagerank_dict = text_file_to_dict(output)

    result = compare_dicts_within_threshold(students_dict, pagerank_dict)

    results.append(result)

grade = 0

for result in results:
    if result:
        grade += 100 / len(results)

print(grade)
