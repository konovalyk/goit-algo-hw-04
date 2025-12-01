from typing import List


def merge_sort(lst: List[int]) -> List[int]:
    """Return a new sorted list using merge sort (stable)."""
    if len(lst) <= 1:
        return lst[:]  # return a shallow copy

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    merged: List[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])

    return merged


if __name__ == "__main__":
    sample = [5, 3, 8, 4, 2]
    print(merge_sort(sample))
