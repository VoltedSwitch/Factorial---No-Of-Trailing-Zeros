class Factorial:
    def __init__(self, number: int) -> None:
        self._factorial = self.calculate_factorial(number)

    @staticmethod
    def calculate_factorial(number_to_calculate_factorial_of: int) -> int:
        if number_to_calculate_factorial_of in (0, 1):
            return 1

        multiplication_storage = number_to_calculate_factorial_of
        for number in reversed(range(1, number_to_calculate_factorial_of)):
            multiplication_storage *= number

        return multiplication_storage

    @property
    def trailing_zeros_amount(self) -> int:
        return self.find_trailing_zeros_amount()

    def find_trailing_zeros_amount(self) -> int:
        zero_streak_counter = 0
        for digit in reversed(str(self._factorial)):
            if digit == "0":
                zero_streak_counter += 1
            else:
                break
        return zero_streak_counter

    def __str__(self):
        return str(self._factorial)
