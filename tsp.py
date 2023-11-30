from itertools import permutations

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i+1]]
    total_distance += graph[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(graph):
    cities = list(graph.keys())
    min_distance = float('inf')
    optimal_path = None

    for perm in permutations(cities):
        distance = calculate_total_distance(perm, graph)
        if distance < min_distance:
            min_distance = distance
            optimal_path = perm

    return optimal_path, min_distance

# Example usage
graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'A': 1, 'B': 2, 'C': 5}
}

optimal_path, min_distance = traveling_salesman_bruteforce(graph)

print("Optimal Path:", optimal_path)
print("Minimum Distance:", min_distance)
