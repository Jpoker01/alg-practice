class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_num = len(students)
        index = 0
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                student_num -= 1
                index = 0
                continue
            
            students.append(students.pop(0))
            index += 1
            if index == student_num:
                return student_num
        return 0

        