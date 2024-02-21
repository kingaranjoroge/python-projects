from calculator_functions import Calculator

if __name__ == "__main__":
    calculator = Calculator()

    numbers_input = input("Enter numbers separated by commas:\n\n ")
    numbers_list = [int(num.strip()) for num in numbers_input.split(',')]

    choice = input("\nWhich operation would you like to perform? Enter:\n\n 1 for Addition,\n 2 for Subtraction,\n 3 for Multiplication,\n 4 for Division\n\n")
    student_choice = int(choice)

    if student_choice == 1:
        print(f"\nThe sum of {numbers_list} is {calculator.addition(numbers_list)}")
    elif student_choice == 2:
        print(f"\nThe result of subtracting {numbers_list[1:]} from {numbers_list[0]} is {calculator.subtraction(numbers_list)}")
    elif student_choice == 3:
        print(f"\nThe product of {numbers_list} is {calculator.multiplication(numbers_list)}")
    elif student_choice == 4:
        print(f"\nThe result of dividing {numbers_list[0]} by {numbers_list[1:]} is {calculator.division(numbers_list)}")
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
