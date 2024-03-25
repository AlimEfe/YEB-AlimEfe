show_items_optıon = "1"
add_item_option = "2"
fınısh_item_option = "3"
exit_optıon = "4"


todo_list ={"görevini": False,
            "görevnceoru":False}

def show_menu():
    menu_text ="1. Listedeki Görevleri Göster\n 2. Listeye Görev Ekle\n 3. Elemen Tamamla\n 4. Çıkış"

    return input(menu_text)


def show_items():
    item_index = 1
    for name,status in todo_list:
        status_text = "Yapılmadı"
        if status:
            print(item_index, ".görev =",name,",durumu  yapıldı")
    else:
        print(item_index,"görev =", "durumu yapılmadı")


def add_item():
    item_text = input("Görevi Giriniz\n")
    todo_list[item_text] = False

def finish_item():
    item_index = int(input("görev numarasını giriniz"))
    for name,status in todo_list :
        item_index -= 1 
        if item_index == 0:
            todo_list[name]=True
            break