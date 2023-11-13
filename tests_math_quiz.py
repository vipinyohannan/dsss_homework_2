import unittest
from math_quiz import generate_random_integer, generate_random_operator, evaluate_expression

class TestMathQuizFunctions(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the generated operator is in the expected list
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, ['+', '-', '*'])

    def test_evaluate_expression(self):
        # Test cases for evaluate_expression function
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = evaluate_expression(num1, num2, operator)
            self.assertEqual(problem, expected_problem, "Expression problem does not match")
            self.assertEqual(answer, expected_answer, "Expression evaluation does not match")

if __name__ == '__main__':
    unittest.main()
