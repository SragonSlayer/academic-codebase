import unittest
# import random
# from bisect import bisect_left


def rank_smallest(A, b, k):

    # Check for invalid inputs. Negative or zero values for b and k are not allowed, and an empty list A should return an empty list.
    if b <= 0:
        raise ValueError("b must be positive")
    if k <= 0 or not A:
        return []

    # if k = 1, Only the rank b element is returned
    elif k == 1:
        pivot = A[len(A) // 2]
        left = [x for x in A if x < pivot]
        right = [x for x in A if x > pivot]
        r = len(left) + 1
        if b == r:
            return [pivot]
        if b < r:
            return rank_smallest(left, b, k)
        # if b > r, search in the right partition with the target rank adjusted by the number of elements removed
        return rank_smallest(right, b - r, k)

    else:
        # if k >= 2, split at the middle target
        mid = (k + 1) // 2
        pivot = rank_smallest(A, mid * b, 1)[0]
        left = [x for x in A if x < pivot]
        right = [x for x in A if x > pivot]

        # recursively find the correct pivot points and combine into one list using the number of targets as the mid point starting
        return (rank_smallest(left, b, mid - 1) + [pivot] + rank_smallest(right, b, k - mid))


class Testing(unittest.TestCase):

    def test_input_k_zero(self):
        self.assertEqual(rank_smallest([4, 1, 3, 2], 2, 0), [])

    def test_input_k_one(self):
        self.assertEqual(rank_smallest([4, 1, 3, 2], 2, 1), [2])

    def test_input_b_one(self):
        self.assertEqual(rank_smallest([4, 1, 3, 2], 1, 4), [1, 2, 3, 4])

    def test_input_kb_equals_n(self):
        self.assertEqual(rank_smallest([4, 1, 3, 2], 2, 2), [2, 4])

    def test_input_sorted_and_reverse_sorted(self):
        self.assertEqual(rank_smallest([1, 2, 3, 4, 5, 6], 2, 3), [2, 4, 6])
        self.assertEqual(rank_smallest([6, 5, 4, 3, 2, 1], 2, 3), [2, 4, 6])

    def test_input_randomized(self):
        import random

        for _ in range(10):
            n = random.randint(1, 20)
            A = random.sample(range(1, 100), n)
            b = random.randint(1, n)
            k = random.randint(0, n // b + 1)

            expected = sorted(A)[b - 1::b][:k]
            result = rank_smallest(A, b, k)
            self.assertEqual(result, expected)   


if __name__ == "__main__":
    unittest.main()
