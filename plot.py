import csv
import matplotlib.pyplot as plt

sizes = []
insertion_random = []
merge_random = []
insertion_sorted_input = []

with open("results.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sizes.append(int(row["n"]))
        insertion_random.append(float(row["insertion_random"]))
        merge_random.append(float(row["merge_random"]))
        insertion_sorted_input.append(float(row["insertion_sorted_input"]))

plt.figure(figsize=(8, 5))

plt.plot(sizes, insertion_random, marker="o", label="Insertion sort (random input)")
plt.plot(sizes, merge_random, marker="o", label="Merge sort (random input)")
plt.plot(sizes, insertion_sorted_input, marker="o", label="Insertion sort (already sorted input)")

plt.xlabel("List size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting time vs list size")
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig("sorting_chart.png", dpi=150, bbox_inches="tight")
print("Saved chart to sorting_chart.png")