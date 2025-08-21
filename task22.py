import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }

    },
    2: {
        "Каа": {
            "Вид питомца": "Желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}


def get_pet(ID):
    if ID in pets:
        return pets[ID]
    else:
        return False


def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
        return "года"
    else:
        return "лет"


def pets_list():
    for ID, info in pets.items():
        for name, data in info.items():
            print(
                f"ID: {ID} | {data['Вид питомца']} по кличке \"{name}\". "
                f"Возраст: {data['Возраст питомца']} {get_suffix(data['Возраст питомца'])}. "
                f"Хозяин: {data['Имя владельца']}"
            )


def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1

    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print("Питомец успешно добавлен!")


def read():
    ID = int(input("Введите ID питомца: "))
    pet = get_pet(ID)
    if pet:
        for name, data in pet.items():
            print(f"Это {data['Вид питомца']} по кличке \"{name}\"."
                  f"Возраст питомца: {data['Возраст питомца']} {get_suffix(data['Возраст питомца'])}."
                  f"Имя владельца: {data['Имя владельца']}")
    else:
        print("Питомца с таким ID нет.")


def update():
    ID = int(input("Введите ID питомца для обновления: "))
    pet = get_pet(ID)
    if pet:
        for name, data in pet.items():
            print("Старая информация:", data)

            new_name = input(
                "Введите новую кличку (оставьте пустым, если без изменений): ")
            new_type = input(
                "Введите новый вид питомца (оставьте пустым, если без изменений): ")
            new_age = input(
                "Введите новый возраст (оставьте пустым, если без изменений): ")
            new_owner = input(
                "Введите нового владельца (оставьте пустым, если без изменений): ")

            if new_name:
                pets[ID] = {new_name: pet[name]}
                name = new_name
            if new_type:
                pets[ID][name]["Вид питомца"] = new_type
            if new_age:
                pets[ID][name]["Возраст питомца"] = int(new_age)
            if new_owner:
                pets[ID][name]["Имя владельца"] = new_owner

            print("Информация обновлена.")
    else:
        print("Питомца с таким ID нет.")


def delete():
    ID = int(input("Введите ID питомца для удаления: "))
    if ID in pets:
        del pets[ID]
        print("Питомец удален.")
    else:
        print("Питомца с таким ID нет")


command = ""
while command != "stop":
    command = input(
        "\nВведите команду (create, read, update, delete, list, stop): ")

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Программа завершена")
    else:
        print("Неизвестная команда")
