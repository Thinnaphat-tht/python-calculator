import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-4, 4), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4,5), -1)
        self.assertEqual(self.calc.subtract(5,4), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,1), 5)
        self.assertEqual(self.calc.multiply(-5,-5), 25)

    def test_divide(self):
        self.assertEqual(self.calc.divide(50,0),"Cannot divide by zero")
        self.assertEqual(self.calc.divide(100,5),20)
        self.assertEqual(self.calc.divide(100,-5),-20)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(25,7),4)
        self.assertEqual(self.calc.modulo(12,3),0)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()