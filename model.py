def create_rec(surname, name, tel, desc) -> dict:
    return {'surname': surname, 'name': name, 'tel': tel, 'desc': desc}


def import_file(filename: str, delimiter =",") ->list:
    rez = []
    with open(filename, mode = "r", encoding="utf-8") as file:
        for line in file:
            surname, name, tel, desc = line.strip().split(delimiter)
            rez.append({'surname': surname, 'name': name, 'tel': tel, 'desc': desc})
    return rez


def export_file(filename: str, data: list, delimiter = ","):
    with open(filename, mode= "w", encoding="utf-8:") as file:
        for rec in data:
            file.write(",".join(rec.values()))
            file.write(f"\n")


if __name__ == "__main__":
    print(import_file("data1.txt"))

    data_test = [
        {'surname': 'Фамилия1', 'name': 'Имя1', 'tel': 'Телефон1', 'desc': 'Описание1'},
        {'surname': 'Фамилия2', 'name': 'Имя2', 'tel': 'Телефон2', 'desc': 'Описание2'},
        {'surname': 'Фамилия3', 'name': 'Имя3', 'tel': 'Телефон3', 'desc': 'Описание3'},
        {'surname': 'Фамилия4', 'name': 'Имя4', 'tel': 'Телефон4', 'desc': 'Описание4'},
    ]

    print(export_file("data2.txt", data_test))
    print(import_file("data2.txt"))