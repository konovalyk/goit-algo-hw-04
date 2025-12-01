"""Benchmark comparisons for insertion sort, merge sort and Python's Timsort.

Produces CSV summary `benchmark_results.csv` and prints a short table.
"""
import copy
import csv
import statistics
import timeit
from typing import Callable

from bench_utils import get_datasets
from insertion_sort import insertion_sort
from merge_sort import merge_sort


ALGORITHMS = {
    "insertion_sort": lambda lst: insertion_sort(lst),
    "merge_sort": lambda lst: merge_sort(lst),
    "timsort": lambda lst: sorted(lst),
}


def run_benchmarks(sizes, patterns, repeats=5, csv_path="benchmark_results.csv"):
    datasets = get_datasets(sizes, patterns)

    rows = []
    for (pattern, size), data in datasets.items():
        for name, func in ALGORITHMS.items():
            # skip very large sizes for insertion sort to keep runtime reasonable
            if name == "insertion_sort" and size > 5000:
                continue

            # prepare a timer that calls the function on a fresh copy
            timer = timeit.Timer(lambda f=func, d=data: f(copy.copy(d)))
            try:
                times = timer.repeat(repeat=repeats, number=1)
            except Exception as e:
                times = [float("nan")] * repeats

            for i, t in enumerate(times, 1):
                rows.append({
                    "algorithm": name,
                    "pattern": pattern,
                    "size": size,
                    "repeat": i,
                    "time_sec": t,
                })

    # write CSV
    fieldnames = ["algorithm", "pattern", "size", "repeat", "time_sec"]
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # print short summary (median times)
    print("Benchmark summary (median times):")
    summary = {}
    for r in rows:
        key = (r["algorithm"], r["pattern"], r["size"])
        summary.setdefault(key, []).append(r["time_sec"])

    lines = []
    for key, vals in sorted(summary.items(), key=lambda x: (x[0][0], x[0][1], x[0][2])):
        alg, pattern, size = key
        med = statistics.median(vals)
        lines.append(f"{alg:15} | {pattern:12} | {size:7} | {med:.6f}s")

    for ln in lines:
        print(ln)


if __name__ == "__main__":
    # sensible default sizes and patterns
    sizes = [10000, 100000,1000000]
    patterns = ["random", "sorted", "reversed", "nearly-sorted", "duplicates"]
    run_benchmarks(sizes, patterns, repeats=3)
