import unittest
import sys

sys.path.append("problem_01")
import solver_01
sys.path.append("problem_02")
import solver_02
sys.path.append("problem_03")
import solver_03
sys.path.append("problem_04")
import solver_04

class Tests(unittest.TestCase):

    def test_solver_01(self):
        self.assertEqual(solver_01.solver(), 233168)

    def test_solver_02(self):
        self.assertEqual(solver_02.solver(), 4613732)

    def test_solver_03(self):
        solver_instance = solver_03.Solver()
        self.assertEqual(solver_instance.get_result(), 6857)

    def test_solver_04(self):
        solver_instance = solver_04.Solver()
        self.assertEqual(solver_instance.get_result(), 906609)

if __name__ == '__main__':
    unittest.main()