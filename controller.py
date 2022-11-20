import view
import model


def menu():
    data = []
    while True:
        choice = view.show_menu()
        if choice == "":
            print("Всего хорошего!!!")
            break
        elif choice == "1":
            rec = model.create_rec(*view.new_recs())
            data.append(rec)
        elif choice == "2":
            filename = view.file_name()
            recs = model.import_file(filename)
            data.extend(recs)
        elif choice == "3":
            filename = view.file_name()
            model.export_file(filename, data)
        elif choice == "4":
            view.show_all_recs(data)
        else:
            print("Недопустимый пункт из меню!")