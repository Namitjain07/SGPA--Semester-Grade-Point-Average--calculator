# SGPA (Semester Grade Point Average) calculator
 Python script that takes input for course details and calculates the SGPA (Semester Grade Point Average) based on the input.

## How to Use

1. Run the script in a Python environment.
2. Enter the course details in the format: `<course_no> <credit> <grade>`. Each course detail should be entered on a new line.
   - `<course_no>`: Alphanumeric course number.
   - `<credit>`: Credit value of the course (1, 2, or 4).
   - `<grade>`: Grade obtained in the course (A+, A, A-, B, B-, C, C-, D, or F).
3. Press Enter without entering any value to stop entering course details and calculate the SGPA.
4. The script will validate the input and display the sorted list of courses along with their grades.
5. Finally, it will calculate and display the SGPA.

## Example

Enter course details (course_no credit grade):
CSE101 4 A
CSE201 4 A-
MAT102 2 B
CSE301 4 B-
CSE401 4 C
CSE501 4 F

CSE101: A
CSE201: A-
CSE301: B-
CSE401: C
CSE501: F
SGPA: 6.91

## Note

- The script validates the input and displays error messages for any incorrect or improper input.
- Only courses with valid input are considered for calculating the SGPA.
- The script assumes that the course numbers are alphanumeric and follow a specific format.
- The script uses a predefined grading scale to calculate the SGPA.

Grades:
A+ : 10
A : 10
A- : 9
B : 8
B- : 7
C : 6
C- : 5
D : 4
F : 2

