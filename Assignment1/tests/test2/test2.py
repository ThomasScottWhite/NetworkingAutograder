import sys
import glob

# If you want to run this test, run it from inside Assignment1
sys.path.insert(1, ".")

from hits import hits, import_graph

input_files = glob.glob(f'{"./tests/test2/input"}/*')
output_files = glob.glob(f'{"./tests/test2/output"}/*')


def compare_dicts_within_threshold(dict1, dict2, threshold=0.005):
    if dict1.keys() != dict2.keys():
        return False

    for key in dict1:
        if abs(dict1[key] - dict2[key]) > threshold:
            return False

    return True


def text_file_to_dict(file_path):
    IsAuthSection = False
    hub_dict = {}
    auth_dict = {}
    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:

        if line.startswith("Authority Scores of the graph:"):
            IsAuthSection = True
            continue
        elif line.startswith("Hub Scores of the graph:"):
            IsAuthSection = False
            continue
        elif not line.strip():
            continue
        
        parts = line.strip().split(":")
        if len(parts) == 2:
            node = int(parts[0].split()[1])
            rank = float(parts[1])
            if IsAuthSection:
                auth_dict[node] = rank
            else:
                hub_dict[node] = rank

    return auth_dict, hub_dict


results = []
for input, output in zip(input_files, output_files):

    with open(input, "r") as file:
        data = file.read()

    G = import_graph(data)

    auth, hub = hits(G)

    student_auth, student_hub = text_file_to_dict(output)

    result1 = compare_dicts_within_threshold(student_auth, auth)
    result2 = compare_dicts_within_threshold(student_hub, hub)

    results.append(result1 and result2)

grade = 0

for result in results:
    if result:
        grade += 100 / len(results)

print(grade)
