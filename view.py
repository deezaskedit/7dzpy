def new_recs() -> dict:
    print("Ввод новой записи:")
    surname = input("Введите фамилию:")
    name = input("Введите имя:")
    tel = input("Введите номер телефона:")
    desc = input("Введите описание:")
    return surname, name, tel, desc


def file_name() -> str:
    return input("Введите имя файла:")


def show_recs(data: dict):
    for val in data.values():
        print(val, end=" ")
    print("")


def show_all_recs(data: list):
    print("Записи в справочнике:")
    for rec in data:
        show_recs(rec)


def show_menu() -> str:
    print("-Меню:")
    print("\t1 - Ввод новой записи:")
    print("\t2 - Имрорт из файла:")
    print("\t3 - Экспорт в файла:")
    print("\t4 - Вывод на экран содержимого справочника:")
    return input("Выберите нужный пункт")