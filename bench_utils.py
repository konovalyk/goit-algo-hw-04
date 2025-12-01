
import random
import time
from typing import List, Tuple, Dict


def generate_random_list(n: int, low: int = 0, high: int = 1_000_000) -> List[int]:
    return [random.randint(low, high) for _ in range(n)]


def generate_nearly_sorted(n: int, shuffle_fraction: float = 0.01) -> List[int]:
    lst = list(range(n))
    swaps = max(1, int(n * shuffle_fraction))
    for _ in range(swaps):
        i = random.randrange(n)
        j = random.randrange(n)
        lst[i], lst[j] = lst[j], lst[i]
    return lst


def generate_duplicates(n: int, unique: int = 10) -> List[int]:
    return [random.randint(0, unique - 1) for _ in range(n)]


def get_datasets(sizes: List[int], patterns: List[str], seed: int = 42) -> Dict[Tuple[str, int], List[int]]:
    random.seed(seed)
    datasets = {}
    for size in sizes:
        for pattern in patterns:
            if pattern == "random":
                lst = generate_random_list(size)
            elif pattern == "sorted":
                lst = list(range(size))
            elif pattern == "reversed":
                lst = list(range(size, 0, -1))
            elif pattern == "nearly-sorted":
                lst = generate_nearly_sorted(size)
            elif pattern == "duplicates":
                lst = generate_duplicates(size)
            else:
                raise ValueError(f"Unknown pattern: {pattern}")

            datasets[(pattern, size)] = lst
    return datasets

