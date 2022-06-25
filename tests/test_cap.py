import unittest
import sys
sys.path.append('../')
from src.driver import startApp

class TestCap(unittest.TestCase):
    
    def test_result1(self):
        input_data = [
            'LOAN IDIDI Dale 10000 5 4', 
            'LOAN MBI Harry 2000 2 2', 
            'BALANCE IDIDI Dale 5',
            'BALANCE IDIDI Dale 40', 
            'BALANCE MBI Harry 12', 
            'BALANCE MBI Harry 0'
            ]
        result = startApp(input_data)
        self.assertEqual(result, [
            ['IDIDI', 'Dale', 1000, 55], 
            ['IDIDI', 'Dale', 8000, 20], 
            ['MBI', 'Harry', 1044, 12], 
            ['MBI', 'Harry', 0, 24]
            ]
        )

    def test_result2(self):
        input_data = [
            'LOAN IDIDI Dale 5000 1 6',
            'LOAN MBI Harry 10000 3 7',
            'LOAN UON Shelly 15000 2 9',
            'PAYMENT IDIDI Dale 1000 5',
            'PAYMENT MBI Harry 5000 10',
            'PAYMENT UON Shelly 7000 12',
            'BALANCE IDIDI Dale 3',
            'BALANCE IDIDI Dale 6',
            'BALANCE UON Shelly 12',
            'BALANCE MBI Harry 12',
        ]
        result = startApp(input_data)
        self.assertEqual(result, [
            ['IDIDI', 'Dale', 1326, 9], 
            ['IDIDI', 'Dale', 3652, 4], 
            ['UON', 'Shelly', 15856, 3], 
            ['MBI', 'Harry', 9044, 10]
            ]
        )

    def test_result3(self):
        input_data = [
            'LOAN IDIDI Dale 4000 3 4',
            'LOAN MBI Dale 10000 3 7',
            'PAYMENT MBI Dale 2000 0',
            'BALANCE IDIDI Dale 3',
            'BALANCE IDIDI Dale 0',
            'BALANCE MBI Dale 0',
            'BALANCE IDIDI Dale 12',
            'BALANCE MBI Dale 4',
            'BALANCE MBI Dale 30',
        ]
        result = startApp(input_data)
        self.assertEqual(result, [
            ['IDIDI', 'Dale', 375, 33], 
            ['IDIDI', 'Dale', 0, 36], 
            ['MBI', 'Dale', 2000, 30], 
            ['IDIDI', 'Dale', 1500, 24],
            ['MBI', 'Dale', 3348, 26],
            ['MBI', 'Dale', 12100, 0]
            ]
        )

if __name__ == '__main__':
    unittest.main()
