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
