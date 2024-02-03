from projection_information import (update_seats_movie, check_movie_in_projections, check_movie_in_bookings,
                                    check_seat_availability)
from data import projections, bookings


def check_booking_in_bookings(bookings: list, email: str) -> bool:
    """
    Check if the booking is in the bookings list

    param bookings: a list of bookings
    param email: user's email
    return: return true if the booking is in the list or false if it's not
    """
    result = False

    for booking in bookings:

        if email == booking["email"]:
            result = True

        else:
            result = False

    return result


def add_booking(info: dict) -> str | dict:
    """
    Allows the user to make a booking if there are no current reservations for that movie

    param info: user's email and name
    return: return a string when user tries to add the same movie or return the booking if there are seats available
    """
    user_info = info

    movie = input("Write here the title of the movie: ").lower()
    while not check_movie_in_projections(movie):
        print(f"Error in typing the name of the movie. {movie} not listed")
        movie = input("Write here the title of the movie: ").lower()

    if check_movie_in_bookings(movie, user_info["email"]):
        return ("\nYou have already placed a booking for this movie!\n\nGo to manage your bookings if you want to "
                "change your booked seats")

    while True:
        try:
            seats = int(input(f"Enter the total number of seats for the movie: "))

            if seats != 0:
                break

            else:
                print("You can't enter 0 seats in your booking!")

        except ValueError:
            print("You must to enter an integer!")

    for film in projections:

        if film["movie_title"] == movie:

            if check_seat_availability(film, seats):

                print(update_seats_movie(projections, seats, movie))
                user_info["seats"] = seats
                user_info["movie_title"] = movie
                bookings.append(user_info)
                print("Booking confirmed!")
                return user_info

            else:
                return "Seats not available!"


def display_booking(email: str) -> str:
    """
    Allows user to display all his bookings

    param email: user's email
    return: a string if there aren't bookings
    """
    valid_email = check_booking_in_bookings(bookings, email)

    if valid_email:

        for booking in bookings:

            if booking["email"] == email:
                print(booking)

    else:
        return "There are no reservations attached to this email!"

    return ""


def manage_booking(email: str) -> str:
    """
    Allows the user to choose one of his bookings and change the number of seats

    param email: user's email
    return: returns a string that informs the user if the booking has been modified if there are seats available
            otherwise informs him that there are not enough seats or if there is no reservation attached to his email
    """

    valid_email = check_booking_in_bookings(bookings, email)
    if valid_email:
        print("Here your bookings:")
        print(display_booking(email))

        movie = input("Write here the title of the movie: ")
        while not check_movie_in_bookings(movie, email):
            print(f"Error in typing the name of the movie. {movie} not listed")
            movie = input("Write here the title of the movie: ")

        for b in bookings:

            if b["email"] == email and b["movie_title"] == movie:
                previous_seats = b["seats"]

                while True:
                    try:
                        seats = int(input(f"Enter the total number of seats for the movie: "))

                        if seats != 0:
                            break

                        else:
                            print("You can't enter 0 seats in your booking!")

                    except ValueError:
                        print("You must to enter an integer!")

                for m in projections:

                    if m["movie_title"] == movie:
                        print(update_seats_movie(projections, - previous_seats, movie))

                        if check_seat_availability(m, seats):

                            b["seats"] = seats
                            print(update_seats_movie(projections, seats, movie))

                            if seats > previous_seats:
                                print(f"You added {seats - previous_seats} seats more from your previous booking!")

                            elif seats < previous_seats:
                                print(f"You removed {previous_seats - seats} seats from your previous booking!")

                            return "Booking updated successfully!"

                        else:
                            return "Seats not available!"

    else:
        return "There are no reservations attached to this email!"


def remove_booking(email: str) -> str:
    """
    Allows the user to delete one of his bookings

    param email: user's email
    return: returns a string that informs the user if the reservation has been deleted or if there is no reservation
            attached to their email
    """

    valid_email = check_booking_in_bookings(bookings, email)
    if valid_email:

        print("Here your bookings:")
        print(display_booking(email))

        movie = input("Write here the title of the movie: ")
        while not check_movie_in_bookings(movie, email):
            print(f"Error in typing the name of the movie. {movie} not listed")
            movie = input("Write here the title of the movie: ")

        for b in bookings:

            if b["email"] == email and b["movie_title"] == movie:

                for m in projections:

                    if m["movie_title"] == movie:

                        print(update_seats_movie(projections, - b["seats"], movie))
                        bookings.remove(b)

                        return "Booking deleted successfully!"
    else:
        return "There are no reservations attached to this email!"
