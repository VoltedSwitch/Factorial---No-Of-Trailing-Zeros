from ui.user_interface import UserInterface
from ui.user_interface_utils import clear_screen


def main():
    ui = UserInterface()

    while True:
        user_input = ui.user_number_menu()
        if ui.is_valid_user_number_menu_input(user_input):
            user_number = int(user_input)
            ui.display_results_to_user(user_number)
            exit()
        else:
            clear_screen()


if __name__ == "__main__":
    clear_screen()
    main()
