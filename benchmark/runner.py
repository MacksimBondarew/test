import sys
import time
import math
from typing import Callable, List, Dict, Any

from metrics.counter import SortMetrics
from data.generator import DATA_GENERATORS

DEFAULT_SIZES = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000]

SLOW_ALGO_LIMIT = 10_000

def measure(
    sort_fn: Callable[[List[int], SortMetrics], List[int]],
    data: List[int],
) -> SortMetrics:
    m = SortMetrics()
    start = time.perf_counter()
    result = sort_fn(data[:], m)   # always pass a copy
    m.elapsed_ms = (time.perf_counter() - start) * 1000.0

    # Sanity-check correctness
    if result != sorted(data):
        raise RuntimeError(f"{sort_fn.__name__} produced incorrect output!")
    return m



def run_benchmark(
    algorithms: Dict[str, Callable],
    sizes: List[int] = None,
    data_types: List[str] = None,
    is_slow: Dict[str, bool] = None,
) -> List[Dict[str, Any]]:
    """
    Run all (algorithm × size × data_type) combinations.
    Returns a list of result dicts.
    """
    if sizes is None:
        sizes = DEFAULT_SIZES
    if data_types is None:
        data_types = list(DATA_GENERATORS.keys())
    if is_slow is None:
        is_slow = {}

    rows = []

    for dtype in data_types:
        gen_fn = DATA_GENERATORS[dtype]
        print(f"\n  Data type: {dtype.upper()}")
        print("  " + "-" * 70)

        for n in sizes:
            data = gen_fn(n)

            for name, fn in algorithms.items():
                # Skip huge inputs for known O(n²) algorithms
                if is_slow.get(name, False) and n > SLOW_ALGO_LIMIT:
                    rows.append({
                        "algorithm": name, "n": n, "data_type": dtype,
                        "elapsed_ms": None, "comparisons": None, "swaps": None,
                    })
                    continue

                try:
                    m = measure(fn, data)
                    rows.append({
                        "algorithm": name,
                        "n": n,
                        "data_type": dtype,
                        "elapsed_ms": m.elapsed_ms,
                        "comparisons": m.comparisons,
                        "swaps": m.swaps,
                    })
                except RecursionError:
                    rows.append({
                        "algorithm": name, "n": n, "data_type": dtype,
                        "elapsed_ms": None, "comparisons": None, "swaps": None,
                    })

    return rows


def _fmt(val, unit=""):
    if val is None:
        return "  —  "
    if isinstance(val, float):
        return f"{val:>10.3f}{unit}"
    return f"{val:>12,}"


def print_results(rows: List[Dict[str, Any]]) -> None:
    """Print results as a formatted table grouped by data type."""
    from itertools import groupby

    # Group by data_type
    data_types = sorted(set(r["data_type"] for r in rows))
    algorithms = list(dict.fromkeys(r["algorithm"] for r in rows))

    for dtype in data_types:
        subset = [r for r in rows if r["data_type"] == dtype]
        sizes = sorted(set(r["n"] for r in subset))

        print(f"\n{'═'*90}")
        print(f"  Data type: {dtype.upper()}")
        print(f"{'═'*90}")

        # Header
        algo_w = max(len(a) for a in algorithms) + 2
        print(f"  {'n':>8}   {'Algorithm':<{algo_w}}  {'Time (ms)':>12}  "
              f"{'Comparisons':>14}  {'Swaps':>12}")
        print("  " + "─" * 70)

        for n in sizes:
            for i, algo in enumerate(algorithms):
                r = next((x for x in subset if x["n"] == n and x["algorithm"] == algo), None)
                if r is None:
                    continue
                n_str = f"{n:>8,}" if i == 0 else " " * 8
                print(
                    f"  {n_str}   {algo:<{algo_w}}"
                    f"  {_fmt(r['elapsed_ms'], ' ms')}"
                    f"  {_fmt(r['comparisons'])}"
                    f"  {_fmt(r['swaps'])}"
                )
            if sizes.index(n) < len(sizes) - 1:
                print("  " + "·" * 70)


def print_complexity_estimate(rows: List[Dict[str, Any]]) -> None:
    print(f"\n{'═'*90}")
    print("  Empirical complexity estimate (log-log slope between consecutive sizes)")
    print(f"{'═'*90}")
    print(f"  {'Algorithm':<20} {'Data type':<14} {'n1':>8}  {'n2':>8}  {'slope':>8}  {'est. class'}")
    print("  " + "─" * 70)

    algorithms = list(dict.fromkeys(r["algorithm"] for r in rows))
    data_types = list(dict.fromkeys(r["data_type"] for r in rows))

    for algo in algorithms:
        for dtype in data_types:
            subset = sorted(
                [r for r in rows if r["algorithm"] == algo and r["data_type"] == dtype
                 and r["elapsed_ms"] is not None and r["elapsed_ms"] > 0],
                key=lambda x: x["n"]
            )
            if len(subset) < 2:
                continue
            # Use last two data points for the slope
            r1, r2 = subset[-2], subset[-1]
            try:
                slope = math.log(r2["elapsed_ms"] / r1["elapsed_ms"]) / math.log(r2["n"] / r1["n"])
            except (ZeroDivisionError, ValueError):
                continue

            if slope < 1.2:
                est = "O(n)  or O(n log n)"
            elif slope < 1.8:
                est = "O(n log n)"
            elif slope < 2.3:
                est = "O(n²)"
            else:
                est = "worse than O(n²)"

            print(
                f"  {algo:<20} {dtype:<14} {r1['n']:>8,}  {r2['n']:>8,}  {slope:>8.2f}  {est}"
            )