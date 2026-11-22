
from dijkstra import dijkstra, get_shortest_path


def build_graph(location_data):

    graph = {
        node: [] for node in location_data["locations"]
    }

    for source, destination, distance in location_data["edges"]:

        graph[source].append((destination, distance))
        graph[destination].append((source, distance))

    return graph


def nearest_neighbor(graph, warehouse, destinations):

    # Duplicate delivery locations remove karna
    destinations = sorted(set(destinations))

    # Warehouse ko delivery destinations se remove karna
    destinations = [
        node for node in destinations
        if node != warehouse
    ]

    current = warehouse
    unvisited = set(destinations)

    route = [warehouse]
    total_distance = 0

    while unvisited:

        distances, _ = dijkstra(graph, current)

        next_location = min(
            unvisited,
            key=lambda node: (distances[node], node)
        )

        total_distance += distances[next_location]

        route.append(next_location)

        current = next_location
        unvisited.remove(next_location)

    # Return to warehouse
    distances, _ = dijkstra(graph, current)

    total_distance += distances[warehouse]
    route.append(warehouse)

    return route, total_distance


def calculate_route_details(graph, route):

    total_distance = 0
    details = []

    for i in range(len(route) - 1):

        start = route[i]
        end = route[i + 1]

        distances, previous = dijkstra(graph, start)

        distance = distances[end]

        path = get_shortest_path(
            previous, start, end
        )

        total_distance += distance

        details.append({
            "from": start,
            "to": end,
            "path": path,
            "distance": distance
        })

    return details, total_distance
