import sys
import glob

# If you want to run this test, run it from inside Assignment1
sys.path.insert(1, ".")

from page_rank import page_rank, import_graph

input_files = glob.glob(f'{"./tests/test1/input"}/*')
output_files = glob.glob(f'{"./tests/test1/output"}/*')


def compare_dicts_within_threshold(dict1, dict2, threshold=0.005):
    if dict1.keys() != dict2.keys():
        return False

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


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

if grade > 80:
    grade_color = GREEN
elif grade > 60:
    grade_color = YELLOW
else:
    grade_color = RED

# Print the colored test output
print(f"{CYAN}========================== TEST 1 =========================={RESET}")
print(f"{GREEN}You have received the following grade: {grade_color}{grade}{RESET}\n")

# print(f"{YELLOW}Expected:{RESET}")
# print(f"{MAGENTA}PageRank of the graph:{RESET}")
# for node, rank in pagerank_dict.items():
#     print(f"Node {node}: {rank:.4f}")

# print(f"\n{RED}Received:{RESET}")
# print(f"{MAGENTA}PageRank of the graph:{RESET}")
# for node, rank in students_dict.items():
#     print(f"Node {node}: {rank:.4f}")
