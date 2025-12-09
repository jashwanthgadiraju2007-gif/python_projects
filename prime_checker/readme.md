
This is a simple Python program that checks whether a given number is a **Prime Number** or **Not a Prime Number**.


 What is a Prime Number?
A prime number is a number that:
- Is greater than 1
- Has only **two factors**: 1 and itself  
Examples: 2, 3, 5, 7, 11, 13

---

 How the Program Works

1. The user enters a number.
2. The program checks:
   - If the number is less than or equal to 1 → Not Prime
   - Otherwise, it checks divisibility from `2` to `√n`
3. If any number divides it → Not Prime
4. If no number divides it → Prime

---

 Algorithm

1. Read the input number.
2. If `n <= 1`, print **Not Prime**.
3. Loop from `2` to `√n`.
4. If `n % i == 0`, return **Not Prime**.
5. Otherwise, return **Prime**.

---

 How to Run the Program

1. Make sure Python is installed.
2. Save the file as:
prime_checker.py

3. Run the program:
python prime_checker.py

 Sample Input & Output

Enter a number: 17
17 is a Prime Number

Copy code
Enter a number: 10
10 is NOT a Prime Number












