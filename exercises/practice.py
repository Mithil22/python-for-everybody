#!/usr/bin/env python3
"""
Simple Python script for practicing basics
Run this with: python exercises/practice.py
"""

def greet_user():
    """Simple function to greet the user"""
    name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to Python programming!")


def calculator():
    """Simple calculator function"""
    print("\n--- Simple Calculator ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print(f"\n{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {num1 / num2}")


def temperature_converter():
    """Convert Fahrenheit to Celsius"""
    print("\n--- Temperature Converter ---")
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")


def main():
    """Main function to run all exercises"""
    print("Python Practice Exercises\n")
    print("Choose an exercise:")
    print("1. Greeting")
    print("2. Calculator")
    print("3. Temperature Converter")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        greet_user()
    elif choice == "2":
        calculator()
    elif choice == "3":
        temperature_converter()
    elif choice == "4":
        print("Goodbye!")
        return
    else:
        print("Invalid choice!")
    
    # Ask if user wants to continue
    again = input("\nTry another exercise? (y/n): ")
    if again.lower() == 'y':
        main()


if __name__ == "__main__":
    main()
