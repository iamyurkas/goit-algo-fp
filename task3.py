import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # paths dictionary
    paths = {node: [] for node in graph}
    paths[start] = [start]

    # priority queue: (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        # check  neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # is shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, paths

# example
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 1},
    'D': {'B': 3, 'C': 1, 'E': 4},
    'E': {'D': 4}
}

distances, paths = dijkstra(graph, 'A')

print("Distances:", distances)
print("Paths:", paths)