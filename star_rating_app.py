"""
An application that queries the client for movie titles
and a rating for each movie.
"""

# update
_MIN_STARS = 0
_MAX_STARS = 0 

def one_star():
    """sets a single * to the variable stars."""
    stars = '*' #change me
    return stars 


def two_star():
    """sets two * to the variable stars."""
    stars = '**' #change me
    return stars


def three_star():
    """sets three * to the variable stars."""
    stars = '***'  # change me
    return stars


def four_star():
    """sets four * to the variable stars."""
    stars = '****'  # change me
    return stars

def five_star():
    """sets five * to the variable stars."""
    stars = '*****'  # change me
    return stars

def add_movie(movies):
    movieName = get_movie()
    starRating = get_rating()
    star = convert_rating(starRating)
    movies += star + "  "+ movieName + "\n"
    return movies

def get_movie():
    movieName = input("Enter a movie: ")
    return movieName

def get_rating():
    starRating = input("Rate between 1 and 5 ")
    return starRating

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def get_valid_int(prompt):
    while prompt.isnumeric() == False:
        print("Must be a positive whole number.")
        prompt = get_rating()
        
    else:
            
        if int(prompt) > 5:
            prompt = 5
            
        if int(prompt) >= 1 and int(prompt) <= 5 and int(prompt) % 1 == 0:
            prompt = prompt

    return int(prompt)
    

def convert_rating(starRating):
    
    starRating = get_valid_int(starRating)

    star = int(starRating)

    if star == 1:
        starRating = one_star()
    if star == 2:
        starRating = two_star()
    if star == 3:
        starRating = three_star()
    if star == 4:
        starRating = four_star()
    if star == 5:
        starRating = five_star()

    return starRating

def list_movies(movies):
    print(movies)

def menu():
    command = str.casefold(input("What would you like to do (add, list, exit)? "))
    return command


def run(movies: str = '') -> None:
    """
    Runs the star rating application.

    Args:
       The movie string, keeping track
       of all movies added between menu calls.
    """
    command = menu() # update with your code

    if command == 'add':
        movies = add_movie(movies)
    if command == 'list':
        movies.strip()
        list_movies(movies)
    if command == 'exit':
        return

    if command != "exit":
        run(movies)


if __name__ == "__main__":
    run()
