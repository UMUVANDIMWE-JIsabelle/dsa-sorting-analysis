import random
import time
import csv

from sorting import insertion_sort, merge_sort

SIZES = [500, 1000, 2000, 4000, 8000]
RUNS_PER_SIZE = 5


def make_random_list(n):
    return [random.randint(0, 1_000_000) for _ in range(n)]


def time_sort(sort_function, data):
    data_copy = data.copy()
    start = time.perf_counter()
    sort_function(data_copy)
    end = time.perf_counter()
    return end - start


def main():
    results = [] 

    for n in SIZES:
        print(f"Working on size n = {n} ...")

        insertion_times = []
        merge_times = []

        for run in range(RUNS_PER_SIZE):
            random_list = make_random_list(n)

            insertion_times.append(time_sort(insertion_sort, random_list))
            merge_times.append(time_sort(merge_sort, random_list))

        avg_insertion = sum(insertion_times) / RUNS_PER_SIZE
        avg_merge = sum(merge_times) / RUNS_PER_SIZE

        already_sorted_list = sorted(make_random_list(n))
        insertion_sorted_input_time = time_sort(insertion_sort, already_sorted_list)

        print(f"  insertion (random):        {avg_insertion:.5f} sec")
        print(f"  merge     (random):        {avg_merge:.5f} sec")
        print(f"  insertion (already sorted):{insertion_sorted_input_time:.5f} sec")

        results.append({
            "n": n,
            "insertion_random": avg_insertion,
            "merge_random": avg_merge,
            "insertion_sorted_input": insertion_sorted_input_time,
        })

    # to save results to a csv file 
    with open("results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "n", "insertion_random", "merge_random", "insertion_sorted_input"
        ])
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print("\nSaved results to results.csv")


if __name__ == "__main__":
    main()