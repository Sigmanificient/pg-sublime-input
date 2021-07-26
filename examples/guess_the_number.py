import random
import sublinput

attempts: int = 1
target: int = random.randint(0, 100)
n: int = -1

while int(input("Enter a number :")) != target:
    print("You were too", "high" if n < target else "low")
    attempts += 1

print(f"You found the number within {attempts} attempt(s) !")
