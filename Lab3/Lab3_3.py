# TODO  Напишите функцию count_letters
def count_letters(str_):
    str_ = str_.lower()
    list_of_count_letters = {}

    for letter in str_:
        if letter.isalpha():
            if letter in list_of_count_letters:
                list_of_count_letters[letter] += 1
            else:
                list_of_count_letters[letter] = 1

    return list_of_count_letters

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_dict):
    total_letters = sum(letter_dict.values())
    frequency_dict = {}

    for letter, count in letter_dict.items():
        frequency = count / total_letters
        frequency_dict[letter] = frequency

    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
frequencies = calculate_frequency(count_letters(main_str))

# Распечатка результатов
for letter, freq in frequencies.items():
    print(f"{letter}: {freq:.2f}")
