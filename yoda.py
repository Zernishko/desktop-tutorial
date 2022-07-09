force_words = ['сила', 'пребудет', 'с', 'тобой', 'Да']
print(id(force_words))
# Место для вашего кода

first_word = force_words.pop(0)
last_word = force_words.pop()

force_words.append(last_word)
force_words.insert(0, first_word)

print(force_words)
# Убедимся, что это тот же объект, что и в начале программы
print(id(force_words))
