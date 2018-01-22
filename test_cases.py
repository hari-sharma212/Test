import unittest

from test import no_century


class MyTests(unittest.TestCase):
    def test_century(self):
        json_data = json.dumps([
            ["Pakistan", 23],
            ["Pakistan", 127],
            ["India", 3],
            ["India", 71],
            ["Australia", 311],
            ["India", 22],
            ["Pakistan", 81]
        ])
        res = no_century(json_data)
        self.assertEquals(1, res)

    def test_century_with_two(self):
        json_data = json.dumps([
            ["Pakistan", 23],
            ["Pakistan", 27],
            ["India", 3],
            ["India", 71],
            ["Australia", 311],
            ["India", 22],
            ["Pakistan", 81]
        ])
        res = no_century(json_data)
        self.assertEquals(2, res)


