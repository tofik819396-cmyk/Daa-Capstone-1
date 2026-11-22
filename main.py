from knapsack import knapsack, save_dp_table

from route_optimizer import (
    build_graph,
    nearest_neighbor,
    calculate_route_details
)

import json

from sorting import merge_sort


# Load parcel dataset
with open("data/parcels.json", "r") as file:
    parcels = json.load(file)


CAPACITY = 50


print("=" * 50)
print("   INTELLIGENT COURIER PLANNING SYSTEM")
print("=" * 50)


# STEP 1: SORTING
print("\n1. PARCEL PRIORITIZATION")
print("-" * 50)

sorted_parcels = merge_sort(parcels)

for parcel in sorted_parcels:
    print(
        parcel["id"],
        "| Priority:", parcel["priority"],
        "| Deadline:", parcel["deadline"],
        "| Weight:", parcel["weight"], "KG"
    )


# STEP 2: KNAPSACK
print("\n2. OPTIMAL PACKAGE SELECTION")
print("-" * 50)

selected, total_value, dp = knapsack(
    sorted_parcels, CAPACITY
)

save_dp_table(dp)

total_weight = sum(
    parcel["weight"] for parcel in selected
)

print("Selected Parcels:")

for parcel in selected:
    print(
        parcel["id"],
        "| Weight:", parcel["weight"],
        "| Value:", parcel["value"]
    )

print("\nTotal Weight:", total_weight, "KG")
print("Remaining Capacity:", CAPACITY - total_weight, "KG")
print("Maximum Total Value:", total_value)


print("\n" + "=" * 50)
print("       PHASE 2 COMPLETED")
print("=" * 50)


# STEP 3: GRAPH AND ROUTE OPTIMIZATION

print("\n3. DELIVERY ROUTE OPTIMIZATION")
print("-" * 50)

# Load location dataset
with open("data/locations.json", "r") as file:
    location_data = json.load(file)

# Create graph
graph = build_graph(location_data)

warehouse = location_data["warehouse"]

# Get delivery locations from selected parcels
destinations = [
    parcel["location"] for parcel in selected
]

# Apply Nearest Neighbor
route, route_distance = nearest_neighbor(
    graph,
    warehouse,
    destinations
)

print("Delivery Route:")

print(" -> ".join(route))

# Display individual shortest paths
print("\n4. SHORTEST PATH DETAILS")
print("-" * 50)

details, total_distance = calculate_route_details(
    graph, route
)

for detail in details:

    print(
        detail["from"],
        "to",
        detail["to"]
    )

    print("Path:", " -> ".join(detail["path"]))

    print("Distance:", detail["distance"], "KM")
    print()

print("Total Delivery Distance:", total_distance, "KM")

print("\n" + "=" * 50)
print("       PHASE 3 COMPLETED")
print("=" * 50)
