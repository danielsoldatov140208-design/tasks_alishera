import unittest
from course_service import Course, IntensiveCourse

class TestCourseService(unittest.TestCase):

    def test_course_creation_success(self):
        course = Course("Python Dev", 20)
        self.assertEqual(course.title, "Python Dev")
        self.assertEqual(course.capacity, 20)
        self.assertEqual(course.enrolled, 0)

    def test_course_creation_empty_title_raises_error(self):
        with self.assertRaises(ValueError):
            Course("", 20)
        with self.assertRaises(ValueError):
            Course("   ", 20)

    def test_course_creation_invalid_capacity_raises_error(self):
        with self.assertRaises(ValueError):
            Course("Python Dev", 0)
        with self.assertRaises(ValueError):
            Course("Python Dev", -5)

    def test_available_places_initial(self):
        course = Course("QA Testing", 15)
        self.assertEqual(course.available_places(), 15)

    def test_enroll_single_student(self):
        course = Course("QA Testing", 5)
        remaining = course.enroll()
        self.assertEqual(course.enrolled, 1)
        self.assertEqual(remaining, 4)

    def test_enroll_multiple_students_until_full(self):
        course = Course("QA Testing", 2)
        course.enroll()
        remaining = course.enroll()
        self.assertEqual(course.enrolled, 2)
        self.assertEqual(remaining, 0)

    def test_enroll_exceeding_capacity_raises_error(self):
        course = Course("QA Testing", 1)
        course.enroll()
        with self.assertRaises(ValueError):
            course.enroll()

    def test_cancel_enrollment_success(self):
        course = Course("DevOps", 5)
        course.enroll()
        remaining = course.cancel_enrollment()
        self.assertEqual(course.enrolled, 0)
        self.assertEqual(remaining, 5)

    def test_cancel_enrollment_when_empty_raises_error(self):
        course = Course("DevOps", 5)
        with self.assertRaises(ValueError):
            course.cancel_enrollment()

    def test_is_full_property(self):
        course = Course("Data Science", 2)
        self.assertFalse(course.is_full)
        course.enroll()
        self.assertFalse(course.is_full)
        course.enroll()
        self.assertTrue(course.is_full)

    def test_intensive_course_inheritance_and_workload(self):
        course = IntensiveCourse("Web Dev", 10, 8)
        self.assertIsInstance(course, Course)
        self.assertEqual(course.workload_level(), "средняя")

        course_high = IntensiveCourse("Web Dev Heavy", 10, 15)
        self.assertEqual(course_high.workload_level(), "высокая")

    def test_intensive_course_boundary_hours(self):
        self.assertEqual(IntensiveCourse("C1", 10, 6).workload_level(), "средняя")
        self.assertEqual(IntensiveCourse("C2", 10, 10).workload_level(), "средняя")
        self.assertEqual(IntensiveCourse("C3", 10, 11).workload_level(), "высокая")
        self.assertEqual(IntensiveCourse("C4", 10, 20).workload_level(), "высокая")

    def test_intensive_course_invalid_hours_raises_error(self):
        with self.assertRaises(ValueError):
            IntensiveCourse("Bad", 10, 5)
        with self.assertRaises(ValueError):
            IntensiveCourse("Bad", 10, 21)

    def test_intensive_course_inherited_methods(self):
        course = IntensiveCourse("Mobile Dev", 1, 12)
        self.assertEqual(course.available_places(), 1)
        course.enroll()
        self.assertTrue(course.is_full)

if __name__ == "__main__":
    unittest.main()