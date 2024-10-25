import random

# Параметри персонажа
arthur_health = 100
arthur_attack = 20
arthur_dodge_chance = 0.3  # шанс уникнути атаки

# Параметри бандитів
bandit_health = 30
bandit_attack = 10
number_of_bandits = 3  # кількість бандитів


def start_battle():
    global arthur_health
    print("Артур наближається до табору і бачить трьох бандитів.")
    print("Він мусить здолати їх, щоб продовжити свій шлях.")

    for bandit_number in range(1, number_of_bandits + 1):
        print(f"\nБій проти бандита {bandit_number}")
        current_bandit_health = bandit_health

        while current_bandit_health > 0:
            print(f"\nЗдоров'я Артура: {arthur_health}")
            print(f"Здоров'я бандита {bandit_number}: {current_bandit_health}")
            print("\nЩо зробити?")
            print("1. Атакувати")
            print("2. Спробувати ухилитися")

            choice = input("Введіть 1 або 2: ")

            if choice == '1':
                # Атака Артура
                damage = random.randint(arthur_attack - 5, arthur_attack + 5)
                current_bandit_health -= damage
                print(f"Артур завдає {damage} одиниць шкоди бандиту!")

                # Перевірка чи бандит переможений
                if current_bandit_health <= 0:
                    print(f"Бандит {bandit_number} переможений!")
                    break

                # Атака бандита у відповідь
                if random.random() > arthur_dodge_chance:
                    arthur_health -= bandit_attack
                    print(f"Бандит атакує та завдає Артуру {bandit_attack} одиниць шкоди!")
                else:
                    print("Артур ухиляється від атаки!")

            elif choice == '2':
                # Спроба ухилитися
                if random.random() < arthur_dodge_chance:
                    print("Артур успішно ухилився від атаки!")
                else:
                    arthur_health -= bandit_attack
                    print(f"Артур не зміг ухилитися і отримує {bandit_attack} одиниць шкоди!")

            else:
                print("Будь ласка, виберіть 1 або 2.")

            # Перевірка, чи Артур ще живий
            if arthur_health <= 0:
                print("Артур зазнав поразки. Гра закінчена.")
                return

    # Перемога
    print("\nАртур здолав усіх бандитів і знаходить карту!")
    print("Ця карта показує шлях до печери дракона. Пригода триває...")


# Початок гри
start_battle()
