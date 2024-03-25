movies = {}


def show_movies():
    for movie_key in movies.keys():
        name = movies[movie_key]["movie_name"]
        director = movies[movie_key]["movie_director"]
        year = movies[movie_key]["movie_year"]
        print(movie_key, "=> Adı: ", name, " Yönetmeni: ", director, " Yılı: ", year)


def add_movie():
    name = input("Filmin adını girin\n")
    director = input("Filmin yçnetmenini girin\n")
    year = input("Filmin yılını girin\n")
    key = len(movies.items()) + 1
    movies[key] = {"movie_name": name, "movie_director": director, "movie_year": year}


def delete_movie():
    movie_key = int(input("Hangi filmi silmek istiyorsunuz\n"))
    movies.pop(movie_key)