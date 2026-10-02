"""TSP solver. Baseline: nearest neighbor from city 0.

Improvement ladder (suggestions, not limits): 2-opt, or-opt, better starts,
Lin-Kernighan-style moves. `solve` must return a permutation of range(n).
"""

from __future__ import annotations

import numpy as np


def solve(coords: np.ndarray) -> list[int]:
    """Return a tour visiting every city exactly once."""
    n = coords.shape[0]
    best_tour = None
    best_length = float('inf')

    for start in range(min(n, 20)):
        tour = _nearest_neighbor(coords, start)
        length = _tour_length(coords, tour)
        if length < best_length:
            best_length = length
            best_tour = tour

    return best_tour


def _nearest_neighbor(coords: np.ndarray, start: int) -> list[int]:
    """Greedy nearest-neighbor tour starting from a given city."""
    n = coords.shape[0]
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    while unvisited:
        cur = coords[tour[-1]]
        nxt = min(unvisited, key=lambda j: float(np.sum((coords[j] - cur) ** 2)))
        tour.append(nxt)
        unvisited.remove(nxt)
    return tour


def _tour_length(coords: np.ndarray, tour: list[int]) -> float:
    """Compute total Euclidean tour length."""
    ordered = coords[np.array(tour)]
    diffs = ordered - np.roll(ordered, -1, axis=0)
    return float(np.sum(np.sqrt(np.sum(diffs**2, axis=1))))
