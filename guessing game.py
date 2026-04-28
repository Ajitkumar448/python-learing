import random
import winsound
Number = random.randint(1, 100)
print("🚀Game Started")
attempts = 1
while attempts <= 3:
    guess = int(input("Enter your guess (1-100): "))
    if guess < Number:
        print("📉Too low! Try again.")
        print("\a")  # Beep sound for incorrect guess
        print("attempts left:", 3 - attempts)
    elif guess > Number:
        print("📈Too high! Try again.")
        print("\a")  # Beep sound for incorrect guess
        print("attempts left:", 3 - attempts)
    else:
        print("🎉Congratulations correct guess")
        winsound.Beep(1000, 500)  # Beep sound for correct guess
        break
    attempts += 1
if attempts > 3:
    print("💥Game Over! The correct number was:", Number)
    winsound.Beep(500, 1000)  # Beep sound for game over
    print("play again")