adwentures_of_tom_sawer = """
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print("Task 01:\n", adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print("Task 02:\n", adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split())
print("Task 03:\n", adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

h_count = adwentures_of_tom_sawer.count('h')
print("Task 04:\n", h_count)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

words = adwentures_of_tom_sawer.split()
capitalized_count = 0
for word in words:
        if word[0].isupper():
            capitalized_count += 1

print("Task 05:\n", capitalized_count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_index = adwentures_of_tom_sawer.find("Tom")
second_index = adwentures_of_tom_sawer.find("Tom", first_index + 1)
print("Task 06:\n", second_index)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None

# task 07_1 With regex module
import re
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?])\s+', adwentures_of_tom_sawer)
print("Task 07_1:\n", adwentures_of_tom_sawer_sentences)

# task 07_2 With additional separator
adwentures_of_tom_sawer_sentences = []
text = adwentures_of_tom_sawer
for sep in ['.', '!', '?']:
    text = text.replace(sep, sep + '|')
adwentures_of_tom_sawer_sentences = [sentence.strip() for sentence in text.split('|') if sentence.strip()]
print("Task 07_2:\n", adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print("Task 08:\n", fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
by_the_time = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        by_the_time = True
        break

print("Task 09:\n", by_the_time)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-1]
last_sentence_words_count = len(last_sentence.split())
print("Task 10:\n", last_sentence_words_count)