import csv

rows = []
with open("results.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append({
            "n": int(row["n"]),
            "insertion_random": float(row["insertion_random"]),
            "merge_random": float(row["merge_random"]),
            "insertion_sorted_input": float(row["insertion_sorted_input"]),
        })

print(f"{'n':>6} -> {'2n':>6} | {'insertion ratio':>16} | {'merge ratio':>12} | {'sorted-input ratio':>18}")

for i in range(1, len(rows)):
    prev = rows[i - 1]
    curr = rows[i]

    insertion_ratio = curr["insertion_random"] / prev["insertion_random"]
    merge_ratio = curr["merge_random"] / prev["merge_random"]
    sorted_input_ratio = curr["insertion_sorted_input"] / prev["insertion_sorted_input"]

    print(f"{prev['n']:>6} -> {curr['n']:>6} | "
          f"{insertion_ratio:>16.2f} | {merge_ratio:>12.2f} | {sorted_input_ratio:>18.2f}")