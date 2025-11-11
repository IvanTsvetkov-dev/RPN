"""Модуль для UNIT тестов модуля RPN

"""


import unittest
from main import evaluate


class TestRPN(unittest.TestCase):
    """Класс для тестирования RPN
    """
    def test_add(self):
        """Правильное работа операции сложения
        """
        self.assertEqual(evaluate('5 3 +'), 8)

    def test_subtraction(self):
        """Правильная работа операции вычитания
        """
        self.assertEqual(evaluate('5 3 -'), 2)

    def test_multiplication(self):
        """Правильная работа операции умножения
        """
        self.assertEqual(evaluate('5 3 *'), 15)

    def test_div(self):
        """Правильная работа операции деления
        """
        self.assertEqual(evaluate('6 3 /'), 2)

    def test_pop_one_operation_and_one_number(self):
        """Ошибка при вычислении одного операнда с оператором (IndexError)
        """
        with self.assertRaises(IndexError):
            evaluate('5 +')


    def test_incorrect_operator(self):
        """Ошибка при вводе недопустимых операторов
        """
        with self.assertRaises(ValueError):
            evaluate('10 5 +-')


if __name__ == 'main':
    unittest.main()
