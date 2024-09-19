def main():
    while True:
        #user menu
        print("\nChoose a data type to perform operations on:")
        print("1. Strings")
        print("2. Numbers")
        print("3. Booleans")
        print("4. Additional Data Types (List, Tuple, Dictionary)")
        print("5. Exit")

        #user choice
        choice = input("Enter the number of your choice (1-5): ")

        if choice == '1':
            #string ops
            sentence = "Learning Python is fun!"
            print("\nYou chose Strings!")
            print("Original Sentence:", sentence)

            #extracting substring (Python)
            print("Substring (Python):", sentence[9:15])

            #converting to upper
            print("Uppercase:", sentence.upper())

            #replacing 'fun' with 'awesome'
            modified_sentence = sentence.replace("fun", "awesome")
            print("Modified Sentence:", modified_sentence)

        elif choice == '2':
            #number ops
            print("\nYou chose Numbers!")
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                #arithmetic ops
                print(f"Addition: {num1 + num2}")
                print(f"Subtraction: {num1 - num2}")
                print(f"Multiplication: {num1 * num2}")

                #division by zero
                if num2 != 0:
                    print(f"Division: {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")

                #power ops
                print(f"{num1} raised to the power of {num2} is: {num1 ** num2}")

            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == '3':
            #boolean ops
            is_python_fun = True
            is_sunny = False
            print("\nYou chose Booleans!")
            print("is_python_fun =", is_python_fun)
            print("is_sunny =", is_sunny)

            #logic ops
            print(f"AND operation (is_python_fun and is_sunny): {is_python_fun and is_sunny}")
            print(f"OR operation (is_python_fun or is_sunny): {is_python_fun or is_sunny}")
            print(f"NOT operation (not is_python_fun): {not is_python_fun}")

            #comparison opS
            print(f"10 > 5: {10 > 5}")
            print(f"5 == 5: {5 == 5}")

        elif choice == '4':
            #ADT (list, tuple, dictionary)
            print("\nYou chose Additional Data Types!")

            #list ops
            my_list = [1, 2, 3, "Python", True]
            print("Original List:", my_list)

            #append to list
            my_list.append("New Element")
            print("Updated List after appending:", my_list)

            #4th element
            print("4th Element in List:", my_list[3])

            #tuple ops
            fruits = ("apple", "banana", "cherry")
            print("\nTuple of fruits:", fruits)
            print("Length of Tuple:", len(fruits))

            #modify tuple and handling TypeError
            try:
                fruits[0] = "mango"
            except TypeError as e:
                print(f"Error: {e} (Tuples are immutable)")

            #dictionary ops
            person = {"name": "Alice", "age": 25, "city": "New York"}
            print("\nDictionary:", person)

            #value by key
            print("Age:", person["age"])

            #adding a new key-value pair
            person["country"] = "USA"
            print("Updated Dictionary:", person)

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            #error-invalid choice
            print("Error: Invalid choice. Please select a valid option.")


#start main function
if __name__ == "__main__":
    main()
