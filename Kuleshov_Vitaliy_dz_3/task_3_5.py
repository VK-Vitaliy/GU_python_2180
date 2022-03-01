# 5.	Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
import random


def get_jokes(x, flag=False):
    """ x - number of jokes, flag=False allows to use repeats in the jocks"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    for i in range(x):
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        if flag:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
        jokes_list.append(f'{noun} {adverb} {adjective}')

    return jokes_list


print(get_jokes(5, True))
