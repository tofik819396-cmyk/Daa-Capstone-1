
def knapsack(parcels, capacity):

    n = len(parcels)

    # DP table initialization
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):

            if weight <= w:

                dp[i][w] = max(
                    value + dp[i - 1][w - weight],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking to find selected parcels
    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected.append(parcels[i - 1])
            w -= parcels[i - 1]["weight"]

    selected.reverse()

    return selected, dp[n][capacity], dp


import csv


def save_dp_table(dp, filename="output/knapsack_dp_table.csv"):

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        # Header row
        header = ["Parcel"] + [
            f"Capacity_{w}" for w in range(len(dp[0]))
        ]

        writer.writerow(header)

        # DP table rows
        for i, row in enumerate(dp):

            writer.writerow([f"Parcel_{i}"] + row)

    print("\nDP Table saved successfully!")
    print("File:", filename)
