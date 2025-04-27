from core.factorial import Factorial


class UserInterface:
    def user_number_menu(self) -> str:
        print("Factorial Related")
        return input("\nEnter a number: ")

    def is_valid_user_number_menu_input(self, user_number_menu_input: str) -> bool:
        return user_number_menu_input.isdigit()

    def display_results_to_user(self, user_number: int):
        factorial = Factorial(user_number)
        print(f"Factorial: {factorial}")
        print(
            f"Amount Of Trailing Zeros In Factorial: {factorial.trailing_zeros_amount}"
        )
