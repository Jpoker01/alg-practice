from collections import Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count = len(students)
        different_sandwich_count = Counter(students)

        for sandwich in sandwiches:
            if  different_sandwich_count[sandwich] > 0:
                student_count -= 1
                different_sandwich_count[sandwich] -= 1
            else:
                break
        return student_count

        