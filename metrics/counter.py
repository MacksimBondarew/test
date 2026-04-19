class SortMetrics:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.elapsed_ms = 0.0

    def reset(self):
        self.comparisons = 0
        self.swaps = 0
        self.elapsed_ms = 0.0

    def compare(self) -> None:
        self.comparisons += 1

    def swap(self) -> None:
        self.swaps += 1

    def __repr__(self):
        return (
            f"SortMetrics(comparisons={self.comparisons}, "
            f"swaps={self.swaps}, elapsed_ms={self.elapsed_ms:.4f})"
        )