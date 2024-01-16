from data import DATA
import l
import sys
import ast
import unittest
from unittest.mock import patch
from num import NUM
from config import the
from sym import SYM


class TestBase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        the["seed"] = 23456  # Resetting Seed
        the["cache"] = {}   # Resetting config cache

    def tearDown(cls):
        the["seed"] = None
        the["cache"] = None


class TestDataStats(TestBase):

    def setUp(self):
        self.data = DATA("../data/auto93.csv")

    def test_stats(self):
        result = l.sort_string(l.o(self.data.stats()))
        expected_result = "{.N: 398, Acc+: 15.57, Lbs-: 2970.42, Mpg+: 23.84}"
        self.assertEqual(result, expected_result)


class TestDataColumns(TestBase):

    def setUp(self):
        self.data = DATA("../data/auto93.csv")

    def test_columns(self):
        expected = 8
        actual = len(self.data.cols.all)
        self.assertEqual(actual, expected)


class TestDataDependent(TestBase):

    def setUp(self):
        self.data = DATA("../data/auto93.csv")

    def test_dependent(self):
        expected = 3
        actual = len(self.data.cols.y)
        self.assertEqual(actual, expected)


class TestDataIndependent(TestBase):

    def setUp(self):
        self.data = DATA("../data/auto93.csv")

    def test_independent(self):
        expected = 4
        actual = len(self.data.cols.x)
        self.assertEqual(actual, expected)


class TestNum(TestBase):

    def setUp(self):
        self.num_obj = NUM()

    def test_add(self):
        self.num_obj.add(5)
        self.assertEqual(self.num_obj.mu, 5.0)

    def test_mid(self):
        self.num_obj.add(5)
        self.num_obj.add(10)
        self.assertEqual(self.num_obj.mid(), 7.5)

    def test_div(self):
        self.num_obj.add(1)
        self.assertEqual(self.num_obj.div(), 0)


class TestSYM(TestBase):

    def setUp(self):
        self.sym_obj = SYM()

    def test_add(self):
        self.sym_obj.add("A")
        self.assertEqual(self.sym_obj.n, 1)
        self.assertEqual(self.sym_obj.has["A"], 1)
        self.assertEqual(self.sym_obj.mode, "A")

    def test_add_multiple_values(self):
        values = ["A", "B", "A", "C", "B", "A"]
        for value in values:
            self.sym_obj.add(value)
        self.assertEqual(self.sym_obj.n, len(values))
        self.assertEqual(self.sym_obj.has["A"], 3)
        self.assertEqual(self.sym_obj.has["B"], 2)
        self.assertEqual(self.sym_obj.has["C"], 1)
        self.assertEqual(self.sym_obj.mode, "A")

    def test_mid(self):
        self.sym_obj.add("A")
        self.assertEqual(self.sym_obj.mid(), 0)


def run_test(test_case):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    run_test(TestDataStats)
    run_test(TestDataColumns)
    run_test(TestDataDependent)
    run_test(TestDataIndependent)
    run_test(TestNum)
    run_test(TestSYM)
