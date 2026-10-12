import unittest
import random
from bisect import bisect_left


def rank_smallest(A, b, k):
    # If k == 0, return an empty list
    if k == 0:
        return []

    # 
    targets = list(range(b - 1, k * b, b))
    result = {}

    def find_targets(part, start, wanted):
        if not wanted:
            return

        # pivot = random.choice(part)
        pivot = part[len(part) // 2]
        lower = [x for x in part if x < pivot]
        higher = [x for x in part if x > pivot]

        pivot_index = start + len(lower)
        split = bisect_left(wanted, pivot_index)

        # Record the pivot if it has a requested rank.
        if split < len(wanted) and wanted[split] == pivot_index:
            result[pivot_index] = pivot
            right_wanted = wanted[split + 1:]
        else:
            right_wanted = wanted[split:]

        find_targets(lower, start, wanted[:split])
        find_targets(higher, pivot_index + 1, right_wanted)

    find_targets(list(A), 0, targets)
    return [result[i] for i in targets]


# def rank_smallest(A, b, k):
#     if (k == 0):
#         return []
#     else:
#         return [0]

def rank_smallest_2(A, b, k):
    """Return the elements of A with ranks b, 2b, ..., kb, in sorted order.
    Divide and conquer by partitioning; no sorting; A is not modified."""

    def solve(arr, targets):
        # targets: increasing list of 1-based ranks within arr
        if not targets:
            return []

        pivot = arr[random.randrange(len(arr))]
        left = [x for x in arr if x < pivot]      # new lists, so A is never changed
        right = [x for x in arr if x > pivot]
        r = len(left) + 1                         # rank of the pivot within arr

        left_targets = [t for t in targets if t < r]
        right_targets = [t - r for t in targets if t > r]
        pivot_hit = [pivot] if r in targets else []

        # Left results < pivot < right results, so the output is already in order
        return solve(left, left_targets) + pivot_hit + solve(right, right_targets)

    return solve(list(A), [i * b for i in range(1, k + 1)])

def rank_smallest_3(A, b, k):
    """Return the elements of A with ranks b, 2b, ..., kb, in sorted order.
    Divide and conquer by partitioning; no sorting; A is not modified."""
    if k == 0:
        return []

    if k == 1:
        # Quickselect for the element of rank b
        pivot = A[random.randrange(len(A))]
        left = [x for x in A if x < pivot]          # new lists: A is not modified
        right = [x for x in A if x > pivot]
        r = len(left) + 1                           # rank of pivot in A
        if b == r:
            return [pivot]
        if b < r:
            return rank_smallest(left, b, 1)
        return rank_smallest(right, b - r, 1)

    # k >= 2: split at the middle target, whose rank is a multiple of b
    mid = (k + 1) // 2
    pivot = rank_smallest(A, mid * b, 1)[0]         # element of rank mid*b
    left = [x for x in A if x < pivot]              # holds targets b, ..., (mid-1)b
    right = [x for x in A if x > pivot]             # targets become b, ..., (k-mid)b

    return (rank_smallest(left, b, mid - 1)
            + [pivot]
            + rank_smallest(right, b, k - mid))


class Testing(unittest.TestCase):
    def test_dummytest(self):
        self.assertEqual(rank_smallest([4, 1, 3, 2], 2, 0), [])

    def test_input(self):
        # k = 0: no ranks requested
        self.assertEqual(rank_smallest([4, 1, 3, 2], 2, 0), [])

        # k = 1: return only the element at rank b
        self.assertEqual(rank_smallest([4, 1, 3, 2], 2, 1), [2])

        # b = 1: return every element, in sorted order
        self.assertEqual(rank_smallest([4, 1, 3, 2], 1, 4), [1, 2, 3, 4])

        # kb = n: the last requested rank is the largest element
        self.assertEqual(rank_smallest([4, 1, 3, 2], 2, 2), [2, 4])

        # Already sorted and reverse-sorted inputs
        self.assertEqual(rank_smallest([1, 2, 3, 4, 5, 6], 2, 3), [2, 4, 6])
        self.assertEqual(rank_smallest([6, 5, 4, 3, 2, 1], 2, 3), [2, 4, 6])


if __name__ == "__main__":
    unittest.main()
