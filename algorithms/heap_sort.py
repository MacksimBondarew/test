from typing import List
from metrics.counter import SortMetrics


def heap_sort(arr: List[int], metrics: SortMetrics) -> List[int]:
    data = arr[:]
    n = len(data)

    # Build max-heap (start from last non-leaf)
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(data, i, n, metrics)

    # Extract elements one by one
    for end in range(n - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        metrics.swap()
        _sift_down(data, 0, end, metrics)

    return data


def _sift_down(arr: List[int], root: int, size: int, metrics: SortMetrics) -> None:
    while True:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < size:
            metrics.compare()
            if arr[left] > arr[largest]:
                largest = left

        if right < size:
            metrics.compare()
            if arr[right] > arr[largest]:
                largest = right

        if largest == root:
            break

        arr[root], arr[largest] = arr[largest], arr[root]
        metrics.swap()
        root = largest