
from typing import List
import heapq


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """Merge k sorted lists into a single sorted list.

    Args:
        lists: list of sorted lists of integers

    Returns:
        A single sorted list containing all elements.
    """
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result: List[int] = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][next_idx], list_idx, next_idx))

    return result


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(merge_k_lists(lists))
