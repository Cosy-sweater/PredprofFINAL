import unittest
import requests
from request_api import room_info, days_info


class TestReverse(unittest.TestCase):
    def test_empty_d_i(self):
        self.assertEqual(type(days_info()), list)
        datas = days_info()
        print("Это unittest -", datas)

    def test_empty_r_i(self):
        with self.assertRaises(RuntimeError):
            room_info('', '', '')

    def test_room_exist_data(self):
        self.assertEqual(type(room_info("25", "01", "23")), dict)

        datas = days_info()
        for day in range(0, 21, 6):
            for month in range(0, 13, 6):
                for year in range(60, -1, -12):
                    data = '-'.join([f"{day}".rjust(2, '0'), f"{month}".rjust(2, '0'), f"{year}".rjust(2, '0')])
                    if data not in datas:
                        with self.assertRaises(RuntimeError):
                            room_info(data[:2], data[3:5], data[6:8])
                        print(data)

    def test_room_no_exist_data(self):
        with self.assertRaises(RuntimeError):
            room_info("95", "011", "23")

    def test_wrong_format(self):
        with self.assertRaises(RuntimeError):
            room_info([42, 1, 24])
        with self.assertRaises(RuntimeError):
            room_info('0014')
        with self.assertRaises(RuntimeError):
            room_info(10, 3, 45)
        with self.assertRaises(RuntimeError):
            room_info(*[42, 1, 24])
        with self.assertRaises(RuntimeError):
            room_info({'d': 11, 'm': 11, 'y': 11})


if __name__ == '__main__':
    unittest.main()
