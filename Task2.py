# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random


def choice_player():  # Выбор с кем играть человек-компьютер
    while True:
        choice = input('С кем бы Вы хотели играть? Человек или компьютер?:\n')
        if choice.lower() == 'человек':
            return True
        elif choice.lower() == 'компьютер':
            return False
        elif choice == 'выход':
            exit()
        else:
            print('Пожалуйста убедитесь, что Вы ввели "человек" или "компьютер"!\nДля выхода из игры введите "выход".')


def selection_difficulty():  # Выбор уровня сложности
    while True:
        selection = input('Выберите уровень сложности!\n1. Простой\n2. Средний\n3. Сложный\nВведите цифру: ')
        if selection.isdigit() and 0 < int(selection) < 4:
            return int(selection)
        else:
            print('Пожалуйста убедитесь, что Вы ввели корректную цифру!')


def first_player(diff):  # Определяем кто первый ходит (если сложность 3, то первый ходит ПК)
    while True:
        coin_side = ['орел', 'решка']
        coin = input('Подбросим монетку, что бы определить кто первый ходит. Игрок №1 выберите "орел" или "решка"?:\n')
        if coin.lower() in coin_side:
            if diff == 3:  # Если сложность №3
                side = coin_side[not bool(coin_side.index(coin))]  # Получаем сторону противоположную выбору игрока
                print(f'К сожалению у Вас {side}. Компьютер ходит первый.')
                return False
            else:
                side = coin_side[random.randint(0, 1)]
                if side in coin:
                    print(f'Поздравляем! У Вас {side}. Вы ходите первый!')
                    return True
                else:
                    print(f'К сожалению у Вас {side}. Противник ходит первый.')
                    return False
        else:
            print('Пожалуйста убедитесь, что Вы ввели "орел" или "решка"!')


def game_people(first_p):  # Игра человек-человек
    base = 2021  # Общее кол-во конфет на столе
    players_list = ['Игрок №1', 'Игрок №2']
    if first_p:
        player = False
    else:
        player = True
    while True:
        player_takes = input(f'{players_list[player]} введите количество конфет сколько Вы возьмете: ')
        if player_takes.isdigit() and 0 < int(player_takes) < 29 and int(player_takes) <= base:
            base = base - int(player_takes)
            if base == 0:
                print(
                    f'На столе не осталось конфет! Победил {players_list[player]}! Примите поздравления! Игра окончена!')
                exit()
            else:
                print(f'На столе осталось {base} конфет, ходит следующий игрок!')
                player = not player
        else:
            print('Вы можете взять не меньше одной и не более 28 конфет!')


def game_pc(dif, first_p):  # Игра человек-ПК
    players_list = ['Компьютер', 'Игрок']
    player = first_p
    base = 2021  # Общее кол-во конфет на столе
    if dif == 3:
        base = base - 20
        print(f'Компьютер берет 20 конфет, на столе осталось {base} конфет.')
        player = not player
    while True:
        if player:  # Если ходит человек
            player_takes = input(f'{players_list[player]} введите количество конфет сколько Вы возьмете: ')
            if player_takes.isdigit() and 0 < int(player_takes) < 29 and int(player_takes) <= base:
                base = base - int(player_takes)
                print(f'На столе осталось {base} конфет. Ход компьютера.')
            else:
                print('Вы можете взять не меньше одной и не более 28 конфет!')
                continue
        else:  # Ходит ПК
            if base < 28:
                if dif == 1:  # Если сложность 1, то ПК будет поддаватся
                    if base != 1:  # Что-бы избежать ошибки если осталась 1 конфета
                        pc_takes = random.randint(1, base - 1)
                    else:
                        pc_takes = 1
                else:
                    pc_takes = base
                base = base - pc_takes
                print(f'Компьютер берет {pc_takes} конфет, на столе осталось {base} конфет.')
            else:
                if dif == 3:  # Если сложность 3 ПК побеждает
                    pc_takes = 29 - int(player_takes)
                else:
                    pc_takes = random.randint(1, 28)
                base = base - pc_takes
                print(f'Компьютер берет {pc_takes} конфет, на столе осталось {base} конфет.')
        if base == 0:
            print(f'На столе не осталось конфет! Победил {players_list[player]}! Примите поздравления! Игра окончена!')
            exit()
        player = not player


def main():
    print('Приветствуем Вас в игре!\nПравила игры:\nНа столе лежит 2021 конфета, за один ход каждый участник берет '
          'не менее одной и не более 28 конфет.\nПобеждает участник который заберет последние конфеты.')
    player = choice_player()  # Человек - True, Компьютер - False
    if not player:  # Если игра против ПК
        difficulty = selection_difficulty()  # Сложность 1-пк поддается, 2-рандом, 3-пк выигрывает
        first = first_player(difficulty)  # Игрок 1 - True, Игрок2(ПК) - False
        game_pc(difficulty, first)
    else:  # Если играют люди
        game_people(first_player(0))


if __name__ == '__main__':
    main()
