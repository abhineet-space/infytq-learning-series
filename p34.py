'''Problem Statement
A teacher in a school wants to find and display the grade of a student based on his/her percentage score. The criterion for grades is as given below:

Score (both inclusive)

Grade

Between 80 and 100

A

Between 73 and 79

B

Between 65 and 72

C

Between 0 and 64

D

Any other value

Z


Assume that the percentage score is a whole number.

Write a python program for the above requirement. Identify the test data and use it to test the program.

Note: Remove the duplicate values, if any, from the identified test data.

Fill the table with sample input and expected output for testing the requirement in the problem statement using boundary value analysis.
Use it to record the actual output and result by comparing the expected and actual output.'''



marks = 79
grade=""
if marks >=80 and marks<=100:
    grade= "A"
elif marks < 80 and marks>= 73:
    grade = "B"
elif marks <73 and marks >=65:
    grade = "C"
elif marks >=0 and marks<65:
    grade = "D"
else:
    grade= "Z"
print(grade)
