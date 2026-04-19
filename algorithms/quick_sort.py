import random
from typing import List
from metrics.counter import SortMetrics


def quick_sort(arr: List[int], metrics: SortMetrics) -> List[int]:
    data = arr[:]
    _quick_sort(data, 0, len(data) - 1, metrics)
    return data


def _median_of_three(arr: List[int], lo: int, hi: int, metrics: SortMetrics) -> int:
    mid = (lo + hi) // 2
    metrics.compare()
    if arr[lo] > arr[mid]:
        arr[lo], arr[mid] = arr[mid], arr[lo]
        metrics.swap()
    metrics.compare()
    if arr[lo] > arr[hi]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        metrics.swap()
    metrics.compare()
    if arr[mid] > arr[hi]:
        arr[mid], arr[hi] = arr[hi], arr[mid]
        metrics.swap()
    arr[mid], arr[hi - 1] = arr[hi - 1], arr[mid]
    metrics.swap()
    return arr[hi - 1]


def _quick_sort(arr: List[int], lo: int, hi: int, metrics: SortMetrics) -> None:
    if lo >= hi:
        return

    if hi - lo < 2:    
        metrics.compare()
        if arr[lo] > arr[hi]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            metrics.swap()
        return

    pivot = _median_of_three(arr, lo, hi, metrics)
    i, j = lo, hi - 1

    while True:
        i += 1
        while i < hi:
            metrics.compare()
            if arr[i] >= pivot:
                break
            i += 1
        j -= 1
        while j > lo:
            metrics.compare()
            if arr[j] <= pivot:
                break
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        metrics.swap()

    arr[i], arr[hi - 1] = arr[hi - 1], arr[i]
    metrics.swap()
    _quick_sort(arr, lo, i - 1, metrics)
    _quick_sort(arr, i + 1, hi, metrics)