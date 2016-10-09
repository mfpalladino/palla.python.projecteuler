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
sys.path.append("problem_05")
import solver_05
sys.path.append("problem_06")
import solver_06
sys.path.append("problem_07")
import solver_07
sys.path.append("problem_08")
import solver_08
sys.path.append("problem_09")
import solver_09
sys.path.append("problem_10")
import solver_10

class Tests(unittest.TestCase):

    def test_solver_01(self):
        print("\r\n")
        print("solver_01")
        self.assertEqual(solver_01.solver(), 233168)

    def test_solver_02(self):
        print("\r\n")
        print("solver_02")
        self.assertEqual(solver_02.solver(), 4613732)

    def test_solver_03(self):
        print("\r\n")
        print("solver_03")
        solver_instance = solver_03.Solver()
        self.assertEqual(solver_instance.get_result(), 6857)

    def test_solver_04(self):
        print("\r\n")
        print("solver_04")
        solver_instance = solver_04.Solver()
        self.assertEqual(solver_instance.get_result(), 906609)

    def test_solver_05(self):
        #slow
        print("\r\n")
        print("solver_05")
        solver_instance = solver_05.Solver()
        self.assertEqual(solver_instance.get_result(), 232792560)

    def test_solver_06(self):
        print("\r\n")
        print("solver_06")
        solver_instance = solver_06.Solver()
        self.assertEqual(solver_instance.get_result(), 25164150)

    def test_solver_07(self):
        print("\r\n")
        print("solver_07")
        solver_instance = solver_07.Solver()
        self.assertEqual(solver_instance.get_result(), 104743)

    def test_solver_08(self):
        print("\r\n")
        print("solver_08")
        solver_instance = solver_08.Solver()
        self.assertEqual(solver_instance.get_result(), 23514624000)

    def test_solver_09(self):
        print("\r\n")
        print("solver_09")
        solver_instance = solver_09.Solver()
        self.assertEqual(solver_instance.get_result(), 31875000)

    def test_solver_10(self):
        print("\r\n")
        print("solver_10")
        solver_instance = solver_10.Solver()
        self.assertEqual(solver_instance.get_result(), 142913828922)

if __name__ == '__main__':
    unittest.main()