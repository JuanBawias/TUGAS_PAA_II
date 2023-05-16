import itertools
import math

def tsp_brute_force(graph, start_node):
    nodes = list(graph.keys())
    nodes.remove(start_node)
    permutations = list(itertools.permutations(nodes))
    min_distance = math.inf
    optimal_path = []

    for permutation in permutations:
        current_path = [start_node] + list(permutation) + [start_node]
        total_distance = 0

        for i in range(len(current_path) - 1):
            current_node = current_path[i]
            next_node = current_path[i + 1]
            total_distance += graph[current_node][next_node]

        if total_distance < min_distance:
            min_distance = total_distance
            optimal_path = current_path

    return optimal_path, min_distance


# Contoh penggunaan
graph = {
    'A': {'A': 0, 'B': 2, 'C': 9, 'D': 10},
    'B': {'A': 1, 'B': 0, 'C': 6, 'D': 4},
    'C': {'A': 15, 'B': 7, 'C': 0, 'D': 8},
    'D': {'A': 6, 'B': 3, 'C': 12, 'D': 0}
}

start_node = 'A'
optimal_path, min_distance = tsp_brute_force(graph, start_node)
print("Jalur optimal:", optimal_path)
print("Jarak minimal:", min_distance)
