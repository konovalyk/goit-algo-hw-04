
from typing import List


def insertion_sort(lst: List[int]) -> List[int]:
    """Sort list in-place using insertion sort and return it.

    Note: This function sorts the provided list in-place.
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


if __name__ == "__main__":
    sample = [5, 3, 8, 4, 2]
    print(insertion_sort(sample))
