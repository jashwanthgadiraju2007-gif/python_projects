A simple and interactive **Number Guessing Game** built using Python.  
The user gets **5 attempts** to guess a number between **1 and 50**, but each attempt must be answered within **15 seconds** otherwise, it is counted as a failed attempt!

This project demonstrates:
- Conditional logic  
- Time measurement using `time` module  
- Loops and game design  
- User interaction  

---

  Features
- Generates a random number between **1 and 50**
- User gets **5 attempts total**
- **15-second time limit** for each guess  
- If the user delays → “Time Over”*  
- Shows hints: Smaller / Greater / Too much smaller / Much greater  
- Clean and beginner-friendly code  

---

## How the Game Works
1. Program picks a random number  
2. You try to guess it  
3. You must enter your guess **within 15 seconds**  
4. After each guess, the program tells you:  
   - `Too much smaller`  
   - `Smaller`  
   - `Greater`  
   - `Much greater`  
5. If you guess correctly →  **You win**  
6. If attempts become 0 → **Game over**
---

##  Sample Output

Guess the number between 1 and 50 (You have 5 attempts, 15 sec each)

Attempts left: 5
Enter your guess: 10
Too much smaller

Attempts left: 4
Enter your guess: 40
Much greater

Attempts left: 3
Enter your guess:
 Time over! You took more than 15 seconds.

Attempts left: 2
Enter your guess: 32
 Correct guess!
You guessed it correctly in 4 attempt(s)!
