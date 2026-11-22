
# INTELLIGENT COURIER PLANNING SYSTEM

## CAPSTONE PROJECT REPORT

**Subject:** Design and Analysis of Algorithms (DAA)

**Project Title:** Intelligent Courier Planning System

**Programming Language:** Python

**Development Environment:** Visual Studio Code

**Application Type:** Console-Based Application

**Submitted By:** [Your Name]

**Roll Number:** [Your Roll Number]

**Course:** B.Tech Computer Science and Engineering

**Submitted To:** [Faculty Name]

**University:** [University Name]

---

# 1. ABSTRACT

The Intelligent Courier Planning System is a Python-based
application designed to optimize parcel selection and
delivery route planning.

The system integrates multiple algorithmic techniques,
including Merge Sort, Dynamic Programming, Dijkstra's
Shortest Path Algorithm, and Nearest Neighbor TSP Approximation.

It prioritizes parcels, selects the optimal package
combination according to vehicle capacity, calculates
shortest paths between delivery locations, and generates
an approximate delivery route.

The system also measures the execution time of different
algorithmic components to evaluate their performance.

# 2. INTRODUCTION

Courier companies handle multiple parcels and delivery
locations every day. Efficient parcel selection and route
planning help reduce transportation costs and improve
delivery operations.

This project simulates an intelligent courier planning
system using fundamental concepts of Design and Analysis
of Algorithms.

# 3. PROBLEM STATEMENT

The objective is to develop a system that:

- Prioritizes parcels according to delivery priority
  and deadlines.
- Selects valuable parcels within vehicle capacity.
- Calculates shortest paths between locations.
- Generates an efficient delivery sequence.
- Compares the execution time of different algorithms.

# 4. PROJECT OBJECTIVES

1. Implement Merge Sort for parcel prioritization.
2. Apply 0/1 Knapsack using Dynamic Programming.
3. Represent delivery locations using a weighted graph.
4. Implement Dijkstra's shortest path algorithm.
5. Apply Nearest Neighbor TSP approximation.
6. Analyze algorithm execution time.
7. Generate performance comparison charts.

# 5. TECHNOLOGIES USED

- Python 3
- Visual Studio Code
- JSON
- Matplotlib
- NetworkX
- CSV

# 6. SYSTEM DESIGN

The system accepts two main inputs:

1. Parcel Dataset
2. Delivery Location Dataset

The parcel dataset contains:
- Parcel ID
- Weight
- Priority
- Deadline
- Value
- Delivery Location

The location dataset contains:
- Warehouse
- Delivery locations
- Road connections
- Distance between locations

Vehicle Capacity: 50 KG

# 7. ALGORITHMS IMPLEMENTED

## 7.1 Merge Sort

Merge Sort is a Divide and Conquer algorithm.

It divides the parcel list into smaller parts,
sorts them, and merges them into a sorted list.

Sorting Criteria:
1. Higher priority first.
2. Earlier deadline first.
3. Parcel ID as tie-breaker.

Time Complexity: O(n log n)

## 7.2 0/1 Knapsack using Dynamic Programming

The Knapsack algorithm selects parcels to maximize
total parcel value without exceeding vehicle capacity.

Each parcel can either be selected or rejected.

The algorithm uses a two-dimensional DP table
to store optimal values for different capacities.

Time Complexity: O(n × W)

Where:
n = Number of parcels
W = Vehicle capacity

## 7.3 Dijkstra's Algorithm

Dijkstra's algorithm calculates the shortest path
between two locations in a weighted graph with
non-negative edge weights.

The graph is represented using an adjacency list
and a priority queue.

Time Complexity:
O((V + E) log V)

## 7.4 Nearest Neighbor TSP Approximation

Nearest Neighbor selects the closest unvisited
delivery location from the current location.

After visiting all selected delivery locations,
the route returns to the warehouse.

This is an approximation technique and does not
guarantee the globally optimal TSP route.

Time Complexity in this implementation:

O(k(V + E) log V + k²)

Where:
k = Number of unique delivery locations
V = Number of graph vertices
E = Number of graph edges

# 8. SYSTEM IMPLEMENTATION

The project contains the following Python modules:

- main.py
- sorting.py
- knapsack.py
- dijkstra.py
- route_optimizer.py
- performance.py

The data directory contains:
- parcels.json
- locations.json

The output directory stores the Knapsack DP table.

The charts directory stores runtime comparison charts.

# 9. PERFORMANCE ANALYSIS

The system tests different dataset sizes:

10, 20, 50, 100 and 200.

Execution time is measured using Python's
time.perf_counter() function.

The following algorithms are compared:

- Merge Sort
- Knapsack Dynamic Programming
- Dijkstra's Algorithm
- Nearest Neighbor

A runtime comparison chart is generated using Matplotlib.

Actual measured execution times are recorded
in the performance test results.

# 10. TESTING AND RESULTS

The system is tested using sample parcel and
delivery location datasets.

Test cases include:

1. Parcel prioritization.
2. Package selection within vehicle capacity.
3. Shortest path calculation.
4. Delivery route generation.
5. Runtime measurement.
6. Runtime chart generation.

The vehicle capacity constraint is 50 KG.

The generated delivery route visits the selected
delivery locations and returns to the warehouse.

# 11. LIMITATIONS

- Nearest Neighbor does not guarantee an optimal TSP route.
- The sample dataset uses predefined road distances.
- The system does not use real-time traffic information.
- Delivery deadlines are used for sorting, not for
  time-window feasibility checking.
- The packing algorithm maximizes parcel value,
  not delivery profit or deadline feasibility.

# 12. FUTURE SCOPE

- Real-time GPS integration.
- Traffic-aware route planning.
- Graphical user interface.
- Multiple delivery vehicles.
- Time-window based scheduling.
- Advanced route optimization techniques.
- Database integration.

# 13. CONCLUSION

The Intelligent Courier Planning System demonstrates
the practical application of various algorithms in
a real-world inspired courier planning problem.

The integration of sorting, dynamic programming,
shortest path algorithms, and approximation techniques
provides an efficient approach to parcel selection
and delivery route planning.

The project also demonstrates the importance of
algorithm performance analysis and optimization.

# 14. REFERENCES

1. Introduction to Algorithms – Cormen, Leiserson,
   Rivest and Stein.
2. Python Official Documentation.
3. Matplotlib Official Documentation.
4. NetworkX Documentation.
5. Design and Analysis of Algorithms course materials.
