name = input("Enter your name: ")

print("Hello", name)
print("Welcome to Smart Student Assistant")

print("1. Study Tip")
print("2. Motivation Quote")
print("3. Date and Time")

choice = input("Enter your choice: ")

if choice == "1":
    print("Study Tip: Read daily and practice regularly")

elif choice == "2":
    print("Motivation: Never give up")

elif choice == "3":
    from datetime import datetime
    print("Current Date and Time:")
    print(datetime.now())

else:
    print("Invalid Choice")