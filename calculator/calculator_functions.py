class Calculator:
    @staticmethod
    def addition(numbers):
        return sum(numbers)

    @staticmethod
    def subtraction(numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result

    @staticmethod
    def multiplication(numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    @staticmethod
    def division(numbers):
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                return "Error! Division by zero!"
            result /= num
        return result
