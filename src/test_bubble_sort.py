import unittest

from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_sorted_Array(self):
        array = [1,2,3,4,5,6,7,8,9]
        self.assertListEqual(
            array,
            bubble_sort(array)
        )

    def test_sorting_first_digit(self):
        unsorted_array = [9,2,3,4,5,6,7,8,1]
        sorted_array = [1,2,3,4,5,6,7,8,9]
        self.assertListEqual(
            sorted_array,
            bubble_sort(unsorted_array)
        )

    def test_empty_array(self):
        array = []
        self.assertListEqual(
            array,
            bubble_sort(array)
        )


    def test_unsorted_multiple_indeces(self):
        array = [29, 72, 98, 13, 87, 66, 52, 51, 36, 21, 75, 4, 88, 58, 46, 31, 55, 74, 19, 8]
        sorted = [4, 8, 13, 19, 21, 29, 31, 36, 46, 51, 52, 55, 58, 66, 72, 74, 75, 87, 88, 98]
        self.assertListEqual(
            sorted,
            bubble_sort(array)
        )

    def test_reveres_order(self):
        array = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertListEqual(
            sorted,
            bubble_sort(array)
        )

    def test_single_element(self):
        array = [7]
        self.assertListEqual(
            array,
            bubble_sort(array)
        )
