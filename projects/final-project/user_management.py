import re
from bookings import add_booking, display_booking, remove_booking, manage_booking
from projection_information import display_info
from data import projections


def check_email(email: str) -> bool:
    """
    This function check if the email is inserted in the appropriate format.

    param email: email to check
    return: return true if the email is correct or false if it is not
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(regex, email):
        return True

    else:
        return False


def get_user_info() -> dict[str, str]:
    """
    Get name and email from user

    return: a dictionary with user's information
    """
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    if check_email(email):
        information = {
            "name": name,
            "email": email
        }
        return information
    else:
        print("Invalid email!")


def user_interface() -> str:
    """
    This function is a direct interface with the user. It handles various inputs that allow the user to add, view,
    edit and remove bookings

    return: a string that informs the user that the app is closing
    """

    using_the_app = input("Press enter if you want to use the Cinema Booking Manager.\nPress q to close the app. ")
    while using_the_app != "" and using_the_app.lower() != "q":
        using_the_app = input("Press enter if you want to use the Cinema Booking Manager.\nPress q to close the app. ")

    user_info = get_user_info()
    while not user_info:
        print("Enter a valid email")
        user_info = get_user_info()

    while using_the_app == "":

        user_choice = input(f"Press enter if you want to create a booking, \npress v to display all movies,"
                            f"\npress d for display your bookings, \npress m if you want to manage your bookings,"
                            f"\npress r if you want to remove "
                            f"a reservation or\npress q to exit: ")

        while (user_choice != "" and user_choice.lower() != "d" and user_choice.lower() != "q" and user_choice.lower()
               != "m" and user_choice.lower() != "r" and user_choice.lower() != "v"):
            user_choice = input(f"Press enter if you want to create a booking, \npress v to display all movies,"
                                f"\npress d for display your bookings, \npress m if you want to manage your bookings,"
                                f"\npress r if you want to remove "
                                f"a reservation or\npress q to exit: ")

        if user_choice == "":
            print(add_booking(user_info))

        if user_choice.lower() == "v":
            print(display_info(projections))

        if user_choice.lower() == "d":
            print(display_booking(user_info["email"]))

        if user_choice.lower() == "m":
            print(manage_booking(user_info["email"]))

        if user_choice.lower() == "r":
            print(remove_booking(user_info["email"]))

        if user_choice.lower() == "q":
            break

        using_the_app = input(
            "\nPress enter if you wish to continue using the Cinema Booking Manager and manage your reservations"
            " or make a new reservation. Otherwise press q to exit: ")
        while using_the_app != "" and using_the_app.lower() != "q":
            using_the_app = input(
                "\nPress enter if you wish to continue using the Cinema Booking Manager and manage your reservations"
                " or make a new reservation. Otherwise press q to exit: ")

    return "Closing the app"
