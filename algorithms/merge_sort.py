from typing import List
from metrics.counter import SortMetrics


def merge_sort(arr: List[int], metrics: SortMetrics) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], metrics)
    right = merge_sort(arr[mid:], metrics)
    return _merge(left, right, metrics)


def _merge(left: List[int], right: List[int], metrics: SortMetrics) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        metrics.compare()
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            metrics.swap()
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result