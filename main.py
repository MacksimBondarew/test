import sys
import os
import argparse

sys.path.insert(0, os.path.dirname(__file__))

from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort
from benchmark.runner import (
    run_benchmark,
    print_results,
    print_complexity_estimate,
    DEFAULT_SIZES,
)
from data.generator import DATA_GENERATORS

ALGORITHMS = {
    "MergeSort": merge_sort,
    "QuickSort": quick_sort,
    "HeapSort":  heap_sort,
}

# Mark algorithms that should be skipped for very large n
IS_SLOW = {
    "MergeSort": False,
    "QuickSort": False,
    "HeapSort":  False,
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Experimental sorting algorithm complexity analyser"
    )
    parser.add_argument(
        "--sizes", nargs="+", type=int, default=DEFAULT_SIZES,
        metavar="N",
        help="Input sizes to test (default: 100 500 1000 5000 10000 50000 100000)",
    )
    parser.add_argument(
        "--dtype", nargs="+", default=list(DATA_GENERATORS.keys()),
        choices=list(DATA_GENERATORS.keys()),
        metavar="TYPE",
        help=f"Data types to test: {list(DATA_GENERATORS.keys())}",
    )
    parser.add_argument(
        "--no-complexity", action="store_true",
        help="Skip the empirical complexity estimation table",
    )
    return parser.parse_args()

def main():
    args = parse_args()

    print("\n" + "=" * 90)
    print("  SORTING ALGORITHM COMPLEXITY ANALYSER")
    print("=" * 90)
    print(f"  Algorithms : {', '.join(ALGORITHMS)}")
    print(f"  Sizes      : {args.sizes}")
    print(f"  Data types : {args.dtype}")
    print("=" * 90)

    rows = run_benchmark(
        algorithms=ALGORITHMS,
        sizes=sorted(args.sizes),
        data_types=args.dtype,
        is_slow=IS_SLOW,
    )

    print_results(rows)

    if not args.no_complexity:
        print_complexity_estimate(rows)

    print("\n" + "=" * 90 + "\n")


if __name__ == "__main__":
    main()