#  1. Start the game, get name and age 
print("Welcome to the Cybersmart Start Quiz!")
user_name = input("Please enter your name: ").strip()
print(f"Hello, {user_name}!")

try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Please enter a valid number for your age.")
    sys.exit()
# --- 2. Check age for Youth Quiz ---
if age >= 14:
    print(f"Hi {user_name}, you are over 14. Please try the 'Cybersmart Youth Quiz' instead.")
    sys.exit()
elif age < 8:
    print("This quiz is designed for ages 8-13, but you can proceed!")
else:
    print("Welcome to the Cyber Agent training!")

