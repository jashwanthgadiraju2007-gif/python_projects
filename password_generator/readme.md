 Password Generator

This Python program generates a strong and secure random password using:
- Uppercase letters
- Lowercase letters
- Digits (0–9)
- Special characters (!, @, #, $, etc.)

The user can enter any desired length, and the program will generate a password of that size.

---

 Features
- Generates completely random passwords
- Uses letters, digits, and punctuation symbols
- User can choose any password length
- Simple and beginner-friendly

---

#How It Works
The program combines:
- `string.ascii_letters`
- `string.digits`
- `string.punctuation`

Then randomly selects characters using `random.choice()`.

---

How to Run

```bash
python main.py

