import random
import unittest
from prog985t import Mergesort
from time import perf_counter as current_time


class TestMergesort(unittest.TestCase):
      def setUp(self):
          self.startTime = current_time()

      def tearDown(self):
          t = current_time() - self.startTime
          print(f"{self.id()}: {t:.6f}")

      def test_normal_case(self):
        input = [4, 2, 5, 1, 3]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(Mergesort.sort(input), expected_output)

      def test_empty_list(self):
        input = []
        expected_output = []
        self.assertEqual(Mergesort.sort(input), expected_output)

      def test_single_element(self):
        input = [1]
        expected_output = [1]
        self.assertEqual(Mergesort.sort(input), expected_output)

      def test_identical_elements(self):
        input = [5, 5, 5, 5]
        expected_output = [5, 5, 5, 5]
        self.assertEqual(Mergesort.sort(input), expected_output)

      def test_negative_numbers(self):
        input = [-3, -1, -4, -2]
        expected_output = [-4, -3, -2, -1]
        self.assertEqual(Mergesort.sort(input), expected_output)

      def test_mixed_types(self):
        input = [3.2, 1.5, 4.8, 2.1]
        expected_output = [1.5, 2.1, 3.2, 4.8]
        self.assertEqual(Mergesort.sort(input), expected_output)

      def test_performance_large_dataset(self):
        input = generate_large_list()
        start_time = current_time()
        Mergesort.sort(input)
        end_time = current_time()
        self.assertLess(end_time-start_time, 10)




def generate_large_list():
  return[random.randint(0, 10_000_000) for i in   range(1_000_000)]
  #     self.assertEqual(methodcall, expectedvalue)


if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestMergesort)
  unittest.TextTestRunner(verbosity=0).run(suite)



