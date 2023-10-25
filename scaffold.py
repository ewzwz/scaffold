from random import choice

alphabet = "йцукенгшщзхъфывапролджэячсмитьбю"

pictures = (
    """
    _______
    |     
    |
    |
    |
    |
    |
    --------------
   """,
    """
    _______
    |     |
    |
    |
    |
    |
    |
    --------------
   """,
    """
    _______
    |     |
    |     o
    |
    |
    |
    |
    --------------
""",
    """
    _______
    |     |
    |     o
    |     |
    |
    |
    |
    --------------
""",
    """
    _______
    |     |
    |     o
    |    /|
    |
    |
    |
    --------------
""",
    """
    _______
    |     |
    |     o
    |    /|\\
    |
    |
    |
    --------------
""",
    """
    _______
    |     |
    |     o
    |    /|\\
    |    /
    |
    |
    --------------
""",
    """
    _______
    |     |
    |     o
    |    /|\\
    |    / \\
    |
    |
    --------------
""")

words = ("скипетр", "мантия", "абракадабра", "эссенция")  # это кортеж со словами для отгадывания

print("Здравствуй, друг! Добро пожаловать на землю «Высшая школа приключений».\nНо перед началом путешествия по нашему королевству каждый должен пройти испытание «Виселица: ты или тебя» от самого короля.\nПроверь, достоин ли ты пройти по землям нашего королевства, или заслуживаешь лишь беспощадной смерти.\nОтгадай слово, и ты можешь отправляться на встречу приключениям,\nа если не отгадаешь, твоя участь быть повешенным!\n")

# чтобы начать игру
helping_variable = True
start = ''
while helping_variable:
    print("""Чтобы начать отгадывать слово, напишите "начать" """)
    start = input()
    if start == "начать" or start == "Начать":
        break

quess = choice(words) # слово которое отгадывают прямо сейчас
stage = 0  # соответствует стадии виселицы
used = list() #использованные слова

print("\nКороль загадал слово")
word = "_" * len(quess) #показывает текущее состояние слова


while stage != len(pictures) - 1 and word != quess:
    print(pictures[stage])  # выводит текущее положение виселицы
    print("Загаданное слово: ", word)
    print("Использованные буквы: ", used)   # перед угадыванием выводит список использованных букв

    #заставляет угадать букву
    letter = '123'
    while (letter not in alphabet) or (len(letter) != 1) or letter == '' or letter in used:
        print("\nУгадывайте букву:")
        letter = input().lower()
        if letter not in alphabet or len(letter) != 1 or letter == '':
            print("Вы должны ввести 1 букву русского алфавита\n")
        if letter in used:
            print("Вы уже использовали эту букву\n")

    used.append(letter) # добавляет букву в список использованных


    if letter in quess:
        word = ''
        for i in range(len(quess)):
            for j in used:
                if quess[i] == j:
                    word += j    #составляет текущее состояние слова
                    break
            if not any(k == quess[i]for k in used):
                word += "_"
    else:
        if stage != len(pictures) - 2:
            print("Вы не угадали букву и стали ближе к смерти")
        stage += 1


if stage == len(pictures) - 1:
    print("\nВы не отгадали слово и король дал приказ вас повесить :*(")
    print(pictures[-1])
if word == quess:
    print("Король загадал слово: ", word)
    print("\nВы отгадали слово и вам открылся доступ к приключению!\n ")
    print("В подарок от короля вы получаете лучшего коня из королевской конюшни!\n")
    print("__________________________________________AIgg\n",
"_____________________________________gggggggggg_\n",
"__________________________________ggggggggggg0gg\n",
"_______________________________ggggggggggggggggggg\n",
"_____ggg____ggggggg__________gggggggggggg_____ggggg\n",
"__ggggggggggggggggggggggggggggggggggggggg\n",
"_gggggg__ggggggggggggggggggggggggggggggg\n",
"gggggg___gggggggggggggggggggggggggggggg\n",
"ggggg____ggggggggggggggggggggggggggggg\n",
"gggg_____ggggggggggggggggggggggggggggg\n",
"gg_________ggggggggggggggggggggggggggg\n",
"__________gggggggg_gggggggggggggggggg\n",
"______gggggggggggg_____________ggggggg\n",
"_____gggg____gggg________________ggggg\n",
"_____ggR_____ggg___________________gggg\n",
"_____gg_____gggg___________ggg__ggggggggg\n",
"____ggg______ggg____________gggggg____ggg\n",
"__gggg_________ggg______________________gg\n",
"__gg____________ggg______________________gg\n",
"_________________gggg_____________________ggg\n",
"__________________gggg_____________________ggg\n",)
