This Python program analyzes the marks of students and generates a detailed report including:

Total number of students

Average score

Highest and lowest marks

Pass/Fail count

Pass and fail percentages

Grade distribution (A, B, C, D, F)

The program takes comma-separated marks as input and processes them using a custom function.

 Features
1. Calculates Key Statistics

Total students

Average marks

Highest mark

Lowest mark

2. Pass/Fail Evaluation

Counts how many students passed (≥ 40)

Counts how many failed

3. Grade Classification

Grades are assigned based on the following rules:

Grade	Marks Range
A	90–100
B	75–89
C	60–74
D	40–59
F	0–39
4. Percentage Calculations

Pass percentage

Fail percentage

5. Clean Output Format

Results are displayed in an organized and readable format.

 How the Program Works
1. User Inputs Marks

User enters values like:

90,75,43,88,69,39

2. student_analysis() Function Runs

This function:

Processes the marks

Determines grades

Counts pass/fail

Calculates percentages

3. main() Prints Results

Displays all the computed statistics.

 Code Overview

The program has two main parts:

1. student_analysis(marks)

This function returns:

Total students

Average

Highest & Lowest

Pass count

Fail count

Grade distribution

Pass percentage

Fail percentage

2. main()

Reads user input

Calls the analysis function

Prints the results

 Sample Input
enter marks: 95,76,88,43,39,67

 Sample Output
total students: 6
average: 68.0
highest: 95
lowest: 39
passed: 5
failed: 1
pass_percentage: 83.33
fail_percentage: 16.67

grade distribution:
A : 1
B : 2
C : 1
D : 1
F : 1
How to Run

Save the Python file (e.g., student_analysis.py)

Run the program:

python student_analysis.py


Enter marks separated by commas.
