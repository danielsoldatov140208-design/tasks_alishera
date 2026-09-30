import unittest
from ekeb_service import (
    Student,
    GrantStudent,
    ExcellentStudent,
    print_cost,
    exam_result
)


class TestPrintCost(unittest.TestCase):
    def test_zero_pages(self):
        self.assertEqual(print_cost(0), 0)

    def test_one_page(self):
        self.assertEqual(print_cost(1), 30)

    def test_nine_pages_no_discount(self):
        self.assertEqual(print_cost(9), 270)

    def test_ten_pages_discount_boundary(self):
        self.assertEqual(print_cost(10), 270)  # 10 * 30 * 0.9 = 270

    def test_eleven_pages_with_discount(self):
        self.assertEqual(print_cost(11), 297)  # 11 * 30 * 0.9 = 297

    def test_negative_pages_raises_value_error(self):
        with self.assertRaises(ValueError):
            print_cost(-1)


class TestExamResult(unittest.TestCase):
    def test_boundary_one(self):
        self.assertEqual(exam_result(1), "Незачёт")

    def test_boundary_zero(self):
        self.assertEqual(exam_result(0), "Незачёт")

    def test_boundary_forty_nine(self):
        self.assertEqual(exam_result(49), "Незачёт")

    def test_boundary_fifty_passed(self):
        self.assertEqual(exam_result(50), "Зачёт")

    def test_boundary_fifty_one_passed(self):
        self.assertEqual(exam_result(51), "Зачёт")

    def test_boundary_one_hundred(self):
        self.assertEqual(exam_result(100), "Зачёт")

    def test_invalid_score_101_raises_error(self):
        with self.assertRaises(ValueError):
            exam_result(101)

    def test_invalid_negative_score_raises_error(self):
        with self.assertRaises(ValueError):
            exam_result(-1)


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Алия", 50)

    def test_initial_attributes(self):
        self.assertEqual(self.student.name, "Алия")
        self.assertEqual(self.student.score, 50)

    def test_has_passed_boundary_fifty(self):
        self.assertTrue(self.student.has_passed())

    def test_add_points(self):
        self.student.add_points(10)
        self.assertEqual(self.student.score, 60)

    def test_add_points_maximum_cap(self):
        self.student.add_points(60)  # 50 + 60 = 110 -> ограничение 100
        self.assertEqual(self.student.score, 100)

    def test_add_negative_points_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.student.add_points(-10)


class TestGrantStudent(unittest.TestCase):
    def test_is_instance_of_student(self):
        grant_student = GrantStudent("Асан", 80)
        self.assertIsInstance(grant_student, Student)

    def test_grant_status_69_points(self):
        student = GrantStudent("Игорь", 69)
        self.assertEqual(student.grant_status(), "Грант не сохранён")

    def test_grant_status_70_points(self):
        student = GrantStudent("Данияр", 70)
        self.assertEqual(student.grant_status(), "Грант сохранён")

    def test_grant_status_71_points(self):
        student = GrantStudent("Мария", 71)
        self.assertEqual(student.grant_status(), "Грант сохранён")

    def test_inherited_add_points_updates_grant_status(self):
        student = GrantStudent("Алихан", 65)
        self.assertEqual(student.grant_status(), "Грант не сохранён")
        student.add_points(10)  # Становится 75
        self.assertEqual(student.grant_status(), "Грант сохранён")


class TestExcellentStudent(unittest.TestCase):
    def test_scholarship_boundaries(self):
        s74 = ExcellentStudent("A", 74)
        s75 = ExcellentStudent("B", 75)
        s89 = ExcellentStudent("C", 89)
        s90 = ExcellentStudent("D", 90)
        s100 = ExcellentStudent("E", 100)

        self.assertEqual(s74.scholarship(), 0)
        self.assertEqual(s75.scholarship(), 15000)
        self.assertEqual(s89.scholarship(), 15000)
        self.assertEqual(s90.scholarship(), 30000)
        self.assertEqual(s100.scholarship(), 30000)


if __name__ == "__main__":
    unittest.main()