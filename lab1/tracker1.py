# Name: Priyanshi
# Date: October 10, 2025
# Project: Daily Calorie Tracker

# Task 1: Setup & Introduction
print("Welcome to the Daily Calorie Tracker!")
print("This app helps you record your meals and calories,")
print("calculate your total intake, and and helps you to mantain your health.")

# Task 2: Input & Data Collection
meal_names = [  ]
calorie_amounts = [ ]

num_meals = int(input("How many meals would you like to enter today? "))

for i in range(num_meals):
    meal_name = input(f"Enter the name of meal {i + 1}: ")
    calorie_amount = float(input(f"Enter the calorie amount for {meal_name}: "))
    meal_names.append(meal_name)
    calorie_amounts.append(calorie_amount)

# Task 3: Calorie Calculations
total_calories = sum(calorie_amounts)
average_calories = total_calories / len(calorie_amounts) #if calorie_amounts else 0

daily_limit = float(input("Enter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
if total_calories > daily_limit:
    print(f"Warning: You have exceeded your daily calorie limit of {daily_limit}!")
else:
    print(f"Success! You are within your daily calorie limit.")

# Task 5: Neatly Formatted Output
meal=[]
calories=[ ]

for name, calories in zip(meal_names, calorie_amounts):
    print(f"{name}\t\t{calories}")

print("-" * 30)
print(f"Total:\t\t\t{total_calories}")
print(f"Average:\t\t{average_calories:.2f}") 
print("=" * 30)

 # type: ignore