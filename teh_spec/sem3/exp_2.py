import re
from collections import Counter

def count_words(text):
    # Избавляемся от знаков препинания
    text = re.sub(r'[^\w\s]', '', text)
    # Приводим все слова к нижнему регистру и разбиваем на список
    words = re.findall(r'\w+', text.lower())
    # Подсчитываем количество встречаемых слов
    word_counts = Counter(words)
    # Возвращаем 10 самых частых слов
    return word_counts.most_common(10)

# Пример использования
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis mauris id lectus pretium mattis. Sed aliquet rutrum sapien, id tincidunt velit tempor id. Praesent vestibulum facilisis laoreet. Sed blandit tincidunt purus, et posuere est laoreet id. Donec consequat condimentum sem a accumsan. Sed faucibus ultrices odio vitae commodo. Nam blandit, turpis eget laoreet ullamcorper, lacus massa bibendum leo, eu efficitur orci leo non orci. Integer a odio ut nibh porta imperdiet. Etiam eleifend purus nulla, quis congue velit viverra consectetur. Sed tincidunt est orci, eu placerat justo blandit ac. Integer et iaculis ligula. Maecenas consectetur convallis dui, at lobortis lorem tempor et. Fusce eu erat rutrum, sollicitudin elit id, aliquam tortor. Morbi pharetra lacus enim, eu consequat arcu pretium a."
most_common_words = count_words(text)
for word, count in most_common_words:
    print(f"{word}: {count}")