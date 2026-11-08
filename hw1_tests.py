"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

from data import Price, Point, Circle, Rectangle, Book, Employee
from hw1 import vowel_count, short_lists, ascending_pairs, add_prices, rectangle_area, books_by_author,circle_bound, below_pay_average


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(vowel_count("Apple"),2)
        
    def test_vowel_count_empty_string(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(vowel_count(""),0)
        
    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        self.assertEqual(short_lists([[2, 3,4], [7, 8,4,5]]), [])

    def test_short_lists_no_matching_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        self.assertEqual(short_lists([[1], [2, 3], [], [4, 5, 6], [7, 8]]), [[2, 3], [7, 8]])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(ascending_pairs([[9, 2], [3, 1, 2], [5, 5]]), [[2, 9], [3, 1, 2], [5, 5]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(ascending_pairs([[5,9,10], [9,10,11],[5,6,7]]), [[5,9,10], [9,10,11],[5,6,7]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(add_prices(Price(3, 0), Price(4,0)), Price(7,0))

    def test_add_prices_with_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(add_prices(Price(3, 75), Price(2, 50)), Price(6, 25))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(rectangle_area(Rectangle(Point(3,5), Point(0,0))), 15)

    def test_rectangle_area_negative_coordinates(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(rectangle_area(Rectangle(Point(-1,5), Point(0,0))), 5)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        books=[Book(["Tolstoy"], "Death of Ivan Illyich"), Book(["Jane Austen"], "Pride and Predjudice")]
        self.assertEqual(books_by_author("Tolstoy", books), [Book(["Tolstoy"], "Death of Ivan Illyich")])

    def test_books_by_author_no_matches(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        books=[Book(["Tolstoy"], "Death of Ivan Illyich"), Book(["Jane Austen"], "Pride and Predjudice")]
        self.assertEqual(books_by_author("Dovensky", books),[])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        rect = Rectangle(Point(0, 0), Point(6, 8))
        result = circle_bound(rect)
        self.assertEqual(result.center, Point(3.0, 4.0))

    def test_circle_bound_non_square_rectangle(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        rect = Rectangle(Point(-4, -2), Point(0, 4))
        result = circle_bound(rect)
        self.assertEqual(result.center, Point(-2.0, 1.0))
    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        employees = [Employee("Alice", 20.0),Employee("Bob", 30.0),Employee("Charlie", 40.0)]
        self.assertEqual(below_pay_average(employees), ["Alice"])

    def test_below_pay_average_empty_list(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        employees = []
        self.assertEqual(below_pay_average(employees), [])


if __name__ == '__main__':
    unittest.main()
