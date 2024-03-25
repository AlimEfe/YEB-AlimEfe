import todo_engine

print("Todo Programına Hoş geldiniz")
while True:
    choise = todo_engine.show_menu()

    if choise == todo_engine.show_item_option:
        todo_engine.show_items()
    elif choise == todo_engine.add_item_option:
        todo_engine.add_item()
    elif choise == todo_engine.fınısh_item_option:
        todo_engine.fınısh_item()
    elif choise == todo_engine.exit_optıon:
        break
    else:
        print("Böyle Bir İşlem Yok !!")

print("Program Bitti")