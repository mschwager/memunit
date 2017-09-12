#!/usr/bin/env python

import unittest

try:
    from unittest import mock
except ImportError:
    # Python 2
    import mock

import memunit


class TestMemunit(unittest.TestCase):
    def test_assert_lt_mb_less_than(self):
        memunit.PROFILER = mock.MagicMock(return_value=([9], True))

        @memunit.assert_lt_mb(10)
        def func():
            return True

        self.assertTrue(func())

    def test_assert_lt_mb_greater_than(self):
        memunit.PROFILER = mock.MagicMock(return_value=([11], True))

        @memunit.assert_lt_mb(10)
        def func():
            return True

        with self.assertRaisesRegexp(memunit.MemoryUsageException, '>='):
            func()

    def test_assert_lt_mb_equal_to(self):
        memunit.PROFILER = mock.MagicMock(return_value=([10], True))

        @memunit.assert_lt_mb(10)
        def func():
            return True

        with self.assertRaisesRegexp(memunit.MemoryUsageException, '>='):
            func()

    def test_assert_le_mb_less_than(self):
        memunit.PROFILER = mock.MagicMock(return_value=([9], True))

        @memunit.assert_le_mb(10)
        def func():
            return True

        self.assertTrue(func())

    def test_assert_le_mb_greater_than(self):
        memunit.PROFILER = mock.MagicMock(return_value=([11], True))

        @memunit.assert_le_mb(10)
        def func():
            return True

        with self.assertRaisesRegexp(memunit.MemoryUsageException, '>'):
            func()

    def test_assert_le_mb_equal_to(self):
        memunit.PROFILER = mock.MagicMock(return_value=([10], True))

        @memunit.assert_le_mb(10)
        def func():
            return True

        self.assertTrue(func())

    def test_assert_eq_mb_equal_to(self):
        memunit.PROFILER = mock.MagicMock(return_value=([10], True))

        @memunit.assert_eq_mb(10)
        def func():
            return True

        self.assertTrue(func())

    def test_assert_eq_mb_not_equal_to(self):
        memunit.PROFILER = mock.MagicMock(return_value=([11], True))

        @memunit.assert_eq_mb(10)
        def func():
            return True

        with self.assertRaisesRegexp(memunit.MemoryUsageException, '!='):
            func()

    def test_assert_ne_mb_equal_to(self):
        memunit.PROFILER = mock.MagicMock(return_value=([10], True))

        @memunit.assert_ne_mb(10)
        def func():
            return True

        with self.assertRaisesRegexp(memunit.MemoryUsageException, '=='):
            func()

    def test_assert_ne_mb_not_equal_to(self):
        memunit.PROFILER = mock.MagicMock(return_value=([11], True))

        @memunit.assert_ne_mb(10)
        def func():
            return True

        self.assertTrue(func())

    def test_assert_ge_mb_less_than(self):
        memunit.PROFILER = mock.MagicMock(return_value=([9], True))

        @memunit.assert_ge_mb(10)
        def func():
            return True

        with self.assertRaisesRegexp(memunit.MemoryUsageException, '<'):
            func()

    def test_assert_ge_mb_greater_than(self):
        memunit.PROFILER = mock.MagicMock(return_value=([11], True))

        @memunit.assert_ge_mb(10)
        def func():
            return True

        self.assertTrue(func())

    def test_assert_ge_mb_equal_to(self):
        memunit.PROFILER = mock.MagicMock(return_value=([10], True))

        @memunit.assert_ge_mb(10)
        def func():
            return True

        self.assertTrue(func())

    def test_assert_gt_mb_less_than(self):
        memunit.PROFILER = mock.MagicMock(return_value=([9], True))

        @memunit.assert_gt_mb(10)
        def func():
            return True

        with self.assertRaisesRegexp(memunit.MemoryUsageException, '<='):
            func()

    def test_assert_gt_mb_greater_than(self):
        memunit.PROFILER = mock.MagicMock(return_value=([11], True))

        @memunit.assert_gt_mb(10)
        def func():
            return True

        self.assertTrue(func())

    def test_assert_gt_mb_equal_to(self):
        memunit.PROFILER = mock.MagicMock(return_value=([10], True))

        @memunit.assert_gt_mb(10)
        def func():
            return True

        with self.assertRaisesRegexp(memunit.MemoryUsageException, '<='):
            func()


if __name__ == "__main__":
    unittest.main()
