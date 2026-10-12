import sys
import importlib.util
import unittest
import time


# Function to dynamically load a module from the given file path
def load_module(file_path):
    print(f"Loading module from: {file_path}")
    module_name = file_path.replace(".py", "")
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {file_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Unit test for factors function
class TestPrimeFactors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global module

        if "module" not in globals():
            if len(sys.argv) < 2:
                raise unittest.SkipTest("Please provide a Python module file as an argument.")
            module = load_module(sys.argv[1])

        if hasattr(module, "factors"):
            cls.factors = module.factors
        else:
            raise AttributeError("The module does not contain a 'factors' function.")

    # def test_negative(self):
    #     ts = time.time() 
    #     self.assertEqual(module.factors(-10), [])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test negative")

    # def test_1(self):
    #     ts = time.time() 
    #     self.assertEqual(module.factors(1), [])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 1")

    # def test_2(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(2), [2])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 2")

    # def test_3(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(3), [3])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 3")

    # def test_4(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(4), [2, 2])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 4")

    # def test_6(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(6), [2, 3])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 6")

    # def test_12(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(12), [2, 2, 3])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 12")

    # def test_15(self):
    #     ts = time.time() 
    #     self.assertEqual(module.factors(15), [3, 5])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 15")

    # def test_29(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(29), [29])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 29")

    # def test_30(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(30), [2, 3, 5])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 30")

    # def test_100(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(100), [2, 2, 5, 5])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 100")

    # def test_13195(self):
    #     ts = time.time() 
    #     self.assertEqual(module.factors(13195), [5, 7, 13, 29])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 13195")

    # def test_600851475143(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(600851475143), [71, 839, 1471, 6857])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 600851475143")

    # def test_60(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(60), [2, 2, 3, 5])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 60")

    # def test_1024(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(1024), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test 1024")

    # def test_large_prime_product(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(999979 * 999331), [999331, 999979])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test large_prime_product")

    # def test_repeated_factor(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(999331 * 999331), [999331, 999331])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test repeated_factor")

    # def test_small_and_large_prime_product(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(3 * 999331), [3, 999331])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test small_and_large_prime_product")

    # def test_huge_number_1(self):
    #     ts = time.time()
    #     self.assertEqual(
    #         module.factors(989466010702279110),
    #         [2, 3, 3, 5, 7, 11, 13, 19, 139, 20983, 198193],
    #     )
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test huge_number_1")


    # def test_huge_number_UserGenerated1(self):
    #     ts = time.time()
    #     self.assertEqual(
    #         module.factors(101234),
    #         [2, 7, 7, 1033],
    #     )
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test huge_number_UserGenerated1")

    # def test_huge_number_UserGenerated2(self):
    #     ts = time.time()
    #     self.assertEqual(
    #         module.factors(10012340),
    #         [2, 2, 5, 13, 97, 397],
    #     )
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test huge_number_UserGenerated2")

    def test_large_data(self):
        # Loop through a range of numbers from n = 1 -> 1000000000000 using only 1000 data points for data collection, then print each used number and its time taken to compute its factors.
        n = 1
        while n < 999999999999:
            ts = time.time()
            factors_result = module.factors(n)
            totalTime = time.time() - ts
            print(f"{n},{totalTime},{factors_result}")
            n = n*2  # Increase n by a factor of 2 for the next iteration

    # def test_huge_number_2(self):
    #     ts = time.time()
    #     self.assertEqual(module.factors(9876543210230123456789), [9876543210230123456789])
    #     totalTime = time.time() - ts
    #     print(f"Total time: {totalTime} for test huge_number_2")


# Main entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a Python module file as an argument.")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        module = load_module(file_path)
        print(f"Module loaded: {module.__name__}")
    except Exception as e:
        print(f"Failed to load module: {e}")
        sys.exit(1)

    unittest.main(argv=[sys.argv[0]], exit=False)
