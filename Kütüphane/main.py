import movie_engine

option_show_list = "1"
option_add_movie = "2"
option_delete_movie = "3"
option_exit = "X" 


def show_menu():
    menu_text = (
            option_show_list + " = Listele\n" + option_add_movie + " = Ekleme\n" + option_delete_movie + " = Silme\n" + option_exit + " = çıkış\n")
    return input(menu_text)


print("Film kütüphanesi v1.0\n")
while True:
    choice = show_menu()

    if choice == option_show_list:
        movie_engine.show_movies()
    elif choice == option_add_movie:
        movie_engine.add_movie()
    elif choice == option_delete_movie:
        movie_engine.delete_movie()
    elif choice == option_exit:
        break

print("çıkış yapılıyor ...")