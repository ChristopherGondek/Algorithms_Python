import unittest
import random

import randomized_select
import time


class SelectTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_range_median(self):
        n = 100000
        k = n//2
        data = list(range(n))
        random.shuffle(data)

        r1 = randomized_select.randomized_select_loop(data[:], k)

        data.sort()
        r2 = data[k]

        self.assertTrue(r1 == r2)

    def test_range_zero(self):
        n = 100000
        k = 0
        data = list(range(n))
        random.shuffle(data)

        r1 = randomized_select.randomized_select_loop(data[:], k)

        data.sort()
        r2 = data[k]

        self.assertTrue(r1 == r2)

    def test_range_length(self):
        n = 100000
        k = n-1
        data = list(range(n))
        random.shuffle(data)

        r1 = randomized_select.randomized_select_loop(data[:], k)

        data.sort()
        r2 = data[k]

        self.assertTrue(r1 == r2)

    def test_dense_list(self):
        n = 100000
        k = n//2
        data = [random.randint(0, 9) for _ in range(0, n)]

        r1 = randomized_select.randomized_select_loop(data[:], k)

        data.sort()
        r2 = data[k]

        self.assertTrue(r1 == r2)

    def test_sparse_list(self):
        n = 1000
        k = n//2
        data = [random.randint(0, 1000000) for _ in range(0, n)]

        r1 = randomized_select.randomized_select_loop(data[:], k)

        data.sort()
        r2 = data[k]

        self.assertTrue(r1 == r2)

    def test_same_list(self):
        n = 1000
        k = n//2
        data = [1]*n

        r1 = randomized_select.randomized_select_loop(data[:], k)

        data.sort()
        r2 = data[k]

        self.assertTrue(r1 == r2)

    def test_performance(self):

        n = 500000
        k = n//2
        arr = list(range(n))
        random.shuffle(arr)

        start = time.time()
        r1 = randomized_select.randomized_select_loop(arr, k)
        print('\n' + 'Time for randomized select: '.ljust(30) + '{0:05f}'.format(time.time() - start) + ' seconds')

        start = time.time()
        arr.sort()
        r2 = arr[k]
        print('Time for sort and select: '.ljust(30) + '{0:05f}'.format(time.time() - start) + ' seconds')

        self.assertTrue(r1 == r2)


def main():
    unittest.main()


if __name__ == '__main__':
    main()