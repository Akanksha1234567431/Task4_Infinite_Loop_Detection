import unittest
from loop_detector import analyze_code


class TestLoopDetector(unittest.TestCase):

    def test_infinite_loop(self):
        code = "while True:\n    print('Hello')"
        result = analyze_code(code)

        self.assertEqual(
            result[0]["status"],
            "POSSIBLE INFINITE LOOP"
        )

    def test_conditional_loop(self):
        code = "while x < 5:\n    x += 1"
        result = analyze_code(code)

        self.assertEqual(
            result[0]["status"],
            "CONDITION-DEPENDENT LOOP"
        )

    def test_for_loop(self):
        code = "for i in range(5):\n    print(i)"
        result = analyze_code(code)

        self.assertEqual(
            result[0]["status"],
            "ITERABLE-BASED LOOP"
        )

    def test_no_loop(self):
        code = "print('Hello')"
        result = analyze_code(code)

        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()