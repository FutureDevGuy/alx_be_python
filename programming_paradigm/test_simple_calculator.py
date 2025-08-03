import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method runs.
        This ensures each test starts with a fresh calculator instance.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the add method with various numerical inputs.
        """
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, -50), 50)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(-2.5, -3.5), -6.0)

    def test_subtraction(self): # <--- THIS IS THE METHOD TO ENSURE IS PRESENT AND CORRECT
        """
        Test the subtract method with various numerical inputs.
        """
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0)
        self.assertEqual(self.calc.subtract(2.5, 7.5), -5.0)
        self.assertEqual(self.calc.subtract(0, 5), -5) # Test subtracting from zero
        self.assertEqual(self.calc.subtract(5, 0), 5) # Test subtracting zero

    def test_multiply(self):
        """
        Test the multiply method with various numerical inputs.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25)
        self.assertEqual(self.calc.multiply(7, 1), 7) # Test multiplying by one

    def test_divide(self):
        """
        Test the divide method with various numerical inputs, including division by zero.
        """
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        # Test division by zero, which should return None as per SimpleCalculator's implementation
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Also test 0/0

# This block allows running the tests directly from the command line
if __name__ == "__main__":
    unittest.main()
