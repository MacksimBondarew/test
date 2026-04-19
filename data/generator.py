import random
from typing import List


def random_data(n: int, low: int = 0, high: int = 10_000) -> List[int]:
    """Return n random integers in [low, high]."""
    return [random.randint(low, high) for _ in range(n)]


def ascending_data(n: int) -> List[int]:
    """Return already-sorted ascending list (best case for most algorithms)."""
    return list(range(1, n + 1))


def descending_data(n: int) -> List[int]:
    """Return reverse-sorted list (worst case for e.g. Insertion Sort)."""
    return list(range(n, 0, -1))


def partial_sorted_data(n: int, sorted_fraction: float = 0.7) -> List[int]:
    """Return a list that is sorted_fraction*100 % sorted, rest shuffled."""
    arr = list(range(1, n + 1))
    split = int(n * sorted_fraction)
    tail = arr[split:]
    random.shuffle(tail)
    return arr[:split] + tail


DATA_GENERATORS = {
    "random":   random_data,
    "ascending":  ascending_data,
    "descending": descending_data,
    "partial":  partial_sorted_data,
}