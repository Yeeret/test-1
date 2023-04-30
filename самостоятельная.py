# # # 1
# f=open('temp.txt ','r', encoding='utf-8')
# s=''
# for x in f:
#     s+=x
# d=open('Демьян ТОП!!!!!.txt','w',encoding='utf-8')
# d.writelines(s)
# 2
# def kal():
#     f=open('temp.txt','r',encoding='utf-8')
#     for x in f:
#         x=x.replace('\n','')
#         print([x])
# kal()
#
# # 3
# f=open('temp.txt','r',encoding='utf-8')
# s=''
# for x in f:
#     s+=x
# s=s.replace(' ','')
# s=s.replace('\n','')
# print(s)
# 4
# a=input()
# f=open('Демьян ТОП!!!!!.txt', 'a+', encoding='utf-8')
# while a!='Конец':
#     f.writelines(a)
#     a=input()

#try:
#     with open('temp.txt','r+',encoding='utf-8') as f:
#         s=''
#         for x in f:
#             s+=x
#         s=s.replace('\n','')
#         print(s)
#         f.close()
# except FileExistsError:
#     print('Ошибка файла')
# finally:
#     f.close()
# 1
# a=input()
# c=0
# with open('temp.txt','r',encoding='utf-8') as f:
#     s=f.readlines()
# for i in range(len(s)):
#     s[i]=s[i].replace('\n','')
# for i in range(len(s)):
#     s[i]=s[i].split()
# for i in range(len(s)):
#     for j in range(len(s[i])):
#         if s[i][j]==a:
#             c+=1
# print(f'Ваше слово встречалось {c} раз')
# 2
# with open('Ros.txt','r',encoding='utf-8') as f:
#     s=''
#     for x in f:
#         s+=x
#     s=s.split()
#     c=str(sorted(s))
#     with open('Демьян ТОП!!!!!.txt','w',encoding='utf-8') as f:
#         f.write(c)
# 4
# with open('temp.txt', 'r', encoding='utf-8') as f:
#     s = f.readlines()
# c=0
# for i in range(len(s)):
#     s[i] = s[i].replace('\n','')
# for i in range(len(s)):
#     s[i] = s[i].split()
# for i in range(len(s)):
#     for j in range(len(s[i])):
#         if len(s[i][j]) > 5 :
#             c+=1
# print(c)
# 5
# a='a','b','c','d','e','f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',' w', 'x', 'y', 'z'
# with open('Ros.txt','w',encoding='utf-8') as f:
#     for i in range(len(a)):
#         f.write(str(a[i])+'\n')
# 3
# from random import randint
#
# with open('temp.txt','r',encoding='utf-8') as f:
#     s=''
#     for i in f:
#         s+=i
#         s=s.split()
#         b=len(s)
#         a=randint(0,b-1)
#     print(a)

# 7
# str = "чтобы сделаться не абстрагировать агр агр"
# R=list(filter(lambda w:(w.startswith('a')),str))
# print(R)
# 8
# x=[1,2,3,4,5,6]
# x = list(map(lambda a : a+10,x))
# print(x)
#
# try:
#     with open('Демьян ТОП!!!!!.txt','r',encoding='utf-8') as f:
#         print(f)
# except FileNotFoundError:
#     print('такого файла нет')
# 6
# s=[]
# x=[1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20]
# x = list(filter(lambda a : a%2==0,x))
# s.append(x)
# print(*s)
# 5
# try:
#     a=int(input('Ввeди число от 1 до 10'))
#     if a == 1:
#         print('I')
#     elif a == 2:
#         print('II')
#     elif a == 3:
#         print('III')
#     elif a == 4:
#         print('IV')
#     elif a == 5:
#         print('V')
#     elif a == 6:
#         print('VI')
#     elif a == 7:
#         print('VII')
#     elif a == 8:
#         print('VIII')
#     elif a == 9:
#         print('IX')
#     elif a == 10:
#         print('X')
# except ValueError:
#     print('Ты ввёл неправильно введи ещё раз')
#



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
    bot.send_message(message.chat.id, f"Сегодня ты будешь играть в: {game},напишии /play если тебе выпало 21 или /start_game если у тебя выпало лото")
@bot.message_handler(commands=['play'])
def play(message):
    bot.send_message(message.chat.id, 'Начинаем игру в "21"!')
    player_cards = [random.randint(2, 11) for _ in range(2)]
    dealer_card = random.randint(2, 11)
    bot.send_message(message.chat.id, f'Твои карты: {player_cards}. Сумма очков: {sum(player_cards)}')
    bot.send_message(message.chat.id, f'Карта дилера: {dealer_card}')
    if sum(player_cards) < 21:
        message = bot.send_message(message.chat.id, 'Хочешь взять еще одну карту? (да/нет)')
        bot.register_next_step_handler(message, hit_me, player_cards=player_cards, dealer_card=dealer_card)

@bot.message_handler(commands=['start_game'])
def q(message):
    if "лото" in games:
        bot.send_message(message.chat.id, 'Начинаем игру в лото!')
        card = random.sample(range(1, 91), 15)
        card.sort()
        bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хочешь продолжить игру? (да/нет)'), process_answer, card=card)
    else:
        bot.send_message(message.chat.id, 'К сожалению, игра в лото недоступна. Попробуйте выбрать другую игру.')

def process_answer(message, card):
    answer = message.text.lower()
    if answer == 'да':
        number = random.randint(1, 90)
        bot.send_message(message.chat.id, f'Выпало число {number}!')
        if number in card:
            card.remove(number)
            bot.send_message(message.chat.id, 'Ты отметил это число на твоей карте лото!')
            if len(card) == 0:
                bot.send_message(message.chat.id, 'Поздравляем, ты выиграл! Ты заполнил всю свою карту лото.')
                bot.send_message(message.chat.id, 'Напиши /restart, чтобы начать игру заново.')
            else:
                bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хочешь продолжить игру? (да/нет)'), process_answer, card=card)
        else:
            bot.send_message(message.chat.id, 'Это число не на твоей карте лото.')
            bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хочешь продолжить игру? (да/нет)'), process_answer, card=card)
    elif answer == 'нет':
        bot.send_message(message.chat.id, 'Хорошо, игра окончена.')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю, ты хочешь продолжить игру или нет?')
        bot.register_next_step_handler(bot.send_message(message.chat.id, 'Хочешь продолжить игру? (да/нет)'), process_answer, card=card)

def hit_me(message, player_cards, dealer_card):
    if message.text == 'да':
        player_cards.append(random.randint(2, 11))
        bot.send_message(message.chat.id, f'Твои карты: {player_cards}. Сумма очков: {sum(player_cards)}')
        bot.send_message(message.chat.id, f'Карта дилера: {dealer_card}')
        if sum(player_cards) >= 21:
            bot.send_message(message.chat.id, 'Игра окончена!')
            return
        message = bot.send_message(message.chat.id, 'Хочешь взять еще одну карту? (да/нет)')
        bot.register_next_step_handler(message, hit_me, player_cards=player_cards, dealer_card=dealer_card)
    elif message.text == 'нет':
        while dealer_card < 17:
            dealer_card += random.randint(2, 11)
        bot.send_message(message.chat.id, f'Твои карты: {player_cards}. Сумма очков: {sum(player_cards)}')
        bot.send_message(message.chat.id, f'Карты дилера: {dealer_card}. Сумма очков: {dealer_card}')
        if sum(player_cards) > dealer_card or dealer_card > 21:
            bot.send_message(message.chat.id, 'вы выиграли')
        else:
            bot.send_message(message.chat.id,'ты проиграл')
bot.polling()