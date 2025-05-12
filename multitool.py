def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

def check_age():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You're an adult.")
    else:
        print("You're a minor.")

def reverse_word():
    word = input("Enter a word: ")
    print("Reversed word:", word[::-1])

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Greet")
        print("2. Check age")
        print("3. Reverse a word")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            greet()
        elif choice == "2":
            check_age()
        elif choice == "3":
            reverse_word()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()