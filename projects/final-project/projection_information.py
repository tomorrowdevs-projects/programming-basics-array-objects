from data import projections, bookings


def display_info(projections: list[dict]) -> str:
    """
    Display all the movies in the cinema

    param projections: A list of movies
    return: None
    """

    for projection in projections:

        print(projection)
        print()

    return ""


def update_seats_movie(projections: list[dict], seats: int, movie: str) -> str:
    """
    Update the number of seats in the dictionary relating to the film within the "projections" list

    param projections: a list of movies
    param seats: the number of seats
    param movie: the name of the film
    return: None
    """

    for projection in projections:

        if movie == projection["movie_title"]:

            projection["available_seats"] -= seats

    return ""


def check_movie_in_projections(movie: str) -> bool:
    """
    Check if the movie is listed in the projections list

    param movie: name of the film
    return: return true if the movie is listed or false if it's not
    """
    result = False

    for projection in projections:

        if movie.lower() == projection["movie_title"]:

            result = True

    return result


def check_movie_in_bookings(movie: str, email: str) -> bool:
    """
    Check if the movie is listed in the user's bookings list

    param movie: name of the movie
    param email: user's email
    return: return true if the movie is listed or false if it's not
    """
    result = False

    for m in bookings:

        if m["email"] == email:

            if movie == m["movie_title"]:

                result = True

    return result


def check_seat_availability(movie: dict, seats: int) -> bool:
    """
    Check seats availability for the selected screening

    param movie: a dictionary of movie information
    param seats: number of seats
    return: return true if there are seats available for that film
    """

    for i in movie:

        if seats <= movie["available_seats"]:

            return True
