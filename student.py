#a program to compute studentname courseworkmark examscore
student_name=input("student name: ")
exam_score=int(input("exams score: "))
course_work_mark=int(input("course work mark: "))
exam=(exam_score/100)*70

final_exam=exam+course_work_mark
print(final_exam)