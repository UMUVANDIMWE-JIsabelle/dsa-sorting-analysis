# Algorithms under the microscope

This repo has my code for the sorting option of the DSA assignment... comparing an O(n²) sort (insertion sort) against an O(n log n) sort (merge sort).

## Files

| File | What it does |
|---|---|
| `sorting.py` | The two sorting algorithms (`insertion_sort`, `merge_sort`), plus a check block that tests both against small hand-picked lists |
| `experiment.py` | Generates random lists at 5 sizes, times both sorts (5 runs each, averaged), and saves everything to `results.csv` |
| `doubling_test.py` | Reads `results.csv` and works out the doubling ratios (time at n ÷ time at n/2) for each sort |
| `plot.py` | Reads `results.csv` and draws the chart (`sorting_chart.png`) |
| `results.csv` | The timing data itself, produced by `experiment.py` |
| `sorting_chart.png` | The chart: insertion sort (random), merge sort (random), and insertion sort (already sorted), all on one plot |


## How to run it, in order

```bash
python sorting.py          # runs the sanity checks, prints OK/WRONG for each test case
python experiment.py       # times both sorts, writes results.csv (takes a minute or so)
python doubling_test.py    # reads results.csv, prints the doubling ratios
python plot.py             # reads results.csv, saves sorting_chart.png
```

`doubling_test.py` and `plot.py` don't generate any new data themselves... they just read whatever is currently in `results.csv`. So if you want new numbers, rerun `experiment.py` first. Running the other two on their own will just reprint/replot the same results every time.

## Why the numbers change slightly between runs of `experiment.py`

Every time `experiment.py` runs, it generates brand new random lists, so the exact timings shift a little each time... normal measurement noise (background processes, small variations in random input, etc). The overall pattern stays the same though: insertion sort's doubling ratio stays close to 4, merge sort's stays a bit above 2, no matter which run you look at. 

## Sources used

I learned the concepts and adapted the code from these videos:

- Sambol, M. (2016) *Insertion sort in 2 minutes*. https://www.youtube.com/watch?v=JU767SDMDvA
- Sambol, M. (2016) *Merge sort in 3 minutes*. https://www.youtube.com/watch?v=4VqmGXwpLqc
- Sherrill, D. (2019) *Insertion Sort Algorithm Explained (Full Code Included)*. https://www.youtube.com/watch?v=byHi41L9vTM
- freeCodeCamp.org (2021) *Understanding Sorting Algorithms*. https://www.youtube.com/watch?v=l7-f9gS8VOs
- FelixTechTips (2020) *Merge Sort In Python Explained (With Example And Code)*. https://www.youtube.com/watch?v=cVZMah9kEjI


                                           written by J'Isabelle UMUVANDIMWE   