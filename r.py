# # from random import randint
# # from openpyxl import load_workbook
# # fn='rostik.xlsx'
# # wb=load_workbook(fn)
# # ws=wb['data']
# # wb.active=0
# # sheet=wb.active
# # def ros(a,b):
# #     for i in range(a,b):
# #         print(sheet['A'+str(i)].value,sheet['B'+str(i)].value,sheet['C'+str(i)].value)
# # ros(1,12)
# # def res (a):
# #         ws.append(['привет меня зовут диктор из канала мастерская настроения и мне',str(a),'лет'])
# # res(randint(1,100))
# # wb.save(fn)
# # wb.close()
#
# # import requests
# # requests.get('htt')
#
# # class Point:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #
# #     def get_quadrant(self):
# #         if self.x > 0 and self.y > 0:
# #             return "I четверть"
# #         elif self.x < 0 and self.y > 0:
# #             return "II четверть"
# #         elif self.x < 0 and self.y < 0:
# #             return "III четверть"
# #         elif self.x > 0 and self.y < 0:
# #             return "IV четверть"
# #         else:
# #             return "Точка находится на оси координат"
# # x = float(input("Введите координату x: "))
# # y = float(input("Введите координату y: "))
# # point = Point(x, y)
# # quadrant = point.get_quadrant()
# # print("Точка с координатами ({}, {}) находится в {}".format(point.x, point.y, quadrant))
#
# # answer = input('Желаете познакомиться с необычным ассортиментом?')
# # if answer == 'да':
# #     product = input('Введите вид товара:')
# #     if product == 'напиток':
# #         taste = input ('Введите вкус:')
# #         if taste=='лимонный':
# #             print('Попробуйте лимонад Лайм-Кактус!')
# #         if taste == 'яблочный':
# #             print('Попробуйте газировку Печёное яблоко')
# #         elif taste!='лимонный' and 'яблочный':
# #             print('Попробуйте напиток Озорная ежевика')
# #     else:
# #         print('Попробуйте можжевеловый пирог!')
# # else:
# #     print('Жаль! Будем ждать вас')
#
#
# # class MyFunctions:
# #     @staticmethod
# #     def is_year_leap(year):
# #         if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
# #             return True
# #         else:
# #             return False
# #
# # print(MyFunctions.is_year_leap(2020))
# #
#
#
# # class MyFunctions:
# #     @staticmethod
# #     def season(month):
# #         if month in [12, 1, 2]:
# #             return "зима"
# #         elif month in [3, 4, 5]:
# #             return "весна"
# #         elif month in [6, 7, 8]:
# #             return "лето"
# #         elif month in [9, 10, 11]:
# #             return "осень"
# #         else:
# #             return "Ошибка: неверно указан номер месяца"
# # print(MyFunctions.season(4))
#
# # class MyFunctions:
# #     @staticmethod
# #     def arithmetic(a, b, op):
# #         if op == "+":
# #             return a + b
# #         elif op == "-":
# #             return a - b
# #         elif op == "*":
# #             return a * b
# #         elif op == "/":
# #             return a / b
# #         else:
# #             return "Неизвестная операция"
# # print(MyFunctions.arithmetic(2, 3, "+"))
#
# # class Person:
# #     def __init__(self, name, age, gender):
# #         self.name = name
# #         self.age = age
# #         self.gender = gender
# #
# #     def get_income(self):
# #         return 0
# #
# #     def get_expenses(self):
# #         return 0
# #
# #
# # class Preschooler(Person):
# #     def __init__(self, name, age, gender):
# #         super().__init__(name, age, gender)
# #
# #
# # class Schoolkid(Person):
# #     def __init__(self, name, age, gender):
# #         super().__init__(name, age, gender)
# #
# #
# # class Student(Person):
# #     def __init__(self, name, age, gender):
# #         super().__init__(name, age, gender)
# #
# #
# # class Employee(Person):
# #     def __init__(self, name, age, gender, company, salary):
# #         super().__init__(name, age, gender)
# #         self.company = company
# #         self.salary = salary
# #
# #     def get_income(self):
# #         return self.salary
# #
# #     def get_expenses(self):
# #         return 50000
# #
# #
# # person_type = input("Выберите тип персоны (дошкольник, школьник, студент, работающий): ")
# #
# # if person_type == "дошкольник":
# #     person = Preschooler("Иванов Иван", 5, "мужской")
# # elif person_type == "школьник":
# #     person = Schoolkid("Петров Петр", 12, "мужской")
# # elif person_type == "студент":
# #     person = Student("Сидорова Анна", 20, "женский")
# # elif person_type == "работающий":
# #     person = Employee("Козлов Игорь", 30, "мужской", "ООО Рога и копыта", 100000)
# # else:
# #     print("Ошибка: неверный тип персоны")
# #     exit()
# #
# # print("Имя:", person.name)
# # print("Возраст:", person.age)
# # print("Пол:", person.gender)
# # print("Средний доход:", person.get_income())
# # print("Средние расходы:", person.get_expenses())
# #
#
#
# #
# # n = int(input("Введите количество чисел: "))
# # positive_sum = 0
# # negative_count = 0
# #
# # for i in range(n):
# #     number = float(input(f"Введите число {i + 1}: "))
# #     if number > 0:
# #         positive_sum += number
# #     elif number < 0:
# #         negative_count += 1
# #
# # print("Сумма положительных чисел:", positive_sum)
# # print("Количество отрицательных чисел:", negative_count)
#
# # word1 = input("Введите первое слово: ")
# # word2 = input("Введите второе слово: ")
# #
# # if word1[-1] == word2[0]:
# #     print("Правильно")
# # else:
# #     print("Неправильно")
#
#
# #
import telebot
import random


bot = telebot.TeleBot('5926623824:AAGkmuLaRKdO8KsIgqtL1NbiVjbBeNV8Fek')

games = ["21", "крестики-нолики", "лото"]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для выбора игры. Напиши /game, чтобы получить случайную игру из списка.')
@bot.message_handler(commands=['game'])
def game(message):
    game = random.choice(games)
    bot.send_message(message.chat.id, f"Сегодня ты будешь играть в: {game}")
@bot.message_handler(func=lambda message: True)
def echo(message):
    if message.text.lower() in games:
        if message.text.lower() == 'лото':
            bot.send_message(message.chat.id, 'Привет! Я бот для игры в лото. Напиши /play, чтобы начать игру.')
            bot.register_next_step_handler(message,q)
def q(message):
    bot.send_message(message.chat.id, 'Начинаем игру!')
    card = random.sample(range(1, 91), 15)
    card.sort()
    bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хочешь продолжить игру? (да/нет)'),process_answer,card)
def process_answer(message, card):
    answer = message.text.lower()
    if answer == 'да':
        number = random.randint(1, 90)
        bot.send_message(message.chat.id, f'Выпало число {number}!')
        if number in card:
            card.remove(number)
            bot.send_message(message.chat.id, 'Ты отметил это число на твоей карте лото!')
            if len(card) == 0:
                bot.send_message(message.chat.id,'Поздравляем, ты выиграл! Ты заполнил всю свою карту лото.')
            else:
                bot.send_message(message.chat.id, 'Это число не на твоей карте лото.')
                bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хочешь продолжить игру? (да/нет)'), process_answer,card)
    elif answer == 'нет':
        bot.send_message(message.chat.id, 'Хорошо, игра окончена.')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю, ты хочешь продолжить игру или нет?')
        bot.send_message(message.chat.id,'напиши /play если хочешь начать занового играть')
        #
        # elif message.text.lower() == "21":
        #     bot.send_message(message.chat.id, 'Привет! Я бот для игры в "21".\nНапиши /play, чтобы начать игру.')
        #     @bot.message_handler(commands=['play'])
        #     def play(message):
        #         bot.send_message(message.chat.id, 'Начинаем игру!')
        #         player_cards = [random.randint(2, 11) for _ in range(2)]
        #         dealer_card = random.randint(2, 11)
        #         bot.send_message(message.chat.id, f'Твои карты: {player_cards}. Сумма очков: {sum(player_cards)}')
        #         bot.send_message(message.chat.id, f'Карта дилера: {dealer_card}')
        #         if sum(player_cards) < 21:
        #             message = bot.send_message(message.chat.id, 'Хочешь взять еще одну карту? (да/нет)')
        #             bot.register_next_step_handler(message, hit_me, player_cards=player_cards, dealer_card=dealer_card)
        #     def hit_me(message, player_cards, dealer_card):
        #         if message.text == 'да':
        #             player_cards.append(random.randint(2, 11))
        #             bot.send_message(message.chat.id, f'Твои карты: {player_cards}. Сумма очков: {sum(player_cards)}')
        #             bot.send_message(message.chat.id, f'Карта дилера: {dealer_card}')
        #             if sum(player_cards) >= 21:
        #                 bot.send_message(message.chat.id, 'Игра окончена!')
        #                 return
        #             message = bot.send_message(message.chat.id, 'Хочешь взять еще одну карту? (да/нет)')
        #             bot.register_next_step_handler(message, hit_me, player_cards=player_cards, dealer_card=dealer_card)
        #         elif message.text == 'нет':
        #             while dealer_card < 17:
        #                 dealer_card += random.randint(2, 11)
        #             bot.send_message(message.chat.id, f'Твои карты: {player_cards}. Сумма очков: {sum(player_cards)}')
        #             bot.send_message(message.chat.id, f'Карты дилера: {dealer_card}. Сумма очков: {dealer_card}')
        #             if sum(player_cards) > dealer_card or dealer_card > 21:
        #                 bot.send_message(message.chat.id, 'Поздравляем, ты выиграл!')
        #             elif sum(player_cards) < dealer_card:
        #                 bot.send_message(message.chat.id, 'К сожалению, ты проиграл.')
        #             else:
        #                 bot.send_message(message.chat.id, 'Ничья!')
        #         else:
        #             bot.send_message(message.chat.id, 'Некорректный ответ. Хочешь взять еще одну карту? (да/нет)')
        #             bot.register_next_step_handler(message, hit_me, player_cards=player_cards, dealer_card=dealer_card)
        # elif message.text.lower() == "крестики-нолики":
        #     bot.send_message(message.chat.id, 'Привет! Я бот для игры в крестики-нолики".\nНапиши /play, чтобы начать игру.')
        #     @bot.message_handler(commands=['play'])
        #     def draw_board(chat_id):
        #         game_state = {}
        #         board = ''
        #         for i in range(1, 10):
        #             if i in game_state:
        #                 board += game_state[i]
        #             else:
        #                 board += '-'
        #             if i % 3 == 0:
        #                 board += '\n'
        #         bot.send_message(chat_id, board)
        #     def check_winner():
        #         game_state = {}
        #         if ((1 in game_state and 2 in game_state and 3 in game_state and game_state[1] == game_state[2] ==
        #              game_state[3]) or
        #                 (4 in game_state and 5 in game_state and 6 in game_state and game_state[4] == game_state[5] ==
        #                  game_state[6]) or
        #                 (7 in game_state and 8 in game_state and 9 in game_state and game_state[7] == game_state[8] ==
        #                  game_state[9]) or
        #                 (1 in game_state and 4 in game_state and 7 in game_state and game_state[1] == game_state[4] ==
        #                  game_state[7]) or
        #                 (2 in game_state and 5 in game_state and 8 in game_state and game_state[2] == game_state[5] ==
        #                  game_state[8]) or
        #                 (3 in game_state and 6 in game_state and 9 in game_state and game_state[3] == game_state[6] ==
        #                  game_state[9]) or
        #                 (1 in game_state and 5 in game_state and 9 in game_state and game_state[1] == game_state[5] ==
        #                  game_state[9]) or
        #                 (3 in game_state and 5 in game_state and 7 in game_state and game_state[3] == game_state[5] ==
        #                  game_state[7])):
        #             return True
        #         else:
        #             return False
        #     def start_command(message):
        #         game_state = {}
        #         bot.send_message(message.chat.id,
        #                          'Привет! Давай сыграем в крестики-нолики. Чтобы поставить крестик или нолик, отправь номер ячейки (от 1 до 9).')
        #         game_state.clear()
        #         draw_board(message.chat.id)
        #     @bot.message_handler(func=lambda message: True)
        #     def handle_message(message):
        #         game_state = {}
        #         if message.text.isdigit():
        #             cell = int(message.text)
        #             if cell < 1 or cell > 9:
        #                 bot.send_message(message.chat.id, 'Номер ячейки должен быть от 1 до 9.')
        #             elif cell in game_state:
        #                 bot.send_message(message.chat.id, 'Эта ячейка уже занята.')
        #             else:
        #                 if len(game_state) % 2 == 0:
        #                     game_state[cell] = 'X'
        #                 else:
        #                     game_state[cell] = 'O'
        #                 draw_board(message.chat.id)
        #                 if check_winner():
        #                     bot.send_message(message.chat.id, f'Игрок {len(game_state) % 2 + 1} победил')
bot.polling()





#
# import telebot
# import random
# bot = telebot.TeleBot('5926623824:AAGkmuLaRKdO8KsIgqtL1NbiVjbBeNV8Fek')
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет! Я бот для игры в лото. Напиши /play, чтобы начать игру.')
# @bot.message_handler(commands=['play'])
# def q(message):
#     bot.send_message(message.chat.id, 'Начинаем игру!')
#     card = random.sample(range(1, 91), 15)
#     card.sort()
#     bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хочешь продолжить игру? (да/нет)'), process_answer, card=card)
#
#
# def process_answer(message, card):
#     answer = message.text.lower()
#     if answer == 'да':
#         number = random.randint(1, 90)
#         bot.send_message(message.chat.id, f'Выпало число {number}!')
#         if number in card:
#             card.remove(number)
#             bot.send_message(message.chat.id, 'Ты отметил это число на твоей карте лото!')
#             if len(card) == 0:
#                 bot.send_message(message.chat.id, 'Поздравляем, ты выиграл! Ты заполнил всю свою карту лото.')
#         else:
#             bot.send_message(message.chat.id, 'Это число не на твоей карте лото.')
#         bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хочешь продолжить игру? (да/нет)'), process_answer, card=card)
#     elif answer == 'нет':
#         bot.send_message(message.chat.id, 'Хорошо, игра окончена.')
#     else:
#         bot.send_message(message.chat.id, 'Я не понимаю, ты хочешь продолжить игру или нет?')
#         bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хочешь продолжить игру? (да/нет)'), process_answer, card=card)
# bot.polling()
#
#
#
#
# #
# # import telebot
# #
# # # создаем экземпляр бота
# # bot = telebot.TeleBot('5926623824:AAGkmuLaRKdO8KsIgqtL1NbiVjbBeNV8Fek')
# #
# game_state = {}
# def draw_board(chat_id):
#     board = ''
#     for i in range(1, 10):
#         if i in game_state:
#             board += game_state[i]
#         else:
#             board += '-'
#         if i % 3 == 0:
#             board += '\n'
#     bot.send_message(chat_id, board)
# def check_winner():
#     if ((1 in game_state and 2 in game_state and 3 in game_state and game_state[1] == game_state[2] == game_state[3]) or
#         (4 in game_state and 5 in game_state and 6 in game_state and game_state[4] == game_state[5] == game_state[6]) or
#         (7 in game_state and 8 in game_state and 9 in game_state and game_state[7] == game_state[8] == game_state[9]) or
#         (1 in game_state and 4 in game_state and 7 in game_state and game_state[1] == game_state[4] == game_state[7]) or
#         (2 in game_state and 5 in game_state and 8 in game_state and game_state[2] == game_state[5] == game_state[8]) or
#         (3 in game_state and 6 in game_state and 9 in game_state and game_state[3] == game_state[6] == game_state[9]) or
#         (1 in game_state and 5 in game_state and 9 in game_state and game_state[1] == game_state[5] == game_state[9]) or
#         (3 in game_state and 5 in game_state and 7 in game_state and game_state[3] == game_state[5] == game_state[7])):
#         return True
#     else:
#         return False
# def start_command(message):
#     bot.send_message(message.chat.id, 'Привет! Давай сыграем в крестики-нолики. Чтобы поставить крестик или нолик, отправь номер ячейки (от 1 до 9).')
#     game_state.clear()
#     draw_board(message.chat.id)
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     if message.text.isdigit():
#         cell = int(message.text)
#         if cell < 1 or cell > 9:
#             bot.send_message(message.chat.id, 'Номер ячейки должен быть от 1 до 9.')
#         elif cell in game_state:
#             bot.send_message(message.chat.id, 'Эта ячейка уже занята.')
#         else:
#             if len(game_state) % 2 == 0:
#                 game_state[cell] = 'X'
#             else:
#                 game_state[cell] = 'O'
#             draw_board(message.chat.id)
#             if check_winner():
#                 bot.send_message(message.chat.id, f'Игрок {len(game_state) % 2 + 1} победил')
# bot.polling()
#
#
# import telebot
# import random
#
# bot = telebot.TeleBot('5926623824:AAGkmuLaRKdO8KsIgqtL1NbiVjbBeNV8Fek')
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет! Я бот для игры в "21".\nНапиши /play, чтобы начать игру.')
# @bot.message_handler(commands=['play'])
# def play(message):
#     bot.send_message(message.chat.id, 'Начинаем игру!')
#     player_cards = [random.randint(2, 11) for _ in range(2)]
#     dealer_card = random.randint(2, 11)
#     bot.send_message(message.chat.id, f'Твои карты: {player_cards}. Сумма очков: {sum(player_cards)}')
#     bot.send_message(message.chat.id, f'Карта дилера: {dealer_card}')
#     if sum(player_cards) < 21:
#         message = bot.send_message(message.chat.id, 'Хочешь взять еще одну карту? (да/нет)')
#         bot.register_next_step_handler(message, hit_me, player_cards=player_cards, dealer_card=dealer_card)
#
# def hit_me(message, player_cards, dealer_card):
#     if message.text == 'да':
#         player_cards.append(random.randint(2, 11))
#         bot.send_message(message.chat.id, f'Твои карты: {player_cards}. Сумма очков: {sum(player_cards)}')
#         bot.send_message(message.chat.id, f'Карта дилера: {dealer_card}')
#         if sum(player_cards) >= 21:
#             bot.send_message(message.chat.id, 'Игра окончена!')
#             return
#         message = bot.send_message(message.chat.id, 'Хочешь взять еще одну карту? (да/нет)')
#         bot.register_next_step_handler(message, hit_me, player_cards=player_cards, dealer_card=dealer_card)
#     elif message.text == 'нет':
#         while dealer_card < 17:
#             dealer_card += random.randint(2, 11)
#         bot.send_message(message.chat.id, f'Твои карты: {player_cards}. Сумма очков: {sum(player_cards)}')
#         bot.send_message(message.chat.id, f'Карты дилера: {dealer_card}. Сумма очков: {dealer_card}')
#         if sum(player_cards) > dealer_card or dealer_card > 21:
#             bot.send_message(message.chat.id, 'Поздравляем, ты выиграл!')
#         elif sum(player_cards) < dealer_card:
#             bot.send_message(message.chat.id, 'К сожалению, ты проиграл.')
#         else:
#             bot.send_message(message.chat.id, 'Ничья!')
#     else:
#         bot.send_message(message.chat.id, 'Некорректный ответ. Хочешь взять еще одну карту? (да/нет)')
#         bot.register_next_step_handler(message, hit_me, player_cards=player_cards, dealer_card=dealer_card)
# bot.polling()
