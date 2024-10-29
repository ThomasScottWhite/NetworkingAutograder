try:
    import sys
    import glob

    # If you want to run this test, run it from inside Assignment1
    sys.path.insert(1, ".")

    from clustering_coefficients import (
        local_clustering_coefficent,
        global_clustering_coefficient,
        import_graph,
    )

    input_files = glob.glob(f'{"./tests/test3/input"}/*')
    output_files = glob.glob(f'{"./tests/test3/output"}/*')

    def compare_dicts_within_threshold(dict1, dict2, threshold=0.005):
        if dict1.keys() != dict2.keys():
            return False

        for key in dict1:
            if abs(dict1[key] - dict2[key]) > threshold:
                return False

        return True

    def text_file_to_dict(file_path):
        global_coefficent_section = False
        local_dict = {}
        with open(file_path, "r") as file:
            lines = file.readlines()

        for line in lines:

            if line.startswith("Global Clustering Coefficent of the graph"):
                global_coefficent_section = True
                continue
            elif line.startswith("Local Clustering Coefficients of the graph:"):
                global_coefficent_section = False
                continue
            elif not line.strip():
                continue

            if global_coefficent_section:
                global_coefficent = float(line.strip())
            else:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    node = int(parts[0].split()[1])
                    rank = float(parts[1])
                    local_dict[node] = rank

        return global_coefficent, local_dict

    results = []
    for input, output in zip(input_files, output_files):

        with open(input, "r") as file:
            data = file.read()

        G = import_graph(data)

        student_local_clustering_dicts = local_clustering_coefficent(G)
        student_global_clustering_value = global_clustering_coefficient(G)

        global_coefficent, local_dict = text_file_to_dict(output)

        result1 = round(global_coefficent, 4) == round(
            student_global_clustering_value, 4
        )
        result2 = compare_dicts_within_threshold(
            local_dict, student_local_clustering_dicts
        )

        grade = 0
        results.append(result1 and result2)
        for result in results:
            if result:
                grade += 100 / len(results)

except Exception as e:
    grade = 0


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
print(f"{CYAN}========================== TEST 3 =========================={RESET}")
print(f"{GREEN}You have received the following grade: {grade_color}{grade}{RESET}\n")

# print(f"{YELLOW}Expected:{RESET}")
# print(f"{MAGENTA}PageRank of the graph:{RESET}")
# for node, rank in pagerank_dict.items():
#     print(f"Node {node}: {rank:.4f}")

# print(f"\n{RED}Received:{RESET}")
# print(f"{MAGENTA}PageRank of the graph:{RESET}")
# for node, rank in students_dict.items():
#     print(f"Node {node}: {rank:.4f}")
