import unittest

class TestTime(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # Extract the Python code and import the package
        from tests.utils.extractPython import extractPy
        extractPy('game/src/py/Time.rpy', 'tests/src/')
        global Time
        from tests.src.Time import Time

    def test_advanceTime(self):
        time = Time(hour=17, minute=30)
        time.advanceTime()
        self.assertEqual(time, Time(17, 32))

    def test_time_comparison_operators(self):

        time1 = Time(hour=17, minute=30)
        time2 = Time(hour=17, minute=31)
        time3 = Time(hour=18, minute=30)
        time4 = Time(hour=17, minute=31)
        time5 = Time(hour=1, minute=30, day=2)


        self.assertTrue(time1 < time2)
        self.assertTrue(time1 <= time2)
        self.assertFalse(time1 == time2)
        self.assertFalse(time1 >= time2)
        self.assertFalse(time1 > time2)

        self.assertTrue(time1 < time3)
        self.assertTrue(time1 <= time3)
        self.assertFalse(time1 == time3)
        self.assertFalse(time1 >= time3)
        self.assertFalse(time1 > time3)

        self.assertTrue(time2 < time3)
        self.assertTrue(time2 <= time3)
        self.assertFalse(time2 == time3)
        self.assertFalse(time2 >= time3)
        self.assertFalse(time2 > time3)

        self.assertFalse(time2 < time1)
        self.assertFalse(time2 <= time1)
        self.assertFalse(time2 == time1)
        self.assertTrue(time2 >= time1)
        self.assertTrue(time2 > time1)

        self.assertFalse(time3 < time2)
        self.assertFalse(time3 <= time2)
        self.assertFalse(time3 == time2)
        self.assertTrue(time3 >= time2)
        self.assertTrue(time3 > time2)

        self.assertFalse(time4 < time2)
        self.assertTrue(time4 <= time2)
        self.assertTrue(time4 == time2)
        self.assertTrue(time4 >= time2)
        self.assertFalse(time4 > time2)

        self.assertTrue(time1 < time5)
        self.assertTrue(time1 <= time5)
        self.assertFalse(time1 == time5)
        self.assertFalse(time1 >= time5)
        self.assertFalse(time1 > time5)


if __name__ == '__main__':
    unittest.main()