# 2) You are given a list of subjects for students.
# Assume one classroom is required for 1 subject.
# How many classrooms are needed by all students.

subjects = ["python", "java", "C++", "python", "javascript",
            "java", "python", "java", "C++", "C"]

unique_subjects = set(subjects)

print("Number of classrooms needed:", len(unique_subjects))
