from random import choice

#здесь должен появиться кортеж с рисунками виселицы
max_mistakes = 7
words = ("скипетр", "мантия" )# это кортеж со словами для отгадывания

#тут пользователь должен начать отгадывать слово, которое ему загадал король, либо умереть

#вместо этого комментария должен оказаться print с историей почему король вас отправил на виселицу

helping_variable = True
start = ''
while helping_variable:
    print("""Чтобы начать отгадывать слово, напишите "начать"\nЕсли вы не хотите даже пытаться, напишите "сдаться" """)
    start = input()
    if start == "начать" or start == "Начать" or start == "сдаться" or start == "Сдаться":
        break

quess = choice(words)
correct = False
right_letters = list(str(c) for c in quess)
attempts = 0
stage = 0 #соответствует стадии виселицы

print("\nКороль загадал слово")
print("[] " * len(quess))


while attempts < max_mistakes or not correct:
    print("\nУгадывайте букву:")
    letter = input()
    if letter in quess:

    else:
        stage += 1




