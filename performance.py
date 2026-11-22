
import time
import random
import matplotlib.pyplot as plt

from sorting import merge_sort
from knapsack import knapsack
from dijkstra import dijkstra
from route_optimizer import nearest_neighbor


def measure_time(function, *args):
    start = time.perf_counter()

    function(*args)

    end = time.perf_counter()

    return end - start


def generate_parcels(n):

    parcels = []

    for i in range(n):

        parcels.append({
            "id": f"P{i}",
            "weight": random.randint(1, 20),
            "priority": random.randint(1, 5),
            "deadline": random.randint(1, 10),
            "value": random.randint(10, 200),
            "location": "A"
        })

    return parcels


def generate_graph(n):

    graph = {
        str(i): [] for i in range(n)
    }

    # Connected chain
    for i in range(n - 1):

        graph[str(i)].append((str(i + 1), 1))
        graph[str(i + 1)].append((str(i), 1))

    # Additional edges
    for i in range(n):

        for j in range(i + 2, n):

            if random.random() < 0.05:

                weight = random.randint(1, 20)

                graph[str(i)].append((str(j), weight))
                graph[str(j)].append((str(i), weight))

    return graph


def run_performance_test():

    sizes = [10, 20, 50, 100, 200]

    sorting_times = []
    knapsack_times = []
    dijkstra_times = []
    route_times = []

    for n in sizes:

        print("\nTesting Dataset Size:", n)

        parcels = generate_parcels(n)

        graph = generate_graph(n)

        # Sorting
        sorting_time = measure_time(
            merge_sort, parcels
        )

        # Knapsack
        knapsack_time = measure_time(
            knapsack, parcels, 50
        )

        # Dijkstra
        dijkstra_time = measure_time(
            dijkstra, graph, "0"
        )

        # Nearest Neighbor
        destinations = [
            str(i) for i in range(1, min(n, 11))
        ]

        route_time = measure_time(
            nearest_neighbor,
            graph,
            "0",
            destinations
        )

        sorting_times.append(sorting_time)
        knapsack_times.append(knapsack_time)
        dijkstra_times.append(dijkstra_time)
        route_times.append(route_time)

        print("Sorting:", sorting_time)
        print("Knapsack:", knapsack_time)
        print("Dijkstra:", dijkstra_time)
        print("Nearest Neighbor:", route_time)

    # Runtime comparison chart
    plt.figure(figsize=(10, 6))

    plt.plot(sizes, sorting_times, marker="o",
             label="Merge Sort")

    plt.plot(sizes, knapsack_times, marker="o",
             label="Knapsack DP")

    plt.plot(sizes, dijkstra_times, marker="o",
             label="Dijkstra")

    plt.plot(sizes, route_times, marker="o",
             label="Nearest Neighbor")

    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (Seconds)")

    plt.title("Courier System Algorithm Performance")

    plt.legend()
    plt.grid(True)

    plt.savefig("charts/runtime_comparison.png")

    plt.show()

    print("\nRuntime chart saved successfully!")


if __name__ == "__main__":
    run_performance_test()
